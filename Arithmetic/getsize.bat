

ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Fake_Ecoli

ECHO ******Method******************Size****************Bits/Byte*******

For %%I in (%target%.txt) Do set /A og=%%~zI

set decimals = 1
For %%I in (%target%*) Do (
Set "name=%%~nxI                                 "
Set "size=%%~zI                                    "
Set "bb=%ogsize%                                    "

set /A one=800
set /A kilo=1000
set /A new=%%~zI/kilo
set /A old=og/kilo
set /A div= one*new/old

Call Echo %%name:~,30%%%%size:~,20%%%%div:~0,-2%%.%%div:~-2%%)
Echo(
PAUSE