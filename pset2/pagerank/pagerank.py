import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """

    # Return probability distribution as a dictionary
    distribution = {}
    num_pages = len(corpus)
    linked_pages = corpus[page]

    if linked_pages:
        for p in corpus:
            distribution[p] = (1 - damping_factor) / num_pages
        for linked_page in linked_pages:
            distribution[linked_page] += damping_factor / len(linked_pages)
    else:
        # If no outgoing links, treat as if it links to all pages
        for p in corpus:
            distribution[p] = 1 / num_pages

    return distribution

def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize the PageRank dictionary
    page_rank = {page: 0 for page in corpus}
    pages = list(corpus.keys())

    # Start with a random page
    current_page = random.choice(pages)

    # Perform sampling
    for _ in range(n):
        page_rank[current_page] += 1
        model = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(model.keys()), weights=model.values(), k=1)[0]

    # Normalize the PageRank values so they sum to 1
    total_samples = sum(page_rank.values())
    for page in page_rank:
        page_rank[page] /= total_samples

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Total number of pages
    num_pages = len(corpus)

    # Initialize pagerank to 1/N for each page
    pagerank = {page: 1 / num_pages for page in corpus}

    # Loop until PageRank values converge
    while True:
        new_rank = {}
        for page in corpus:
            rank = (1 - damping_factor) / num_pages

            for other_page in corpus:
                if page in corpus[other_page]:
                    rank += damping_factor * pagerank[other_page] / len(corpus[other_page])
                # If a page has no links, treat it as linking to all pages
                elif len(corpus[other_page]) == 0:
                    rank += damping_factor * pagerank[other_page] / num_pages

            new_rank[page] = rank

        # Check for convergence
        if all(abs(new_rank[page] - pagerank[page]) < 0.001 for page in pagerank):
            break

        # Update PageRank value for next iteration
        pagerank = new_rank

    return pagerank



if __name__ == "__main__":
    main()
