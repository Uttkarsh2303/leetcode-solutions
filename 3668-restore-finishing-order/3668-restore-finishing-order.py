class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans=[]
        hashset=set(friends)
        for i in order:
            if i in hashset:
                ans.append(i)
        return ans