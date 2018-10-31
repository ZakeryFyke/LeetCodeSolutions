class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        open_brackets = ['{', '(', '[']
        close_brackets = ['}', ')', ']']

        bracket_list = []

        for bracket in s:
            if bracket in open_brackets:
                bracket_list.append(bracket)

            else:
                if len(bracket_list) == 0:
                    return False

                # Get the matching open bracket for this bracket
                open_bracket = open_brackets[close_brackets.index(bracket)]

                if bracket_list[-1] != open_bracket:
                    return False
                else:
                    bracket_list.pop(-1)

        if len(bracket_list) == 0:
            return True
        else:
            return False