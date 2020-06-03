from typing import List
import numpy as np
from plist import ProbabilityList
from itertools import groupby

class SingleBlockEncoding(ProbabilityList):
    def set(self, symbol, freq):
        self._check_symbol(symbol)
        if freq < 0:
            raise ValueError('Frequency can\'t be negative')
        temp = self.total - self.frequencies[symbol]
        assert temp >= 0
        self.frequencies[symbol] = freq
        self.cumulative = None
    def increment(self, symbol):
        self._check_symbol(symbol)
        self.frequencies[symbol] += 1
        self.total += 1
        self.cumulative = None

def SBE_f_2file(s: List[int], order: List[int] = None)-> List[int]:
    # First, converts ATCGATCG to A10001000T100100C1010G11EOF to A8T6C4G and 100010001001001010
    s_arr = np.array(s)
    sbe1 = [] # list of characters and length
    sbe2 = [] # only binary list
    i = 0
    j = 0
    while len(s_arr)>0:
        if order is not None:
            if s_arr[i] != order[j]:
                i += 1
        else:
            try:
                sbe2 += list(checklist*1)
            except:
                pass
            
            cur_block = s_arr[i]
            sbe1 += [cur_block]
            sbe1 += [len(s_arr)]
            checklist = (np.ones([len(s_arr)])*cur_block==s_arr)
            s_arr = s_arr[~checklist]
            i= 0
            j += 1
    # last one is always 11111111 so no need to get another sbe2
    return sbe1, sbe2

def SBE_b_2file(sbe1: List[int], sbe2: List[int])-> List[int]:
    s = np.zeros(sbe1[1]) # length of sbe1
    sbe2 = np.array(sbe2)
    first = True
    while len(sbe1) > 0:
        cur_char = sbe1.pop(0)
        block_len = sbe1.pop(0)
        try:
            sbe1[0] # if last value in the list, we put in all 1s since we have no sbe2
            cur_block = sbe2[:block_len]
            sbe2 = sbe2[block_len:] # update sbe2
        except:
            cur_block = np.ones(block_len)
        
        insert_loc = (s==0) # insert location
        s[insert_loc] = cur_block*cur_char
        
    return s

def SBE_f(s: List[int], order: List[int] = None)-> List[int]:
    # First, converts ATCGATCG to A10001000T100100C1010G11EOF
    s_arr = np.array(s)
    sbe = [] # list
    i = 0
    j = 0
    while len(s_arr)>0:
        if order is not None:
            if s_arr[i] != order[j]:
                i += 1
        else:
            cur_block = s_arr[i]
            sbe += [cur_block]
            checklist = (np.ones([len(s_arr)])*cur_block==s_arr)
            s_arr = s_arr[~checklist]
            sbe += list(checklist*1)
            i= 0
            j += 1
    return sbe

def SBE_b(sbe: List[int])-> List[int]:
    sbe_arr = np.array(sbe)
    char_idx = (sbe_arr > 1)
    seq_len = [len(list(g)) for k, g in groupby(char_idx)]   
    char_arr = list(sbe_arr[char_idx])
    s = np.zeros(seq_len[1]) # length of sbe1 
        
    sbe2 =  sbe_arr[~char_idx]
    first = True
    while len(char_arr) > 0:
        cur_char = char_arr.pop(0)
        assert seq_len.pop(0)
        block_len = seq_len.pop(0)
        try:
            seq_len[0] # if last value in the list, we put in all 1s since we have no sbe2
            cur_block = sbe2[:block_len]
            sbe2 = sbe2[block_len:] # update sbe2
        except:
            cur_block = np.ones(block_len)
        
        insert_loc = (s==0) # insert location
        s[insert_loc] = cur_block*cur_char
        
    return s

#######################
#  Deprecated
#######################

# def SBE_b(sbe):
#     s = []
#     s_list = sbe
#     first = True
#     while len(s_list) > 0:
#         cur_block = s_list.pop(0)
#         i = 0
#         section = True
#         while section:
#             try:
#                 cur_char = s_list[0]
# #                 print(cur_block)
# #                 print(s)
#             except:
#                 return s
#             if first:
#                 if cur_char == 1:
#                     s += [cur_block]
#                     s_list.pop(0)
#                 elif cur_char == 0:
#                     s += [0]
#                     s_list.pop(0)
#                 else: # new character, no pop
#                     section = False
#                     first = False
#             else: # not first, only replace 0
#                 if i == len(s):
#                     section = False
#                 elif s[i] != 0:
#                     i += 1
#                 elif cur_char == 1:
#                     s[i] = cur_block
#                     i+= 1
#                     s_list.pop(0)
#                 elif cur_char == 0:
#                     i+= 1
#                     s_list.pop(0)
#                 else:
#                     section = False
#     return s

#######################
#  Deprecated
#######################
def SBE_convert_f(s):
    # First, converts ATCGATCG to A10001000T100100C1010G11EOF
    n = len(s)
    s_list = list(s)
    sbe = ''
    while len(s_list)>0:
        cur_block = s_list.pop(0)
        sbe += cur_block + '1'
        i = 0
        while i < len(s_list):
            if s_list[i] == cur_block:
                sbe += '1' 
                s_list.pop(i)
            else:
                sbe += '0' 
                i += 1
    return sbe

def SBE_convert_b(sbe):
    s = []
    s_list = list(sbe)
    first = True
    while len(s_list) > 0:
        cur_block = s_list.pop(0)
        i = 0
        section = True
        while section:
            try:
                cur_char = s_list[0]
            except:
                return ''.join(s)
            if first:
                if cur_char == '1':
                    s += [cur_block]
                    s_list.pop(0)
                elif cur_char == '0':
                    s += ['0']
                    s_list.pop(0)
                else: # new character, no pop
                    section = False
                    first = False
            else: # not first, only replace 0
                if i == len(s):
                    section = False
                elif s[i] != '0':
                    i += 1
                elif cur_char == '1':
                    s[i] = cur_block
                    i+= 1
                    s_list.pop(0)
                elif cur_char == '0':
                    i+= 1
                    s_list.pop(0)
                else:
                    section = False
    return ''.join(s)
