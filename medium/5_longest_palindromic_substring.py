# longest palindromic substring

# jdajslkabcbalfkadsj
# answer: abcba

class Solution:
    def find_longest_substring(self,s):
        if len(s) == 1:
            return s[0]

        def findPal(s,i,j):
            a = i
            b = j
            while a >= 0 and b < len(s) and s[a]==s[b]:
                a-=1
                b+=1
            
            return s[a+1:b]


        maxPal = s[0]
        for i in range(1,len(s)):
            if i+1 < len(s) and s[i-1] == s[i+1]:
                pal = findPal(s,i-1,i+1)
                if len(pal) > len(maxPal):
                    maxPal = pal
            if s[i-1] == s[i]:
                pal = findPal(s,i-1,i)
                if len(pal) > len(maxPal):
                    maxPal = pal
            

        print(maxPal)
        return maxPal


s = "abcdefgfedcadajslkabccbalfkadsjabbbba"
s = "aab"
Solution().find_longest_substring(s)