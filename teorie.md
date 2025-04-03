
# Deterministic finite automaton Emulator

DFA example
```
Q={q1,q1,...,qn} //state
```
```
sigma={0,1} //alphabet
```
```
delta: Q x sigma -> Q //transition function

q0,0,q1
q0,1,q1
q1,0,q1
q1,1,q0
```
```
start=q0 //start state
```
```
F={q1} //final state
```

Input file for dfa -> **sections**
```txt
#states

[start]
q0 q1
[end]

#alphabet

[start]
0 1
[end]

#transitions
[start]
q0 0 q1
q0 1 q1
q1 0 q0
q1 1 q1
[end]

#initial state
[start]
q0
[end]

#accepting states
[start]
q1
[end]

```

