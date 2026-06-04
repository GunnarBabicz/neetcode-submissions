class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {"]" : "[",")" :"(", "}" :"{"}
        for i in s:
            if i in hashMap:
                if stack and stack[-1] == hashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack) == 0
        