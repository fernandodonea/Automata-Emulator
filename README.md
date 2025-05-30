# Automata Emulator

**LFA Project** — Advanced Python emulator for 
Deterministic Finite Automata (DFA), Nondeterministic Finite Automata (NFA), Pushdown Automata (PDA), and Turing Machines (TM).

---

## Features

- **Supports DFA, NFA, PDA, and TM**: Simulate classical and advanced automata.
- **Automata Templates**: Quickly define new automata using customizable templates.
- **Modular Includes**: Shared loading and verification logic in `include/`.
- **Interactive Examples**: Ready-to-run sample scripts for each automaton type.
- **Clear Output**: Step-by-step computation, state transitions, and acceptance results.

---

## Project Structure

```
automata-emulator/
├── automata templates/         # Automata definition templates
├── include/
│   ├── load_functions.py       # Functions to load automata from files/templates
│   └── verify_functions.py     # Utilities for input/automata validation
├── dfa.py                     
├── nfa.py                     
├── pda.py                     
├── tm.py                      
├── main.py                    
├── examples/                  # Example files
│   ├── rpgSim.txt
│   ├── tm-copy.txt
│   ├── tm-palindrome.txt
│   └── tm-unary-addition.txt
└── README.md
```


---

## Getting Started

### Prerequisites

- Python 3.7 or newer

### Installation

Clone this repository:
```bash
git clone https://github.com/fernandodonea/automata-emulator.git
cd automata-emulator
```
Run the `main.py` script to start the emulator:
```bash
python3 main.py
```
---

## Deterministic Finite Automata 
### DFA - RPG Simulator
Acest DFA simulează un joc de tip RPG, unde jucătorul se plimba pe harta.

```
                 [secreet room]
                        ^
                        |
                        ⌄
    [kitchen] <---> [hallway]  <---> [Library]
                        ^               ^
                        |               |
                        ⌄               ⌄
                    [entrance]        [exit]

```

## Turing Machines

### TM - Unary Adition
Acest TM adună două numere în format unary.

Format de intrare:
primul_nr$al_doilea_nr@spațiu_rezultat

#### Exemplu:
Input:
    ```
    1$11@___
    ```

Output:
    ```
    Tape: X$YY@111
    ```
### TM - Palindrom Checker
Acest TM verifică dacă un cuvânt este palindrom.

Format de intrare:
sir format din `a`si `b`

#### Exemplu:
Input:
    ```
    abba
    ```

Output:
    ```
    Tape: _XYX
    Accepted: True
    ```


### TM - Copy Between Delimiters

Acest TM copiază un șir de la începutul benzii undeva pe bandă pe un segment delimitat de @

Format de intrare:
01011….$____@______@___

#### Exemplu:
Input:
    ```
    1100$___@____@__
    ```
Output:
    ```
    Tape: YYXX$___@1100@
    ```




