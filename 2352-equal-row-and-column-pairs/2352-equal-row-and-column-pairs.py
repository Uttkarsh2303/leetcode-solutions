class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        set1=set()
        set2=set()
        final=[]
        temp=[]
        for i in grid:
            set1.add(tuple(i))
        for j in range(len(grid[0])):
            for i  in range(len(grid)):
                temp.append(grid[i][j])
            final.append(temp)
            temp=[]

        count=0
        for i in grid:
            for j in final:
                if i==j:
                    count+=1
        return count