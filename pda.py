

from automata_utils import verify_automaton, load_automaton

def verify_pda(states, input_alphabet, stack_alphabet, delta, start, final_states):
    ok = True

    if not states:
        print("Error: The states list is empty")
        ok = False
    if len(states) != len(set(states)):
        print("Error: The states list contains duplicates")
        ok = False

    if not input_alphabet:
        print("Error: The input alphabet is empty")
        ok = False
    if len(input_alphabet) != len(set(input_alphabet)):
        print("Error: The input alphabet contains duplicates")
        ok = False

    if not stack_alphabet:
        print("Error: The stack alphabet is empty")
        ok = False
    if len(stack_alphabet) != len(set(stack_alphabet)):
        print("Error: The stack alphabet contains duplicates")
        ok = False

    if not delta:
        print("Error: The delta function is empty")
        ok = False
    for line in delta:
        if len(line) != 5:
            print(f"Error: Invalid transition syntax: {line}")
            ok = False
        else:
            if line[0] not in states:
                print(f"Error: State {line[0]} not in the automaton's states")
                ok = False
            if line[1] not in input_alphabet and line[1] != "eps":
                print(f"Error: Input symbol {line[1]} not in the input alphabet or 'eps'")
                ok = False
            if line[2] not in stack_alphabet and line[2] != "eps":
                print(f"Error: Stack symbol {line[2]} not in the stack alphabet or 'eps'")
                ok = False
            if line[3] not in states:
                print(f"Error: Next state {line[3]} not in the automaton's states")
                ok = False
            # line[4] can be 'eps' or a string of stack symbols to push

    if not start:
        print("Error: The starting state is empty")
        ok = False
    if start not in states:
        print(f"Error: Invalid starting state {start} (not in states list)")
        ok = False

    if not final_states:
        print("Error: The final states list is empty")
        ok = False
    for state in final_states:
        if state not in states:
            print(f"Error: Invalid final state {state} (not in states list)")
            ok = False

    return ok

def load_pda(fn):
    try:
        with open(fn, 'r') as fin:
            states = []
            input_alphabet = []
            stack_alphabet = []
            delta = []
            start = ""
            final_states = []

            lines = fin.readlines()
            section = -1

            for line in lines:
                line = line.split('#')[0].strip()
                if line:
                    if line == "[start]":
                        section += 1
                    elif line == "[end]":
                        continue
                    else:
                        if section == 0:
                            states = line.split()
                        elif section == 1:
                            input_alphabet = line.split()
                        elif section == 2:
                            stack_alphabet = line.split()
                        elif section == 3:
                            delta.append(line.split())
                        elif section == 4:
                            start = line
                        elif section == 5:
                            final_states.extend([x for x in line.split()])

            if not verify_pda(states, input_alphabet, stack_alphabet, delta, start, final_states):
                print("Error: Invalid PDA")
                return None
            else:
                pda = {
                    "states": states,
                    "input_alphabet": input_alphabet,
                    "stack_alphabet": stack_alphabet,
                    "delta": delta,
                    "start": start,
                    "final_states": final_states
                }
                print(pda)
                return pda
    except FileNotFoundError:
        print(f"Error: File '{fn}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{fn}': {e}")
        return None

def simulate_pda(pda, input_string):
    # Each configuration: (current_state, remaining_input, stack)
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