ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\DNACorpus\

ECHO %target%



nncp -batch_size 8 -time_steps 24 -seg_len 24 c %target%DrMe %target%DrMe.lstm 

ECHO DrMe Called



PAUSE