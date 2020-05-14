ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Fake_Ecoli.txt

ECHO %target%

gzip < %target% > %target%.gz

ECHO Gzip Called

bzip2 < %target% > %target%.bz2

ECHO Bzip2 Called

PAUSE