ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%


paq8o10t -9 %target%.txt

ECHO paq8o10t Called

paq8o10t -d %target%.txt.paq8o10t %target%_test.txt

ECHO paq8o10t Called


PAUSE