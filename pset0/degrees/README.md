# Degrees of Separation

This project is part of the **CS50’s Introduction to Artificial Intelligence with Python** course, specifically for Problem Set 0: **Degrees**. The program finds the shortest path between two actors/actresses by connecting them through movies they've starred in together, demonstrating a "degrees of separation" problem similar to the "Six Degrees of Kevin Bacon" game.

---

## Project Overview

The goal of the project is to determine the shortest path between two people based on the movies they have appeared in together. This problem is represented as a graph, where:

- **Nodes** represent actors/actresses.
- **Edges** represent movies connecting two actors/actresses.

The program uses **Breadth-First Search (BFS)** to find the shortest path between two actors, ensuring that it explores all possible connections in an optimal manner.

---

## Files in the Repository

1. **`degrees.py`**: The main Python program that loads data, prompts the user for input, and finds the shortest path using BFS.
2. **`util.py`**: Contains helper classes for the graph search:
   - `Node`: Represents a single node in the search tree.
   - `StackFrontier`: Implements a stack-based frontier for depth-first search (not used in this project).
   - `QueueFrontier`: Implements a queue-based frontier for breadth-first search.
3. **CSV Files** (provided by CS50 AI course):
   - `people.csv`: Contains information about actors/actresses (IDs, names, and birth years).
   - `movies.csv`: Contains information about movies (IDs, titles, and release years).
   - `stars.csv`: Connects people to movies they starred in.

---

## How the Program Works

1. The program loads data from the CSV files into memory.
2. The user is prompted to enter the names of two actors/actresses.
3. Using BFS, the program searches for the shortest path between the two actors.
4. If a connection exists, the program outputs the degrees of separation and lists the movies and co-stars involved in each connection step.
5. If no connection exists, the program informs the user that the two actors are not connected.

---

## Example Usage

```bash
$ python degrees.py small
Loading data...
Data loaded.
Name: Emma Watson
Name: Daniel Radcliffe
2 degrees of separation.
1: Emma Watson and Rupert Grint starred in Harry Potter and the Sorcerer's Stone
2: Rupert Grint and Daniel Radcliffe starred in Harry Potter and the Chamber of Secrets
```

## Breadth-First Search Implementation

The **BFS algorithm** is implemented in the `shortest_path` function:

1. **Initialize** the frontier with the starting actor.
2. **Explore nodes level by level**:
   - Check if the current node is the target.
   - If not, add its neighbors (actors connected by movies) to the frontier.
3. **Track explored nodes** to avoid revisiting them.
4. **Return the path** if found, or `None` if no connection exists.

---

## Key Functions

### `load_data(directory)`

Loads data from the CSV files (`people.csv`, `movies.csv`, `stars.csv`) into memory.

Populates three data structures:

- **`names`**: Maps names to a set of corresponding person IDs.
- **`people`**: Maps person IDs to details (name, birth year, movies).
- **`movies`**: Maps movie IDs to details (title, year, stars).

### `shortest_path(source, target)`

Finds the shortest path between the source and target actors using BFS.

Returns a list of `(movie_id, person_id)` pairs representing the path.

### `person_id_for_name(name)`

Resolves a person's name to their corresponding ID, handling ambiguities by prompting the user.

### `neighbors_for_person(person_id)`

Returns `(movie_id, person_id)` pairs for all people who starred in movies with the given person.
