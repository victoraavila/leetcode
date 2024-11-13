class Solution:
    def isValid(self, s: str) -> bool:
        # Número de brackets de um mesmo tipo tem que ser par para ser válido
        parentheses = []
        curly_brackets = []
        square_brackets = []

        opening = []

        mapping = {
            ")" : "(",
            "}": "{",
            "]": "["
        }

        if len(s) % 2 != 0:
            return False

        is_valid = False

        for char in s:
            is_closing = False

            if char == "(" or char == ")":
                parentheses.append(char)
            elif char == "{" or char == "}":
                curly_brackets.append(char)
            elif char == "[" or char == "]":
                square_brackets.append(char)

            if char == "(" or char == "{" or char == "[":
                opening.append(char)

            if char == ")" or char == "}" or char == "]":
                is_closing = True

            if is_closing:
                if len(opening) >= 1:
                    if opening[-1] != mapping[char]:
                        is_valid = False
                        break
                    else:
                        opening.pop(-1)
                else:
                    return False

        if len(opening) == 0:
            is_valid = True
        
        return is_valid