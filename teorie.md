
# Deterministic finite automaton Emulator

Sa se scrie o functie care primeste ca parametru un DFA si un cuvant si verifica daca acel cuvant este acceptat de automat.

Exemplu de DFA:
```
Q={q1,q1,...,qn} //stare 
```
```
sigma={0,1} //alfabetul
```
```
delta: Q x sigma -> Q //functia de tranzitie

q0,0,q1
q0,1,q1
q1,0,q1
q1,1,q0
```
```
start=q0 //starea de start
```
```
F={q1} //starile finale
```

Recomandare de input pentru fisier -> **sectiuni**
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

