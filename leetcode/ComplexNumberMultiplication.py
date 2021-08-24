class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        sp_num1 = num1.split('+') 
        sp_num2 = num2.split('+')
        
        real1 = int(sp_num1[0])
        real2 = int(sp_num2[0])
        
        if sp_num1[1][0] == '-': im1 = (-1)* int(sp_num1[1][1:-1])
        else: im1 = int(sp_num1[1][0:-1])
            
        if sp_num2[1][0] == '-': im2 = (-1)* int(sp_num2[1][1:-1])
        else: im2 = int(sp_num2[1][0:-1])
        
        real_total = real1*real2 + im1*im2*(-1) 
        imaginary_total = real1*im2 + real2*im1
        
        return f'{real_total}+{imaginary_total}i'