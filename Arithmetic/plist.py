class ProbabilityList():
    def __init__(self, prior):
        self.prob_list = list(prior)
        if len(self.prob_list) < 1:
            raise ValueError('Need at least 1 symbol')
        for prob in self.prob_list:
            if prob < 0:
                raise ValueError('Probability can\' be negative')
        self.total = sum(self.prob_list)
        if self.total != 1:
            raise ValueError('Probability must sum up to 1')
        self.cumulative = None
    def get_symbol_limit(self):
        return len(self.prob_list)
    def _check_symbol(self,symbol):
        if 0 <= symbol < len(self.prob_list):
            return
        else:
            raise ValueError('Symbol out of range')
    def get(self, symbol):
        self._check_symbol(symbol)
        return self.prob_list[symbol]
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
        for prob in self.prob_list:
            cumsum += prob
            cumul.append(cumsum)
        assert cumsum == self.total
        self.cumulative = cumul
    # For debugging
    def __str__(self):
        result = ''
        for (i, prob) in enumerate(self.prob_list):
            result += '{}\t{}\n'.format(i,prob)
        return result