# python

import dfa
import nfa
import pda

def prompt_automaton_file(automaton_type):
    return input(f"Enter {automaton_type.upper()}'s definition file name: ").strip()

def prompt_input_string(automaton_type):
    return input(f"Enter an input string: ").strip()

def run_dfa_simulation():
    while True:
        fn = prompt_automaton_file("dfa")
        automaton = dfa.load_dfa(fn)
        if not automaton:
            print("Invalid DFA\n")
            retry = input("Try another file? (y/n): ").strip().lower()
            if retry != 'y':
                return
        else:
            print("DFA loaded successfully")
            while True:
                string = prompt_input_string("dfa")
                dfa.run_dfa(automaton, string)
                choice = input("Enter another string? (y), Go back to main menu? (b), or Quit? (q): ").strip().lower()
                if choice == 'y':
                    continue
                elif choice == 'b':
                    return
                elif choice == 'q':
                    print("Goodbye!")
                    exit(0)
                else:
                    print("Invalid choice, going back to main menu.\n")
                    return

def run_nfa_simulation():
    while True:
        fn = prompt_automaton_file("nfa")
        automaton = nfa.load_nfa(fn)
        if not automaton:
            print("Invalid NFA\n")
            retry = input("Try another file? (y/n): ").strip().lower()
            if retry != 'y':
                return
        else:
            print("NFA loaded successfully")
            while True:
                string = prompt_input_string("nfa")
                nfa.run_nfa(automaton, string)
                choice = input("Enter another string? (y), Go back to main menu? (b), or Quit? (q): ").strip().lower()
                if choice == 'y':
                    continue
                elif choice == 'b':
                    return
                elif choice == 'q':
                    print("Goodbye!")
                    exit(0)
                else:
                    print("Invalid choice, going back to main menu.\n")
                    return

def run_pda_simulation():
    while True:
        fn = prompt_automaton_file("pda")
        automaton = pda.load_pda(fn)
        if not automaton:
            print("Invalid PDA\n")
            retry = input("Try another file? (y/n): ").strip().lower()
            if retry != 'y':
                return
        else:
            print("PDA loaded successfully")
            while True:
                string = prompt_input_string("pda")
                accepted = pda.run_pda(automaton, string)
                if accepted:
                    print("Input accepted by the PDA.")
                else:
                    print("Input rejected by the PDA.\n")
                choice = input("Enter another string? (y), Go back to main menu? (b), or Quit? (q): ").strip().lower()
                if choice == 'y':
                    continue
                elif choice == 'b':
                    return
                elif choice == 'q':
                    print("Goodbye!")
                    exit(0)
                else:
                    print("Invalid choice, going back to main menu.\n")
                    return

def main():
    print("\n=== Automata Simulator ===\n")
    while True:
        try:
            choice = input("Select automaton type (dfa/nfa/pda) or type 'quit' to exit: ").strip().lower()
            if choice in ("quit", "exit", "q"):
                print("Goodbye!")
                break
            elif choice == "dfa":
                run_dfa_simulation()
            elif choice == "nfa":
                run_nfa_simulation()
            elif choice == "pda":
                run_pda_simulation()
            else:
                print("Invalid choice. Please enter 'dfa', 'nfa', 'pda', or 'quit'.\n")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting. Goodbye!")
            break

if __name__ == "__main__":
    main()