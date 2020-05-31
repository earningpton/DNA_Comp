from typing import List
import numpy as np
from plist import ProbabilityList
    
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

def SBE_b(sbe):
    s = []
    s_list = sbe
    first = True
    while len(s_list) > 0:
        cur_block = s_list.pop(0)
        i = 0
        section = True
        while section:
            try:
                cur_char = s_list[0]
#                 print(cur_block)
#                 print(s)
            except:
                return s
            if first:
                if cur_char == 1:
                    s += [cur_block]
                    s_list.pop(0)
                elif cur_char == 0:
                    s += [0]
                    s_list.pop(0)
                else: # new character, no pop
                    section = False
                    first = False
            else: # not first, only replace 0
                if i == len(s):
                    section = False
                elif s[i] != 0:
                    i += 1
                elif cur_char == 1:
                    s[i] = cur_block
                    i+= 1
                    s_list.pop(0)
                elif cur_char == 0:
                    i+= 1
                    s_list.pop(0)
                else:
                    section = False
    return s

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
