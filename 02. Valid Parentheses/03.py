class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize stack
        stack = []
        
        # Define mapping of closing to opening brackets
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in string
        for char in s:
            # If it's a closing bracket
            if char in brackets:
                # Check if stack is empty or if top element doesn't match
                if not stack or stack[-1] != brackets[char]:
                    return False
                # If matches, pop the opening bracket
                stack.pop()
            # If it's an opening bracket
            else:
                stack.append(char)
        
        # String is valid if stack is empty (all brackets were matched)
        return len(stack) == 0