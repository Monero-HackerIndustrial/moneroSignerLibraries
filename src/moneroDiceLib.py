from monero.seed import Seed
import hashlib



class moneroDiceLib:
    def __init__(self):
        self.version = "0.0.1"
        self.dice_rolls = ""
        index = 0
        DEBUG = False
        self.entropy = False
        self.seed = False
    def verifyRange(self,_roll):
        try:
            _roll = int(_roll)
            if 1 <= _roll <= 6:
                return True
            else:
                False
        except:
            return False
    def minimumEntropy(self):
        entropy = len(self.dice_rolls)
        if entropy < 100:
            return False
        else:
            return True

    def calculateSeedPhrase(self):
        # Checkk minimum Entropy for dice rolls
        if self.minimumEntropy() == False:
            return False
        entropy_bytes = hashlib.sha256(dice_rolls.encode()).digest()
        hex = entropy_bytes
        hex = hex.hex()
        self.seed = Seed(hex)
        phrase = self.seed.phrase
        return phrase
    def getPublicAddress(self):
        public_address = self.seed.public_address()
        return public_address
