# DFA-Emulator


This project provides a Python-based implementation for validating and simulating Deterministic Finite Automata (DFA). 
It includes functions to verify the correctness of a DFA definition, load a DFA from a file, and simulate the DFA with a given input string.

## Features
- **DFA Validation**: Ensures the DFA definition (states, alphabet, transitions, start state, and final states) is valid.
- **DFA Loading**: Reads DFA definitions from a file.
- **DFA Simulation**: Simulates the DFA with a given input string and determines if the string is accepted or rejected.

## Project Structure
- [dfa.py](dfa.py): Contains the `DFA` class and methods for validation, loading, and simulating the DFA.
- [main.py](main.py): The main script that runs the program and interacts with the user.

- [template.txt](template.txt): Template for the DFA definition file.

- [resources/dfa.txt](examples/dfa.txt): Example DFA definition file.
- [resources/rpgSim.txt](examples/rpgSim.txt): Example DFA definition file.

## DFA Definition Format
The DFA definition file should be structured as follows using sections:


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