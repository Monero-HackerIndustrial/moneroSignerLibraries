import monero

# Currently hardcoded for use in english


class seedPack:
    def __init__(self):
        self.version = "0.0.1"
        self.seeds = []
    def addSeed(self,_seed):
        self.seeds.append(_seed)

class moneroSignerLib:
    def __init__(self):
        self.version = "0.0.1"
    def test(self):
        return True
