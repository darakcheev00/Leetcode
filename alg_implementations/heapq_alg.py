
class MaxHeapq:
    def __init__(self):
        self.class_name = "my maxheapq implementation"
    
    def printHeap(self, heap):
        for i in range(len(heap)):
            left = None if 2*i+1 >= len(heap) else heap[2*i+1]
            right = None if 2*i+2 >= len(heap) else heap[2*i+2]
            print(f"{heap[i]}: ({left},{right})")    

    def heapify(self, array):
        n = len(array)
        last_non_leaf = (n-2)//2

        for i in range(last_non_leaf,-1,-1):
            curr = i
            while True:
                left = 2*curr+1
                right = 2*curr+2 
                if left < n and array[curr] < array[left]:
                    largest_child = left
                else:
                    largest_child = curr

                if right < n and array[largest_child] < array[right]:
                    largest_child = right

                if largest_child == curr:
                    break

                #swap curr with largest
                temp = array[curr]
                array[curr] = array[largest_child]
                array[largest_child] = temp

                curr = largest_child


    def heappop(self, array):
        val = array.pop(0)
        self.heapify(array)
        return val
    
    def heappush(self,array,val):
        array.append(val)
        self.heapify(array)

    def heappushpop(self, array, val):
        res = array.pop(0)
        array.append(val)
        self.heapify(array)
        return res


class MinHeapq:
    def __init__(self):
        self.class_name = "my minheapq implementation"
    
    def printHeap(self, heap):
        for i in range(len(heap)):
            left = None if 2*i+1 >= len(heap) else heap[2*i+1]
            right = None if 2*i+2 >= len(heap) else heap[2*i+2]
            print(f"{heap[i]}: ({left},{right})")    

    def heapify(self, array):
        n = len(array)
        last_non_leaf = (n-2)//2

        for i in range(last_non_leaf,-1,-1):
            curr = i
            while True:
                left = 2*curr+1
                right = 2*curr+2 
                if left < n and array[curr] > array[left]:
                    smallest_child = left
                else:
                    smallest_child = curr

                if right < n and array[smallest_child] > array[right]:
                    smallest_child = right

                if smallest_child == curr:
                    break

                #swap curr with largest
                temp = array[curr]
                array[curr] = array[smallest_child]
                array[smallest_child] = temp

                curr = smallest_child


    def heappop(self, array):
        val = array.pop(0)
        self.heapify(array)
        return val
    
    def heappush(self,array,val):
        array.append(val)
        self.heapify(array)

    def heappushpop(self, array, val):
        res = array.pop(0)
        array.append(val)
        self.heapify(array)
        return res

test = [1,2,3,4,5]
hq_max = MaxHeapq()

print(test)
hq_max.heapify(test)
print(hq_max.heappop(test))
print(test)
hq_max.heappush(test,10)
print(test)
print(hq_max.heappushpop(test,7))
print(test)


test = [1,2,3,4,5]
hq_min = MinHeapq()

print(test)
hq_min.heapify(test)
print(hq_min.heappop(test))
print(test)
hq_min.heappush(test,10)
print(test)
print(hq_min.heappushpop(test,7))
print(test)
