class ArithmeticCoder:
    #32 makes most sense
    def __init__(self, numbits):
        self.b = numbits - 2
        self.lb = 1 << (self.b-2)
        self.hb = 1 << (self.b-1)
        self.tb = (1 << self.b) - 1
        self.mask = (1<<self.b) - 1
        self.R: int  = int()
        self.L: int  = int()
        self.D: int  = int()
        self.bits_waiting: int  = int()
        self.output = None
        self.input = None
        
    def start_encode(self, bitout):
        self.output = output
        self.L = 0
        self.R = self.tb
        self.bits_waiting = 0
        
    def getRange(self):
        return self.R
    def getTarget(self, t = None):
        if t is not None:
            r = self.R / t
            dr = (self.D - self.L) / r
            return t - 1 if (t-1 < dr) else dr
        else:
            return self.D - self.L
    def narrow_region(self, l, h, t = None):
        if t is not None:
            r = self.R / t
            self.L = self.L + r * l
            self.R = r * (h - l) if h < t else self.R - r * l
        else:
            self.L = self.L + l
            self.R = h - l
    #Encode
    def storeRegion(self, l, h, t = None):
        self.narrow_region(l,h,t)
        self.output_bits()

    def output_bits(self):
        while self.R <= self.lb:
            if self.L + self.R <= self.hb:
                bit_plus_follow(int(0))
            elif self.L >= self.hb:
                bit_plus_follow(int(1))
                self.L = self.L - self.hb
            else:
                self.bits_waiting += 1
                self.L = self.L - self.lb
            self.L = self.L << 1
            self.R = self.R << 1  
    def  bit_plus_follow(self,bit):
        self.output.writeBit(bit)
        while self.bits_waiting > 0:
            self.output.writeBit(int((1 - bit)))
            self.bits_waiting -= 1
        
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
            self.D += self.input.readBit()
            
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
        self.input = BitReaderSequence.appendZeros(in_)
        k = 0
        while k < self.b:
            self.D <<= 1
            self.D += self.input.readBit()
            k += 1
        self.L = 0
        #  hb
        self.R = self.tb
        
    def finish_decode(self):
        pass

        

       
            