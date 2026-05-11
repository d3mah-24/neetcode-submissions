class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hash={"}":"{",")":"(","]":"["}
        for a in s:
            if not hash.get(a):
                stack.append(a) 
            elif not stack or stack[-1]!=hash.get(a):
                return False 
            else:
                stack.pop()
        return not stack