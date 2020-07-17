ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%


zpaq64 a %target%_5.zpaq %target%.txt -method 5
ECHO zpaq64 Called


PAUSE