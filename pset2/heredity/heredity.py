import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

def get_pass_prob(parent_gene_count):
    """
    Helper function for joint probability.
    Given the number of genes a parent has (0, 1, or 2),
    return the probability that the parent passes the gene to their child.
    Takes into account the probability of mutation.
    """
    if parent_gene_count == 2:
        return 1 - PROBS["mutation"]
    elif parent_gene_count == 1:
        return 0.5
    else:
        return PROBS["mutation"]

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    joint_prob = 1

    for person in people:
        # Find the gene count of this person
        if person in two_genes:
            gene_count = 2
        elif person in one_gene:
            gene_count = 1
        else:
            gene_count = 0

        # Find if the person has any traits
        has_trait = person in have_trait

        mother = people[person]['mother']
        father = people[person]['father']

        # If the person has no parents information
        if mother is None and father is None:
            gene_prob = PROBS["gene"][gene_count]

        # If parent information are known
        else:
            # Probability that each person passes the gene
            mother_gene_count = (2 if mother in two_genes else 1 if mother in one_gene else 0)
            father_gene_count = (2 if father in two_genes else 1 if father in one_gene else 0)

            # Calculate the probability of the gene being inherited
            mother_pass_prob = get_pass_prob(mother_gene_count)
            father_pass_prob = get_pass_prob(father_gene_count)

            if gene_count == 2:
                gene_prob = mother_pass_prob * father_pass_prob
            elif gene_count == 1:
                gene_prob = (mother_pass_prob * (1 - father_pass_prob)) + ((1 - mother_pass_prob) * father_pass_prob)
            else:
                gene_prob = (1 - mother_pass_prob) * (1 - father_pass_prob)

        # Probability for having the trait
        trait_prob = PROBS["trait"][gene_count][has_trait]

        # Multiply into joint probability
        joint_prob *= gene_prob * trait_prob

    return joint_prob


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in probabilities:
        if person in one_gene:
            gene_count = 1
        elif person in two_genes:
            gene_count = 2
        else:
            gene_count = 0

        has_trait = person in have_trait

        probabilities[person]["gene"][gene_count] += p

        probabilities[person]["trait"][has_trait] += p


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        total_gene_prob = sum(probabilities[person]["gene"].values())
        if total_gene_prob > 0:
            for gene_count in probabilities[person]["gene"]:
                probabilities[person]["gene"][gene_count] /= total_gene_prob

        total_trait_prob = sum(probabilities[person]["trait"].values())
        if total_trait_prob > 0:
            for has_trait in probabilities[person]["trait"]:
                probabilities[person]["trait"][has_trait] /= total_trait_prob


if __name__ == "__main__":
    main()
