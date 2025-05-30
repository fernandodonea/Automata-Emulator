from include.load_functions import load_finite_automata
from include.verify_functions import verify_finite_automata


def verify_nfa(states, alphabet, delta, start, final_states):
    return verify_finite_automata(states, alphabet, delta, start, final_states, allow_epsilon=True)

def load_nfa(fn):
    return load_finite_automata(fn, verify_nfa)


def epsilon_closure(states, delta):
    closure = set(states)
    stack = list(states)
    while stack:
        state = stack.pop()
        for t in delta:
            if t[0] == state and t[1] == "eps" and t[2] not in closure:
                closure.add(t[2])
                stack.append(t[2])
    return closure


def run_nfa(nfa, input_string):
    if ' ' in input_string:
        input_string = input_string.split()
    current_states = epsilon_closure([nfa["start"]], nfa["delta"])
    print(f"Initial states: {current_states}")

    for letter in input_string:
        next_states = set()
        for state in current_states:
            for t in nfa["delta"]:
                if t[0] == state and t[1] == letter:
                    next_states.add(t[2])
        current_states = epsilon_closure(next_states, nfa["delta"])
        print(f"After input '{letter}': {current_states}")

    if any(state in nfa["final_states"] for state in current_states):
        print("String accepted.")
    else:
        print("String rejected.")