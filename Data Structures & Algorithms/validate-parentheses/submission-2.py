class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for i in range(len(s)):
            if s[i] == '{' or s[i]=='(' or s[i]=='[':
                stack.append(s[i])
            else:
                #If stack is empty here
                if not stack:
                    return False

                top = stack.pop()

                if(s[i]=='}' and top!='{') or (s[i]==']' and top!='[') or (s[i]==')' and top!='('):
                    return False
        
        if stack:
            return False
        
        return True