class Solution_Recursion:    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        ans = self.helper(len(coins)-1,amount)
        if ans >= 1e9: return -1
        else: return ans
        
    def helper(self,index,tar):
        if index == 0:
            # if target is divisible by the current coin
            if tar%self.coins[index] == 0:
                # the quantity of that coin to make the target
                return tar//self.coins[index]
            else:
                # not divisible, therefore not a valid combo
                return 1e9
            
        notpick = self.helper(index-1, tar)
        pick = 1e9
        
        # if the current coin is less that the target-> meaning target can be made up of those coins
        if self.coins[index] <= tar:
            pick = 1+self.helper(index, tar-self.coins[index])

        return min(pick, notpick)


