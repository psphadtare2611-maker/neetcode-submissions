class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        for ch in s:
            if ch == "(" or ch =="{" or ch == "[":
                result.append(ch)
            else:
                if not result:
                    return False

                top = result.pop()

                if ch == ")" and top != "(":
                    return False
                if ch == "}" and top != "{":
                    return False
                if ch == "]" and top != "[":
                    return False

        return len(result) == 0