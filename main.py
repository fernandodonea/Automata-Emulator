
import dfa
import nfa
import pda

choice = input("Select automaton type (dfa/nfa/pda): ").strip().lower()

if choice == "dfa":
    fn = input("Enter DFA's file name: ")
    d = dfa.load_dfa(fn)
    if not d:
        print("Invalid DFA")
    else:
        print("DFA loaded successfully")
        string = input("Enter a string: ")
        dfa.run_dfa(d, string)
elif choice == "nfa":
    fn = input("Enter NFA's file name: ")
    n = nfa.load_nfa(fn)
    if not n:
        print("Invalid NFA")
    else:
        print("NFA loaded successfully")
        string = input("Enter a string: ")
        nfa.run_nfa(n, string)
elif choice == "pda":
    fn = input("Enter PDA's file name: ")
    p = pda.load_pda(fn)
    if not p:
        print("Invalid PDA")
    else:
        print("PDA loaded successfully")
        string = input("Enter a string: ")
        accepted = pda.simulate_pda(p, string)
        if accepted:
            print("Input accepted by the PDA.")
        else:
            print("Input rejected by the PDA.")
else:
    print("Invalid choice. Please enter 'dfa', 'nfa', or 'pda'.")