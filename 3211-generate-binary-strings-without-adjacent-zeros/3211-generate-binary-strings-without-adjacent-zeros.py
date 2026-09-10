class Solution:
    def validStrings(self, n: int) -> List[str]:
        result=[]
        def backtrack(path):
            if len(path)==n:
                result.append(''.join(path))
                return
            path.append('1')
            backtrack(path)
            path.pop()
            if not path or path[-1]!='0':
                path.append('0')
                backtrack(path)
                path.pop()
        backtrack([])
        return result