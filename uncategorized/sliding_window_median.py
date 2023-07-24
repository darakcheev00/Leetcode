
import heapq as hq

class Solution:
    def sliding_window_median(self,nums,k):
        res = []
        small = []
        large = []

        for i,val in enumerate(nums[:k]):
            hq.heappush(small,(-val,i))
        
        for i in range(k-(k>>1)):
            self.move(small,large)

        res.append(self.getMedian(small,large,k))

        for i, x in enumerate(nums[k:]):
            #if the incoming number is larger than the smallest large
            if x >= large[0][0]:
                hq.heappush(large,(x,i+k))
                # if the element that is being removed is smaller than the smallest large then the 
                if nums[i] <= large[0][0]:
                    self.move(large,small)
            else:
                hq.heappush(small,(-x,i+k))
                # if the element that is being popped is greater than the largest small then the median must moves left
                if nums[i] >= small[0][0]:
                    self.move(small,large)

            # the heaps are untouched if the existing elemeent is on the opposite side of the median as the
            # entering element
            while small and small[0][1] <= i:
                hq.heappop(small)
            while large and large[0][1] <= i:
                hq.heappop(large)

            res.append(self.getMedian(small,large,k))

        return res


    def move(self,one,two):
        val,i = hq.heappop(one)
        hq.heappush(two,(-1*val,i))

    def getMedian(self,small,large,k):
        if k & 1:
            #k is odd
            return large[0][0]
        else:
            # k is even
            return res.append((large[0][0] + small[0][0])/2)




nums1 = [1,3,-1,-3,5,3,6,7]
expected1 = [1,-1,-1,3,5,6]

nums2 = [1,3,-1,-3,2,1,3,6,7]
# expected2 = [3,3,2,2,3,6,7]

nums3 = [9,8,7,6,5,4,3,2,1]
# expected3 = [9,8,7,6,5,4,3]

nums4 = [1,2,3,4,1,4,-1,5,3,5]
# expected4 = [3,4,4,4,4,5,5,5]


k = 3
res = Solution().sliding_window_median(nums1, k)
print(res)

if res == expected1:
    print("Success :)")
else:
    print("Failed :(")