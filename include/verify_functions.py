

def verify_finite_automata(states, alphabet, delta, start, final_states, allow_epsilon=False):
    ok = True

    if not states:
        print("Error: The states list is empty")
        ok = False
    if len(states) != len(set(states)):
        print("Error: The states list contains duplicates")
        ok = False

    if not alphabet:
        print("Error: The alphabet list is empty")
        ok = False
    if len(alphabet) != len(set(alphabet)):
        print("Error: The alphabet list contains duplicates")
        ok = False

    if not delta:
        print("Error: The delta function is empty")
        ok = False
    for line in delta:
        if len(line) != 3:
            print(f"Error: Invalid syntax on line {delta.index(line)}: {line}")
            ok = False
        else:
            if line[0] not in states:
                print(f"Error: State {line[0]} not in the automaton's states")
                ok = False
            if line[1] not in alphabet and (not allow_epsilon or line[1] != "eps"):
                print(f"Error: Letter {line[1]} not in the automaton's alphabet or 'eps'")
                ok = False
            if line[2] not in states:
                print(f"Error: State {line[2]} not in the automaton's states")
                ok = False

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




def verify_pushdown_automata(states, input_alphabet, stack_alphabet, delta, start, final_states):
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

