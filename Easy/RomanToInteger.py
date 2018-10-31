class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A dictionary of characters to values
        numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

        num = 0

        for i in range(0, len(s) - 1):

            # If this char's value is less than the value after it, e.g. IV, subtract its value
            if numerals[s[i]] < numerals[s[i + 1]]:
                num -= numerals[s[i]]

            # Otherwise, add it
            else:
                num += numerals[s[i]]
                
        return num + numerals[s[-1]]