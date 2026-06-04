class Solution:
    def isPalindrome(self, s: str) -> bool:
        
    

        # remove case senitivity
        s = s.lower()

        # remove non alphanumeric characters from the string s
        newString = ""
        for i in s:
            if i.isalnum():
                newString += i
        # Find the length of the string

        stringLength = len(newString)

        for i in range(stringLength):
            if newString[(-i)-1] != newString[i]:
                return False
        return True
        # for the length of the string, iterate from the end

        # if the character does not equal, return false
        # return true at the end of the string


