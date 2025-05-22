from automata_utils import verify_automaton, load_automaton

def verify_dfa(states, alphabet, delta, start, final_states):
    return verify_automaton(states, alphabet, delta, start, final_states, allow_epsilon=False)

def load_dfa(fn):
    return load_automaton(fn, verify_dfa)


def run_dfa(dfa, string):
    string=string.split()
    current_state = dfa["start"]
    for letter in string:
        found = False
        for transition in dfa["delta"]:
            if transition[0] == current_state and transition[1] == letter:
                print(f"Transition: {transition[0]} --{letter}--> {transition[2]}")
                current_state = transition[2]
                found = True
                break
        if not found:
            print(f"Error: No transition found for state {current_state} with letter {letter}")

    if current_state in dfa["final_states"]:
        print(f"Final state: {current_state}")
        print("String accepted.")
    else:
        print(f"Final state: {current_state}")
        print("String rejected.")






