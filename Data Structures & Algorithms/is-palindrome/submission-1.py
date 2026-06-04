class Solution:

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1
        return True








        # simplest solution:

        """
        newStr = ""

        for i in s:
            if i.isalnum()
                newStr += i.lower()
        return newStr == newStr[::-1]

        [::-1] is how you reverse a string in Python
        """

        # Solving with constant memory
        """
        This method will be using two pointers at each end of the string. This
        will use O(1) memory

        Once the pointers either meet or pass each other, that will be where we need to stop

        We will be able to use the ascii values to be able to verify if the characters are the proper values

        While a pointer is not alphanumeric, we can simply skip the value on one of the pointers
        """




