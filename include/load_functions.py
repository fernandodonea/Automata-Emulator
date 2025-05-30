
def load_finite_automata(fn, verify_function):
    try:
        with open(fn, 'r') as fin:
            states = []
            alphabet = []
            delta = []
            start = ""
            final_states = []

            lines = fin.readlines()
            section = -1 #Track wich section we are reading

            for line in lines:
                #Remove comments and whitespace
                line = line.split('#')[0].strip()
                if line:
                    if line == "[start]":
                        section += 1 #move to new section
                    elif line == "[end]":
                        continue #end current section
                    else:
                        #add the line to the appropriate section
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

            #check if the automata is valid before returning it
            if not verify_function(states, alphabet, delta, start, final_states):
                print("Error: Invalid automata")
                return None
            else:
                #organise the automata in a dictionary
                automata = {
                    "states": states,
                    "alphabet": alphabet,
                    "delta": delta, "start": start,
                    "final_states": final_states
                }
                #print the automata
                for i in automata:
                    print(f"{i}: {automata[i]}")
                return automata

    except FileNotFoundError:
        print(f"Error: File '{fn}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{fn}': {e}")
        return None



def load_pushdown_automata(fn, verify_function):
    try:
        with open(fn, 'r') as fin:
            states = []
            input_alphabet = []
            stack_alphabet = [] #Stack
            delta = []
            start = ""
            final_states = []

            lines = fin.readlines()
            section = -1

            for line in lines:
                #remove comments
                line = line.split('#')[0].strip()
                if line:
                    if line == "[start]":
                        section += 1
                    elif line == "[end]":
                        continue
                    else:
                        if section == 0:
                            states.append(line)
                        elif section == 1:
                            input_alphabet.append(line)
                        elif section == 2:
                            stack_alphabet.append(line)
                        elif section == 3:
                            delta.append(line.split())
                        elif section == 4:
                            start = line
                        elif section == 5:
                            final_states.append(line)

            if not verify_function(states, input_alphabet, stack_alphabet, delta, start, final_states):
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
                for i in pda:
                    print(f"{i}: {pda[i]}")

                return pda


    except FileNotFoundError:
        print(f"Error: File '{fn}' not found.")
        return None
    except IOError as e:
        print(f"Error reading file '{fn}': {e}")
        return None
