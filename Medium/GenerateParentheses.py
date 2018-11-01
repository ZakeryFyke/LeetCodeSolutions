'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        par_list = []

        self.pairs(par_list, "", 0, 0, n)

        return par_list

    def pairs(self, par_list, current, open_par, close_par, max_len):

        if len(current) == max_len * 2:
            par_list.append(current)
            return

        if open_par < max_len:
            self.pairs(par_list, current + "(", open_par + 1, close_par, max_len)

        if close_par < open_par:
            self.pairs(par_list, current + ")", open_par, close_par + 1, max_len)

