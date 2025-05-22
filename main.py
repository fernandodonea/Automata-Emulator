import dfa
import nfa

choice = input("Select automaton type (dfa/nfa): ").strip().lower()

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
else:
    print("Invalid choice. Please enter 'dfa' or 'nfa'.")