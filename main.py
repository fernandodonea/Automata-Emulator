import dfa

fn=input("Enter DFA's file name: ")
d=dfa.load_dfa(fn)

if not d:
    print("Invalid DFA")
else:
    print("DFA loaded successfully")
    string=input("Enter a string: ")
    dfa.run_dfa(d,string)
