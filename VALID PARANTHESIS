class Solution:
    def isValid(self, s: str) -> bool:
        k=0
        stack=[]
        for k in range(len(s)):
            if s[k]=='('or s[k]=='['or s[k]=='{':
                stack.append(s[k])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[k]==')'and top!='(':
                    return False
                if s[k]==']'and top!='[':
                    return False
                if s[k]=='}'and top!='{':
                    return False
        return len(stack)==0
        
           
        
