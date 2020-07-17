ECHO OFF

set target=C:\Users\saiou\github\DNA_Comp\Arithmetic\data\ecoli\Ecoli

ECHO %target%

nncp -n_layer 2 -hidden_size 32 -n_symb 256 -batch_size 16 -lr 4e-3 -block_len 100000 -time_steps 20 -seg_len 20 c %target%.txt %target%.nncp_huh1
ECHO nncp large Called

nncp -n_layer 3 -hidden_size 32 -n_symb 256 -batch_size 64 -lr 4e-3 -block_len 100000 -time_steps 20 -seg_len 20 c %target%.txt %target%.nncp_huh2
ECHO nncp large Called

nncp -n_layer 4 -hidden_size 32 -n_symb 256 -batch_size 16 -lr 4e-3 -block_len 100000 -time_steps 20 -seg_len 20 c %target%.txt %target%.nncp_huh3
ECHO nncp large Called

nncp -n_layer 2 -hidden_size 90 -n_symb 256 -batch_size 250 -lr 4e-3 -block_len 100000 -time_steps 60 -seg_len 6 c %target%.txt %target%.nncp_huh4
ECHO nncp large Called

nncp -n_layer 4 -hidden_size 90 -n_symb 256 -batch_size 250 -lr 4e-3 -block_len 100000 -time_steps 60 -seg_len 6 c %target%.txt %target%.nncp_huh5
ECHO nncp large Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 16 -lr 4e-3 -block_len 100000 -time_steps 20 -seg_len 20 -full_connect 1 c %target%.txt %target%.nncp_huh6
ECHO nncp large Called

PAUSE