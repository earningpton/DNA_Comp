ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

paq8l -8 %target%.txt

ECHO paq8l Called

paq8l -d %target%.txt.paq8l

ECHO paq8l Called


PAUSE