ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

gzip -9 < %target%.txt > %target%.gz

ECHO Gzip Called

bzip2 -9 < %target%.txt > %target%.bz2

ECHO Bzip2 Called  

gtz %target%.txt

ECHO gtz Called

paq8a -8 %target%.paq8a %target%.txt

ECHO paq8a Called

paq9a a %target%.paq9a -9 %target%.txt

ECHO paq9a Called

zpaq a %target%.zpaq %target%.txt

zpaq -method 5 a %target%.zpaq5 %target%.txt

ECHO zpaq Called

7z a -tzip  %target%.7z %target%.txt  

ECHO 7z Called

PAUSE