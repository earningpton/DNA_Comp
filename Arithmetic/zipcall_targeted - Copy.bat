ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

trfcp c %target%.txt %target%.trfcp
ECHO trfcp Called

PAUSE