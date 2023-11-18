class VendingMachine:
    def __init__(self):
        self.bank1 = {
                0.01: 423,
                0.05: 20,
                0.1: 20,
                0.25: 20,
                1: 20,
                5: 20,
                10: 20
            }
        
        self.bank = {
                0.01: 423,
                0.05: 0,
                0.1: 0,
                0.25: 0,
                1: 0,
                5: 0,
                10: 0
            }

    def getChange(self,price,amount):
        total = round(amount - price,2)

        res = {
            0.01: 0,
            0.05: 0,
            0.1: 0,
            0.25: 0,
            1: 0,
            5: 0,
            10: 0
        }
        if total < 0:
            return "Error: amount not sufficient"
        elif total == 0:
            return res

        coins = [c for c in self.bank.keys()]
        coins.sort()
        coins.reverse()

        coinIndex = 0

        while total > 0:
            if coinIndex >= len(coins):
                print(res)
                return "Error: Not enough change"
            
            currCoin = coins[coinIndex]
            if currCoin <= total and self.bank[currCoin] > 0:
                total = round(total - currCoin,2)
                res[currCoin] += 1
                self.bank[currCoin] -= 1
            else:
                coinIndex += 1

        return res


v1 = VendingMachine()

print(v1.getChange(price=5.78,amount=10))