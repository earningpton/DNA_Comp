ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%


nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 20 -seg_len 20 c %target%.txt %target%.nncp_20208
ECHO nncp large Called


PAUSE