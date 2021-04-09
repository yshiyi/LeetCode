class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sa, sb, s_sum = [], [], [];
        for char in a:
            sa.append(ord(char)-48)
        for char in b:
            sb.append(ord(char)-48)
        carry = 0
        while len(sa)>0 and len(sb)>0:
            sum = sa[-1] + sb[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sa.pop()
            sb.pop()
        while len(sa)>0:
            sum = sa[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sa.pop()
        while len(sb)>0:
            sum = sb[-1] + carry
            if sum < 2:
                s_sum.append(sum)
                carry = 0
            elif sum == 2:
                s_sum.append(0)
                carry = 1
            else:
                s_sum.append(1)
                carry = 1
            sb.pop()
        if carry == 1:
            s_sum.append(1)
        
        res = ""
        while len(s_sum) > 0:
            res += str(s_sum[-1])
            s_sum.pop()
        return res
