# automata_utils.py

def verify_automaton(states, alphabet, delta, start, final_states, allow_epsilon=False):
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


def load_automaton(fn, verify_function):
    try:
        with open(fn, 'r') as fin:
            states = []
            alphabet = []
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
                            alphabet = line.split()
                        elif section == 2:
                            delta.append(line.split())
                        elif section == 3:
                            start = line
                        elif section == 4:
                            final_states.extend([x for x in line.split()])

            if not verify_function(states, alphabet, delta, start, final_states):
                print("Error: Invalid automaton")
                return None
            else:
                automaton = {"states": states, "alphabet": alphabet, "delta": delta, "start": start, "final_states": final_states}
                print(automaton)
                return automaton
    except FileNotFoundError:
        print(f"Error: File '{fn}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{fn}': {e}")
        return None