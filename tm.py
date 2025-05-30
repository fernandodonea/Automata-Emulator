from collections import defaultdict
from include.load_functions import load_turing_machine
from include.verify_functions import verify_turing_machine

BLANK_SYMBOL = '_'


def verify_tm(states, input_alphabet, tape_alphabet, delta, start, final_states):
    """Verify the Turing machine configuration."""
    return verify_turing_machine(states, input_alphabet, tape_alphabet, delta, start, final_states)


def load_tm(fn):
    """Load a Turing machine from a file."""
    return load_turing_machine(fn, verify_turing_machine)


def preprocess_delta(delta):
    """
    Preprocess the list of transitions into a dictionary for O(1) lookup.
    Each transition is expected as [current_state, read_symbol, next_state, write_symbol, direction]
    """
    return {(t[0], t[1]): (t[2], t[3], t[4]) for t in delta}


def run_tm(tm, input_string, max_steps=10000, verbose=True):
    """
    Run a Turing machine on the given input string.
    Args:
        tm: Dictionary containing Turing machine specification.
        input_string: The input string for the Turing machine.
        max_steps: Maximum steps before halting to prevent infinite loops.
        verbose: If True, print tape and state after execution.
    Returns:
        is_accepted: bool (for compatibility with main.py)
    """
    tape = defaultdict(lambda: BLANK_SYMBOL)
    for i, ch in enumerate(input_string):
        tape[i] = ch
    head = 0
    current_state = tm["start"]
    delta = preprocess_delta(tm["delta"])

    steps = 0
    while steps < max_steps:
        symbol = tape[head]
        key = (current_state, symbol)
        if key not in delta:
            # No valid transition
            break
        next_state, write_symbol, direction = delta[key]
        tape[head] = write_symbol
        if direction == "R":
            head += 1
        elif direction == "L":
            head -= 1
        else:
            raise ValueError(f"Unknown direction: {direction}")
        current_state = next_state
        if current_state in tm["final_states"]:
            break
        steps += 1

    # Compose the tape output (trim blanks)
    if tape:
        min_index = min(tape.keys())
        max_index = max(tape.keys())
        output = ''.join(tape[i] for i in range(min_index, max_index + 1)).rstrip(BLANK_SYMBOL)
    else:
        output = ""

    is_accepted = current_state in tm["final_states"]

    if verbose:
        print("Tape:", output)
        print("Final state:", current_state)
        print("Accepted:", is_accepted)

    return is_accepted