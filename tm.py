from include.load_functions import load_turing_machine
from include.verify_functions import verify_turing_machine

def verify_tm(states, input_alphabet, tape_alphabet, delta, start, final_states):
    return verify_turing_machine(states, input_alphabet, tape_alphabet, delta, start, final_states)

def load_tm(fn):
    return load_turing_machine(fn, verify_turing_machine)


def run_tm(tm, input_string):
    tape = list(input_string) + ['_'] * 128  # Blank symbol is '_'
    head = 0
    current_state = tm["start"]

    while True:
        symbol = tape[head]
        found = False
        for t in tm["delta"]:
            # t: [current_state, read_symbol, next_state, write_symbol, direction]
            if t[0] == current_state and t[1] == symbol:
                current_state = t[2]
                tape[head] = t[3]
                head += 1 if t[4] == "R" else -1
                found = True
                break
        if not found:
            break
        if current_state in tm["final_states"]:
            break

    print("Tape:", "".join(tape).rstrip('_'))
    print("Final state:", current_state)
    return current_state in tm["final_states"]



