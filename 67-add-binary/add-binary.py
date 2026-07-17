class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0  
        for i in range(max(len(a), len(b))):
            if i < len(a):
                digit_a = int(a[len(a) - 1 - i])
            else:
                digit_a = 0

            if i < len(b):
                digit_b = int(b[len(b) - 1 - i])
            else:
                digit_b = 0

            total = digit_a + digit_b + carry     
            carry = total// 2
            result.append(total % 2)

        if carry:
            result.append(carry)

        return ''.join(str(digit) for digit in result[::-1])
           

    
        
        