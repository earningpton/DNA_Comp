ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

lpaq9l 9 %target%.txt %target%.txt.lpaq9l

ECHO lpaq9l Called

lpaq9l d %target%.txt.lpaq9l %target%_lpaq9l.txt

ECHO lpaq9l Called


PAUSE