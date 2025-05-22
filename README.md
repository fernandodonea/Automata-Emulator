# DFA and NFA Emulator

This project provides a Python-based implementation for validating and simulating both Deterministic Finite Automata (DFA) and Nondeterministic Finite Automata (NFA). It includes functions to verify automaton definitions, load them from files, and simulate them with input strings.

## Features

- **DFA & NFA Validation**: Ensures the automaton definition (states, alphabet, transitions, start state, and final states) is valid.
- **DFA & NFA Loading**: Reads automaton definitions from a file.
- **DFA & NFA Simulation**: Simulates the automaton with a given input string and determines if the string is accepted or rejected.
- **Epsilon Transitions**: Supports `eps` (epsilon) transitions for NFAs.

## Project Structure

- `dfa.py`: Contains the DFA class and methods for validation, loading, and simulation.
- `nfa.py`: Contains the NFA class and methods for validation, loading, and simulation.
- `main.py`: Main script that runs the program and interacts with the user.
- `template.txt`: Template for DFA/NFA definition files.
- `examples/dfa.txt`: Example DFA definition file.
- `examples/nfa.txt`: Example NFA definition file.

## Automaton Definition Format

The definition file for both DFA and NFA should be structured as follows:

```
#states
[start]

[end]

#alphabet
[start]

[end]

#transitions
[start]

[end]

#initial state
[start]

[end]

#accepting states
[start]

[end]
```
Comments are allowed in the file, and the sections must be clearly defined. Each section should contain the relevant elements of the DFA.