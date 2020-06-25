ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

nncp d %target%.nncp %target%_nncp_decompressed.txt
ECHO nncp default Called

PAUSE