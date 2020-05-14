ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Fake_Ecoli.txt

ECHO %target%

gzip -9 < %target% > %target%.gz

ECHO Gzip Called

bzip2 -9 < %target% > %target%.bz2

ECHO Bzip2 Called  

gtz %target%

ECHO gtz Called  

PAUSE