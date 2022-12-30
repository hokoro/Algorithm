class Solution:
    def romanToInt(self, s: str):
        s_list = list(s)
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        last_char = ''
        answer = 0
        for s_char in s_list:
            if last_char == 'I' and (s_char == 'V' or s_char == 'X'):
                answer -= 2
            elif last_char == 'X' and (s_char == 'L' or s_char == 'C'):
                answer -= 20
            elif last_char == 'C' and (s_char == 'D' or s_char == 'M'):
                answer -= 200
            answer += roman_dict[s_char]
            last_char = s_char

        return answer

s = input()

p = Solution.romanToInt(s)
