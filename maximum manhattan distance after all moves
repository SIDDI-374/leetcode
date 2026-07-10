class Solution:
    def maxDistance(self, moves: str) -> int:
        U = D = L = R = underscore = 0
        for c in moves:
            if c == 'U':
                U += 1
            elif c == 'D':
                D += 1
            elif c == 'L':
                L += 1
            elif c == 'R':
                R += 1
            else:
                underscore += 1
                    
        x = R - L
        y = U - D 
        answer = abs(x) + abs(y) + underscore
            
        return answer
