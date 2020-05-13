class ArithmeticCoder:
    #32 makes most sense
    def __init__(self, numbits):
#         self.b = numbits #- 2
#         self.lb = 1 << (self.b-2)
#         self.hb = 1 << (self.b-1)
#         self.tb = (1 << self.b) #- 1
#         self.mask = (1 << self.b) - 1
        
        self.b = numbits - 2
        self.lb = 1 << (self.b-2)
        self.hb = 1 << (self.b-1)
        self.tb = (1 << self.b) - 1
        self.mask = (1 << self.b) - 1
        
        self.R: int  = int()
        self.L: int  = int()
        self.D: int  = int()
        self.bits_waiting: int  = int()
        self.output = None
        self.input = None
        
#         self.b = numbits 
#         self.tb = 1<< self.b
#         self.hb = self.tb >> 1
#         self.lb = self.hb >> 1
#        self.mask = self.tb - 1 # mask == top point in Christian's code
        
    def start_encode(self, output):
        self.output = output
        self.L: int = 0
        self.R: int = self.tb
        self.bits_waiting: int = 0
        
    def getRange(self):
        return self.R
    
    def getTarget(self, t = None):
        if t is not None:
            r = self.R // t
            dr = (self.D - self.L) // r
            return t - 1 if (t-1 < dr) else dr
        else:
            return self.D - self.L
    def narrow_region(self, l, h, t = None):
        if t is not None:
            r = self.R // t
            self.L = self.L + r * l
            self.R = r * (h - l) if h < t else self.R - r * l
        else:
            self.L = self.L + l
            self.R = h - l
    #Encode
    def encode(self, l, h, t = None):
        self.narrow_region(l,h,t)
        output_bits()
        
    def encode_0(Self, e, x):
        e.encode(x, self)
        
    def storeRegion(self, l, h, t = None):
        self.narrow_region(l,h,t)
        try:
            self.output_bits()
        except:
            pass
#         except IOException as e:
#             raise RuntimeException(e)
        

    def output_bits(self):
        while self.R <= self.lb:
            if self.L + self.R <= self.hb:
                self.bit_plus_follow(int(0))
            elif self.L >= self.hb:
                self.bit_plus_follow(int(1))
                self.L = self.L - self.hb
            else:
                self.bits_waiting += 1
                self.L = self.L - self.lb
            self.L = self.L << 1
            self.R = self.R << 1 
        
    def  bit_plus_follow(self,bit):
        self.output.write(bit) #bytes
        while self.bits_waiting > 0:
            self.output.write(int((1 - bit))) #bytes
            self.bits_waiting -= 1  
            
#     def output_bits(self):
#         self.H = self.L + self.R - 1
#         while ((self.L ^ self.H) & self.hb) == 0:
#             bit = self.low >> (self.b - 1)
#             self.output.write(bit)#bytes
#             for _ in range(self.bits_waiting):
#                 self.output.write(bit ^ 1)#bytes
#             self.bits_waiting = 0
#             self.L  = ((self.L  << 1) & self.mask)
#             self.H = ((self.H << 1) & self.mask) | 1
#         while (self.L & ~self.H & self.lb) != 0:
#             self.bits_waiting += 1
#             self.L = (self.L << 1) ^ self.hb
#             self.H = ((self.H ^ self.hb) << 1) | self.hb | 1
#         self.R = self.H - self.L + 1
          
    def finish_encode(self,output):
        while True:
            if self.L + (self.R >> 1) >= self.hb:
                self.bit_plus_follow(int(1))
                if self.L < self.hb:
                    self.R -= self.hb - self.L
                    self.L = 0
                else:
                    self.L -= self.hb
            else:
                self.bit_plus_follow(int(0))
                if self.L + self.R > self.hb:
                    self.R = self.hb - self.L
            if self.R == self.hb:
                break
            else:
                if self.R == self.L:
                    raise IllegalStateException("R = L = " + self.R)
            self.L <<= 1
            self.R <<= 1
            
    def start_decode(self, in_, pad1 = False):
        #self.input = BitReaderSequence.appendZeros(in_)
        self.input = in_
        k = 0
        while k < self.b:
            self.D <<= 1
            self.D += self.input.read()
            k += 1
        self.L = 0
        self.R = self.tb
        
    def decode(self, d):
        symbol = d.decode(self)
        
    def loadRegion(self, l, h, t = None):
        self.narrow_region(l, h, t)
        try:
            self.discard_bits()
        except:
            pass
#         except IOException as e:
#             raise RuntimeException(e)
    
    def discard_bits(self):
        while self.R <= self.lb:
            if self.L >= self.hb:
                self.L -= self.hb
                self.D -= self.hb
            elif self.L + self.R <= self.hb:
                pass
            else:
                self.L -= self.lb
                self.D -= self.lb
            self.L <<= 1
            self.R <<= 1
            self.D <<= 1
            self.D &= self.mask
            self.D += self.input.read()
            
    def finish_decode(self):
        pass
    
    def debugout(cls, d):
        print(str(d))
        

# Supporting classes
        
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