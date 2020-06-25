ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

nncp d %target%.nncp_t60_l6 %target%_t60_l6_decompressed.txt
ECHO nncp large Called

PAUSE