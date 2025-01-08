from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# These common clauses can be applied to every KB
common_KB = And(
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave))
)

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    common_KB,
    Implication(AKnight, And(AKnight, AKnave)), # If A is a knight, they are telling the truth
    Implication(AKnave, Not(And(AKnight, AKnave))) # If A is a knave, they are telling the lie.
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    common_KB,
    Implication(AKnight, And(AKnave, BKnave)), # If A is a knight, then it is telling the truth
    Implication(AKnave, Not(And(AKnave, BKnave))) # If B is a knave, then it is teling the lie.
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    common_KB,
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))), # If A is telling the truth, then both are of same kind
    Implication(AKnave, Not(Or(And(AKnight, BKnight), And(AKnave, BKnave)))), # If A is telling a lie, then both are of different kind
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))), # If B is telling the truth, then both are of different kind
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight)))) # If B is teling a lie, then both are of same kind
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    common_KB,
    Implication(AKnight, Or(AKnight, AKnave)), # If A is telling the truth, it is either one of those
    Implication(AKnave, Not(Or(AKnight, AKnave))), # If A is telling a lie, it is not either one of those
    Implication(BKnight, Implication(AKnight, BKnave)),
    Implication(BKnave, Implication(AKnave, Not(BKnave))),
    Implication(BKnight, CKnave),
    Implication(BKnave, Not(CKnave)),
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
