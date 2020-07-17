ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\DNACorpus\

ECHO %target%

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 16 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%AeCa %target%AeCa.nncp2

ECHO AeCa Called



nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%AeCa %target%AeCa.nncp

ECHO AeCa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%AgPh %target%AgPh.nncp

ECHO AgPh Called

PAUSE