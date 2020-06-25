ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%


paq8a -8 %target%_test.paq8a %target%.txt

ECHO paq8a Called

paq8a %target%_test.paq8a %target%_test.txt

ECHO paq8a Called


PAUSE