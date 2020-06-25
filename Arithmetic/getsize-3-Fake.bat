

ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\ecoli\Fake_Ecoli

ECHO ******Method******************Size****************Bits/Byte*******

For %%I in (%target%.txt) Do set /A og=%%~zI

set decimals = 1
For %%I in (%target%*) Do (
Set "name=%%~nxI                                 "
Set "size=%%~zI                                    "
Set "bb=%ogsize%                                    "

set /A one=8000
set /A kilo=10000
set /A new=%%~zI/kilo
set /A old=og/kilo
set /A div= one*new/old

Call Echo %%name:~,30%%%%size:~,20%%%%div:~0,-3%%.%%div:~-3%%)
Echo(
PAUSE