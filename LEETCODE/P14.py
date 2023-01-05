from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        answer = ''
        token = ''

        while True:
            i = 0
            answer_bool = True
            for s in range(len(strs) - 1):
                if strs[s][i] != strs[s][i + 1]:
                    answer_bool = False
                    break

            if not answer_bool:
                answer += token
                break

            else:
                token += strs[0][i]
            i += 1

        print(answer)
        return answer


a = Solution
print(a.longestCommonPrefix(["flower", "flow", "flight"]))
