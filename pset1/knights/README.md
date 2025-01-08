# CS50 AI Course: Problem Set 1 – Knights and Knaves

This repository contains the solution to **Problem Set 1** of **CS50’s Introduction to Artificial Intelligence with Python**. The problem involves solving logical puzzles based on the "Knights and Knaves" puzzle theme, where characters are either **knights** (who always tell the truth) or **knaves** (who always lie).

---

## Project Overview

This project consists of two main files:

1. **`logic.py`**: Implements the logic representation and inference engine, including classes for logical symbols, conjunctions, disjunctions, negations, and implications.
2. **`puzzle.py`**: Defines specific knowledge bases for four puzzles and checks possible solutions using logical inference.

---

## How the Program Works

### **1. Knights and Knaves Logic**

Each puzzle is modeled using propositional logic. The characters in the puzzles (A, B, C) can be either knights or knaves, and the program builds a knowledge base for each puzzle by encoding the rules:

- **A character can only be either a knight or a knave, but not both**.
- **Knights always tell the truth**.
- **Knaves always lie**.

The program uses **propositional logic** to represent statements and applies **model checking** to infer whether a character is a knight or a knave.

### **2. Solving the Puzzles**

Four puzzles are provided:

- **Puzzle 0**: A says, "I am both a knight and a knave."
- **Puzzle 1**: A says, "We are both knaves." (B says nothing.)
- **Puzzle 2**: A says, "We are the same kind." B says, "We are of different kinds."
- **Puzzle 3**: A says either "I am a knight" or "I am a knave." B reports what A said and also claims that C is a knave. C says that A is a knight.

The program evaluates the truthfulness of each statement based on whether the character is a knight or a knave.

---

## Example Output

When you run the program, it prints the solution to each puzzle:

```bash
$ python puzzle.py
Puzzle 0
    A is a Knave
Puzzle 1
    A is a Knave
    B is a Knight
Puzzle 2
    A is a Knight
    B is a Knave
Puzzle 3
    A is a Knight
    B is a Knave
    C is a Knight
```

## Key Components

### **`logic.py`**

This file defines the logical framework used to solve the puzzles. Key classes include:

- **`Symbol`**: Represents a propositional symbol (e.g., "A is a Knight").
- **`And`**, **`Or`**, **`Not`**, **`Implication`**, and **`Biconditional`**: Represent logical operators.
- **`model_check(knowledge, query)`**: Uses model checking to determine if the knowledge base entails a given query.

### **`puzzle.py`**

This file defines the knowledge bases for the four puzzles and uses **`model_check`** to infer the type (knight or knave) of each character.