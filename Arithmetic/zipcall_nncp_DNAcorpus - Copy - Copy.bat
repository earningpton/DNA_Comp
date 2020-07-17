ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\DNACorpus\

ECHO %target%



nncp -batch_size 8 -time_steps 24 -seg_len 24 c %target%HePy %target%HePy.lstm2

ECHO HePy Called

nncp c %target%PlFa %target%PlFa.lstm

ECHO HaHi Called

nncp c %target%ScPo %target%ScPo.lstm

ECHO ScPo Called

nncp c %target%EnIn %target%EnIn.lstm

ECHO EnIn Called


PAUSE