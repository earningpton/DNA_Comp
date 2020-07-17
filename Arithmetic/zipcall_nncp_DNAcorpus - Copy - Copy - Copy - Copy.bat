ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\DNACorpus\

ECHO %target%



nncp -n_layer 2 -hidden_size 12 -n_symb 256 -batch_size 8 -lr 4e-3 -block_len 10000  -time_steps 24 -seg_len 24 c %target%YeMi %target%YeMi.lstm2 

ECHO YeMi Called

nncp -n_layer 2 -hidden_size 12 -n_symb 256 -batch_size 8 -lr 4e-3 -block_len 10000 -time_steps 24 -seg_len 24 c %target%BuEb %target%BuEb.lstm2 

ECHO BuEb Called

nncp -n_layer 2 -hidden_size 12 -n_symb 256 -batch_size 8 -lr 4e-3 -block_len 10000 -time_steps 24 -seg_len 24 c %target%AgPh %target%AgPh.lstm2 

ECHO AgPh Called

PAUSE