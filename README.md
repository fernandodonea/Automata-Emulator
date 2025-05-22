# Automata Simulator

This project provides a Python-based implementation for validating and simulating Deterministic Finite Automata (DFA), Nondeterministic Finite Automata (NFA), and Pushdown Automata (PDA). It includes functions to verify automaton definitions, load them from files, and simulate them with input strings.

## Features

- **DFA, NFA & PDA Validation**: Ensures the automaton definition (states, alphabet, transitions, start state, and final states) is valid.
- **DFA, NFA & PDA Loading**: Reads automaton definitions from a file.
- **DFA, NFA & PDA Simulation**: Simulates the automaton with a given input string and determines if the string is accepted or rejected.
- **Epsilon Transitions**: Supports `eps` (epsilon) transitions for NFAs and PDAs.

## Project Structure

- `dfa.py`: Contains the DFA class and methods for validation, loading, and simulation.
- `nfa.py`: Contains the NFA class and methods for validation, loading, and simulation.
- `pda.py`: Contains the PDA class and methods for validation, loading, and simulation.
- `main.py`: Main script that runs the program and interacts with the user.

- `template_dfa_nfa.txt`: Template for DFA/NFA definition files.
- `template_pda.txt`: Template for PDA definition files.
- `examples/dfa.txt`: Example DFA definition file.
- `examples/nfa.txt`: Example NFA definition file.
- `examples/pda.txt`: Example PDA definition file.
- `examples/rpgSim.txt`: Example for an RPG simulator for DFA.

## Automaton Definition Format

The definition file for DFA, NFA, and PDA should be structured as follows:

### DFA/NFA

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
### PDA
```
#states 
[start]

[end]

#input alphabet 
[start]

[end]

#stack alphabet 
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
Comments are allowed in the files, and the sections must be clearly defined.