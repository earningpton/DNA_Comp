ECHO OFF

set target=C:\Users\acer\Documents\GitHub\DNA_Comp\Arithmetic\data\DNACorpus\

ECHO %target%

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 256 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%AnCa %target%AnCa.nncp

ECHO AnCa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%BuEb %target%BuEb.nncp

ECHO BuEb Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%DaRe %target%DaRe.nncp

ECHO DaRe Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%DrMe %target%DrMe.nncp

ECHO DrMe Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%EnIn %target%EnIn.nncp

ECHO EnIn Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%EsCo %target%EsCo.nncp

ECHO EsCo Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%GaGa %target%GaGa.nncp

ECHO GaGa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%HaHi %target%HaHi.nncp

ECHO HaHi Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%HePy %target%HePy.nncp

ECHO HePy Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%HoSa %target%HoSa.nncp

ECHO HoSa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%OrSa %target%OrSa.nncp

ECHO OrSa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%PlFa %target%PlFa.nncp

ECHO PlFa Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%ScPo %target%ScPo.nncp

ECHO ScPo Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%WaMe %target%WaMe.nncp

ECHO WaMe Called

nncp -n_layer 4 -hidden_size 352 -n_symb 256 -batch_size 8 -lr 4e-3 -time_steps 24 -seg_len 24 c %target%YeMi %target%YeMi.nncp

ECHO YeMi Called



PAUSE