from include.verify_functions import verify_pushdown_automata
from include.load_functions import load_pushdown_automata

def verify_pda(states, input_alphabet, stack_alphabet, delta, start, final_states):
    return verify_pushdown_automata(states, input_alphabet, stack_alphabet, delta, start, final_states)


def load_pda(fn):
    return load_pushdown_automata(fn, verify_pda)


def run_pda(pda, input_string):

    from collections import deque
    initial_config = (pda["start"], input_string, ["Z"])  # Assume 'Z' is initial stack symbol
    queue = deque([initial_config])

    while queue:
        state, remaining, stack = queue.popleft()
        if not remaining and state in pda["final_states"]:
            return True
        for t in pda["delta"]:
            cur_state, in_sym, stack_sym, next_state, push_syms = t
            if state != cur_state:
                continue
            # Check input symbol
            if in_sym == "eps":
                next_input = remaining
            elif remaining and in_sym == remaining[0]:
                next_input = remaining[1:]
            else:
                continue

            # Check stack symbol
            if stack_sym == "eps":
                next_stack = stack.copy()
            elif stack and stack[0] == stack_sym:
                next_stack = stack[1:]
            else:
                continue
            # Push to stack
            if push_syms != "eps":
                for sym in reversed(push_syms):
                    next_stack.insert(0, sym)
            queue.append((next_state, next_input, next_stack))

            # Accept if in final state and input is empty
            if not next_input and next_state in pda["final_states"]:
                return True
    return False