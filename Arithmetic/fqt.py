class FrequencyTable:
    def get_symbol_limit(self):
        raise NotImplementedError()
            
class FlatFrequencyTable(FrequencyTable):
    def __init__(self, numsyms):
        if numsyms < 1:
            raise ValueError("Number of symbols must be positive")
        self.numsymbols = numsyms  # Total number of symbols, which 
    def get_symbol_limit(self):
        return self.numsymbols
    def get(self, symbol):
        self._check_symbol(symbol)
        return 1
    def get_total(self):
        return self.numsymbols
    def get_low(self, symbol):
        self._check_symbol(symbol)
        return symbol
    def get_high(self, symbol):
        self._check_symbol(symbol)
        return symbol + 1
    def _check_symbol(self, symbol):
        if 0 <= symbol < self.numsymbols:
            return
        else:
            raise ValueError("Symbol out of range")
    def __str__(self):
        return "FlatFrequencyTable={}".format(self.numsymbols)
   
        
class SimpleFrequencyTable(FrequencyTable):
    def __init__(self, freqs):
        if isinstance(freqs, FrequencyTable):
            numsym = freqs.get_symbol_limit()
            self.frequencies = [freqs.get(i) for i in range(numsym)]
        else:
            self.frequencies = list(freqs)
        if len(self.frequencies) < 1:
            raise ValueError('Need at least 1 symbol')
        for freq in self.frequencies:
            if freq < 0:
                raise ValueError('Frequency can\' be negative')
        self.total = sum(self.frequencies)
        self.cumulative = None
    def get_symbol_limit(self):
        return len(self.frequencies)
    def get(self, symbol):
        self._check_symbol(symbol)
        return self.frequencies[symbol]
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
    def get_total(self):
        return self.total
    def get_low(self, symbol):
        self._check_symbol(symbol)
        if self.cumulative is None:
            self._init_cumulative()
        return self.cumulative[symbol]
    def get_high(self, symbol):
        self._check_symbol(symbol)
        if self.cumulative is None:
            self._init_cumulative()
        return self.cumulative[symbol + 1]
    def _init_cumulative(self):
        cumul = [0]
        cumsum = 0
        for freq in self.frequencies:
            cumsum += freq
            cumul.append(cumsum)
        assert cumsum == self.total
        self.cumulative = cumul
    def _check_symbol(self,symbol):
        if 0 <= symbol < len(self.frequencies):
            return
        else:
            raise ValueError('Symbol out of range')
    # For debugging
    def __str__(self):
        result = ''
        for (i, freq) in enumerate(self.frequencies):
            result += '{}\t{}\n'.format(i,freq)
        return result
class CheckedFrequencyTable(FrequencyTable):
    def __init__(self, freqtab):
        self.freqtable = freqtab
    def get_symbol_limit(self):
        result = self.freqtable.get_symbol_limit()
        if result <= 0:
            raise AssertionError(' Symbol limit is non positive')
        return result
    def get(self, symbol):
        result = self.freqtable.get(symbol)
        if not self._is_symbol_in_range(symbol):
            raise AssertionError('ValueError expected')
        if result < 0 :
            raise AssertionError('Negative symbol frequency')
        return result
    def get_total(self):
        result =  self.freqtable.get_total()
        if result < 0:
            raise AssertionError('Total frequency is negative')
        return result
    def get_low(self, symbol):
        if self._is_symbol_in_range(symbol):
            low = self.freqtable.get_low (symbol)
            high = self.freqtable.get_high(symbol)
            if not (0 <= low <= high <= self.freqtable.get_total()):
                raise AssertionError('Symbol low cumulative freq out of range')
            return low
        else:
            self.freqtable.get_low(symbol)
            raise AssertionError('ValueError expected')
    def get_high(self, symbol):
        if self._is_symbol_in_range(symbol):
            low = self.freqtable.get_low (symbol)
            high = self.freqtable.get_high(symbol)
            if not (0 <= low <= high <= self.freqtable.get_total()):
                raise AssertionError('Symbol low cumulative freq out of range')
            return high
        else:
            self.freqtable.get_high(symbol)
            raise AssertionError('ValueError expected')
    def __str__(self):
        return 'CheckedFrequencyTable (' + str(Self.freqtable) + ')'
    def set(self,symbol,freq):
        self.freqtable.set(symbol, freq)
        if not self._is_symbol_in_range(symbol) or freq < 0:
            raise Assertion('ValueError Expected')
    def increment(self, symbol):
        self.freqtable.increment(symbol)
        if not self._is_symbol_in_range(symbol):
            raise Assertion('ValueError Expected')
    def _is_symbol_in_range(self,symbol):
        return 0 <= symbol < self.get_symbol_limit()    