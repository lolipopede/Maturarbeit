# Sieb des Eratosthenes fuer die Zahlen 1 bis 100.
# RAM[1..100]: 1 bedeutet prima, 0 bedeutet nicht prima.
# Die Zaehler liegen in RAM[1025..1027].
# Bedingter Sprung: "Bedingung, Ziel, Sprungbedingung, LABEL"

# i = 2, p = 2, m = 0
A=2
A, wD, nj
A=1025
D, wM, nj
A=2
A, wD, nj
A=1026
D, wM, nj
A=1027
0, wM, nj

# 0 und 1 sind keine Primzahlen.
A=0
0, wM, nj
A=1
0, wM, nj

# Alle Zahlen von 2 bis 100 zunaechst als prima markieren.
@INIT
A=1025
M, wD, nj
D, wA, nj
1, wM, nj
A=1025
M, wD, nj
D+1, wM, nj
A=1025
M, wD, nj
A=100
A-D, wD, nj
D, dw, comp>=0, INIT

# Fuer jeden Teiler p von 2 bis 10 seine Vielfachen loeschen.
@OUTER
A=1026
M, wD, nj
D, wA, nj
D+A, wD, nj
A=1027
D, wM, nj

@INNER
A=1027
M, wD, nj
D, wA, nj
0, wM, nj
A=1027
M, wD, nj
A=1026
M, wA, nj
D+A, wD, nj
A=1027
D, wM, nj
A=1027
M, wD, nj
A=100
A-D, wD, nj
D, dw, comp>=0, INNER

A=1026
M, wD, nj
D+1, wM, nj
A=1026
M, wD, nj
A=10
A-D, wD, nj
D, dw, comp>=0, OUTER
