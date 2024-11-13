class Solution:
    def isValid(self, s: str) -> bool:
        # Número de brackets de um mesmo tipo tem que ser par para ser válido
        parentheses = []
        curly_brackets = []
        square_brackets = []

        opening = []
        closing = []

        mapping = {
            ")" : "(",
            "}": "{",
            "]": "["
        }

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
                closing.append(char)
                is_closing = True

            if is_closing:
                if len(opening) >= 1:
                    if opening[-1] != mapping[char]:
                        is_valid = False
                        break
                    else:
                        opening.pop(-1)
                        closing.pop(-1)

        if len(opening) == 0 and len(closing) == 0:
            is_valid = True
        
        return is_valid
