ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

cmix -c %target%.txt %target%.cmix 
ECHO cmix Called

PAUSE