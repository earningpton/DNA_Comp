class ArithmeticCoder:
    #32 makes most sense
    def __init__(self, numbits):
        if numbits<1:
            raise ValueError('State size out of range')
        self.num_state_bits = numbits 
        self.full_range = 1<< self.num_state_bits
        self.half_range = self.full_range >> 1
        self.quarter_range = self.half_range >> 1
        self.minimum_range = self.quarter_range + 2
        #Python's native bigint avoids constraining the size of intermediate computations.
        self.maximum_total = self.minimum_range
        #Mask coding interval 1-bits.
        self.state_mask = self.full_range - 1 # mask == top point in Christian's code
        
    def start_encode(self, bitout):
        self.low = int(0)
        self.range = int(self.state_mask + 1)
        self.target = int(0)
        self.high = int(self.state_mask)
        self.output = bitout
        self.num_underflow = 0
    def getRange(self):
        self.range = self.high - self.low + 1
        return self.range
    def getTarget(self):
        return self.target - self.low
    def getTarget(self, t):
        self.range = self.high - self.low + 1
        r = self.range / t
        dr = (self.target - self.low) / r
        return t - 1 if (t-1 < dr) else dr
    
    def storeRegion_model(model, symbol):
        low = self.low
        high = self.high
        range = high - low + 1
        total = model.get_total()
        symlow = model.get_low(symbol)
        symhigh = model.get_high(symbol)
        newlow = low + l * range // t
        newhigh = low + h * range// t - 1
        self.low = newlow
        self.high = newhigh
        self.output_bits()
    #Encode
    def storeRegion(self, l, h, t = None):
        if t is not None:
            low = self.low
            high = self.high
            range = high - low + 1
            newlow = low + l * range // t
            newhigh = low + h * range// t - 1
            self.low = newlow
            self.high = newhigh
            self.output_bits()
        else:
            low = self.low
            high = self.high
            range = high - low + 1
            newlow = low + l * range
            newhigh = low + h * range - 1
            self.low = int(newlow)
            self.high = int(newhigh)
            self.output_bits()
 
    def output_bits(self):
        while ((self.low ^ self.high) & self.half_range) == 0:
            self.shift_encode()
            self.low  = ((self.low  << 1) & self.state_mask)
            self.high = ((self.high << 1) & self.state_mask) | 1
        while (self.low & ~self.high & self.quarter_range) != 0:
            self.underflow_encode()
            self.low = (self.low << 1) ^ self.half_range
            self.high = ((self.high ^ self.half_range) << 1) | self.half_range | 1
            
    def shift_encode(self):
        bit = self.low >> (self.num_state_bits - 1)
        self.output.write(bit)
        for _ in range(self.num_underflow):
            self.output.write(bit ^ 1)
        self.num_underflow = 0
    def underflow_encode(self):
        self.num_underflow += 1
    def finish_encode(self):
        self.output.write(1)
        
    def start_decode(self, bitin):
        self.low = 0
        self.range = int(self.state_mask + 1)
        self.target = int(0)
        self.high = self.state_mask
        self.input = bitin
        self.code = 0
        for _ in range(self.num_state_bits):
            self.code = self.code << 1 | self.read_code_bit()
    # decode you need to find which symbol correspond to the *value*        
    def loadRegion_binary(self, model):
        total = model.get_total()
        range = self.high - self.low + 1
        offset = self.code - self.low
        value = ((offset + 1) * total - 1)// range
        assert value * range // total <= offset
        assert 0 <= value < total
        
        start = 0
        end = model.get_symbol_limit()
        while end - start > 1:
            middle = (start + end) >> 1
            if model.get_low(middle) > value:
                end = middle
            else:
                start = middle
        assert start + 1 == end
        symbol = start
        assert model.get_low(symbol) * range // total <= offset < model.get_high(symbol)*range // total
        self 
        l = model.get_low(symbol) / total
        h = model.get_high(symbol) / total
        self.loadRegion(l,h)

#         low = self.low
#         high = self.high
#         range = high - low + 1
#         l = model.get_low(symbol)
#         h = model.get_high(symbol)
#         newlow = low + l * range // total
#         newhigh = low + h * range // total - 1
#         self.low = int(newlow)
#         self.high = int(newhigh)
#         self.discard_bits()

        return symbol
    
    # If we know exact l,h,t
    def loadRegion(self, l,h,t = None):
        if t is not None:
            low = self.low
            high = self.high
            range = high - low + 1
            newlow = low + l * range // t
            newhigh = low + h * range// t - 1
            self.low = newlow
            self.high = newhigh
            self.discard_bits()
        else:
            low = self.low
            high = self.high
            range = high - low + 1
            newlow = low + l * range
            newhigh = low + h * range - 1
            self.low = int(newlow)
            self.high = int(newhigh)
            self.discard_bits()
            
        # Have to find out and return symbol outside!
    def discard_bits(self):
        while ((self.low ^ self.high) & self.half_range) == 0:
            self.shift_decode()
            self.low  = ((self.low  << 1) & self.state_mask)
            self.high = ((self.high << 1) & self.state_mask) | 1
        while (self.low & ~self.high & self.quarter_range) != 0:
            self.underflow_decode()
            self.low = (self.low << 1) ^ self.half_range
            self.high = ((self.high ^ self.half_range) << 1) | self.half_range | 1
        
    def shift_decode(self):
        self.code = ((self.code << 1) & self.state_mask) | self.read_code_bit()
    def underflow_decode(self):
        self.code = (self.code & self.half_range) | ((self.code << 1) & (self.state_mask >> 1)) | self.read_code_bit()
    def read_code_bit(self):
        temp = self.input.read()
        if temp == -1:
            temp = 0
        return temp
        
        
#     def bit_plus_follow(self, bit):
#         self.output.writeBit(bit)
#         while self.bits_waiting > 0:
#             self.output.writeBit(int((1 - bit)))
#             self.bits_waiting -= 1
   # A stream of bits that can be read
    
# Supporting classes
class BitInputStream:
    def __init__(self, inp):
        self.input = inp
        self.currentbyte = 0 
        self.numbitsremaining = 0 #0-7
    def read(self):
        if self.currentbyte == -1:
            return -1
        if self.numbitsremaining == 0:
            temp = self.input.read(1)
            if len(temp) == 0:
                self.currentbyte = -1
                return -1
            self.currentbyte = temp[0]
            self.numbitsremaining = 8
        assert self.numbitsremaining > 0
        self.numbitsremaining -= 1
        return (self.currentbyte >> self.numbitsremaining) & 1
    def read_no_eof(self):
        result = self.read()
        if result != -1:
            return result
        else:
            raise EOFError()
    def close(self):
        self.input.close()
        self.currentbyte = -1
        self.numbitsremaining = 0

# A stream where bits can be written to.
class BitOutputStream:
    def __init__(self, out):
        self.output = out
        self.currentbyte = 0
        self.numbitsfilled = 0
    def write(self, b):
        if b not in (0,1):
            raise ValueError('Argument must be 0 or 1')
        self.currentbyte = (self.currentbyte << 1) | b
        self.numbitsfilled += 1
        if self.numbitsfilled == 8:
            towrite = bytes((self.currentbyte,))
            self.output.write(towrite)
            self.currentbyte = 0
            self.numbitsfilled = 0
    def close(self):
        while self.numbitsfilled != 0:
            self.write(0)
        self.output.close()
       
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            