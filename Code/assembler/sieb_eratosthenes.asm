# Sieb des Eratosthenes fuer die Zahlen 1 bis 100.
# Der Programmcode belegt RAM[1..83] (83 Maschinenwoerter).
# RAM[n + 83]: 1 bedeutet prima, 0 bedeutet nicht prima.
# Die Ergebnistabelle liegt deshalb in RAM[84..183].
# n, p und m sind Assembly-Variablen; ihr Inhalt wird beim Lesen direkt
# in das A-Register geladen. "name = D" speichert einen neuen D-Wert.

n=2
p=1
m=0

# 1 ist keine Primzahl. Die Zahlen 2 bis 100 als prima markieren.
A=84
0, wM, nj

@INIT
n
A, wD, nj
A=83
D+A, wA, nj
1, wM, nj
n
A, wD, nj
D+1, wD, nj
n = D
n
A, wD, nj
A=100
A-D, wD, nj
D, dw, comp>=0, INIT

# Vielfache des Kandidaten p ueberspringen, wenn p schon gestrichen ist.
@OUTER
p
A, wD, nj
D+1, wD, nj
p = D
p
A, wD, nj
A=83
D+A, wA, nj
M, wD, nj
D, dw, comp=0, OUTER

# m = 2 * p
p
A, wD, nj
p
D+A, wD, nj
m = D

# m, m+p, m+2p, ... streichen.
@INNER
m
A, wD, nj
A=83
D+A, wA, nj
0, wM, nj
m
A, wD, nj
p
D+A, wD, nj
m = D
m
A, wD, nj
A=100
A-D, wD, nj
D, dw, comp>=0, INNER

# Weiter bis p=10; p=11 wird als harmloser zusaetzlicher Teiler bearbeitet,
# danach ist die Schleife beendet.
p
A, wD, nj
A=10
A-D, wD, nj
D, dw, comp>=0, OUTER
