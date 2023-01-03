'''Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array(In Place).
In other words, arrange the elements into a sequence such that arr[1] >= arr[2] <= arr[3] >= arr[4] <= arr[5].....'''

from typing import List


class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        # code here
        #b = a
        
        if n%2 != 0:
            for i in range (1,n,2):
                if i < n:
                    a[i-1],a[i] = a[i],a[i-1]
                else:
                    a[i] = a[i]
        else:
            for i in range (1,n,2):
                if i<= n-1:
                    a[i-1],a[i] = a[i],a[i-1] 
        return a
        


        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        a=IntArray().Input(n)
        
        obj = Solution()
        obj.convertToWave(n, a)
        IntArray().Print(a)

# } Driver Code Ends