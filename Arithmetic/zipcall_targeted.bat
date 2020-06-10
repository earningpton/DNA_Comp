ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

nncp -n_layer 7 -hidden_size 512 -n_symb 256 -full_connect 1 -lr 5e-3 -n_embed_out 5 -block_len 500000 -time_steps 40 -seg_len 20 c %target%.txt %target%.nncplarge
ECHO nncp large Called

PAUSE