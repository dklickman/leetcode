class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        last = 0
        total = 0
        for num in list(s):
            current = roman_dict.get(num)
            if current > last:
                total -= last
                total += (current - last)
            else:
                total += current
            last = current

        return total 
print(Solution().romanToInt('MCMXCVI'))
#print(Solution().romanToInt('MCCCCCCCCCXXXXXXXXXVI'))
print(Solution().romanToInt('XXVII'))
print(Solution().romanToInt('LXI'))
