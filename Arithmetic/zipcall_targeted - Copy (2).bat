ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 16 -lr 4e-3 -block_len 100000 -time_steps 60 -seg_len 6 c %target%.txt %target%.nncp_t60_l6
ECHO nncp large Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 16 -lr 4e-3 -block_len 100000 -time_steps 120 -seg_len 3 c %target%.txt %target%.nncp_t120_l3
ECHO nncp large Called

PAUSE