class Solution:
    def GCDofString(self, str1, str2):
        str1_len, str2_len = len(str1), len(str2)

        def valid(k):

            # if any one generates a remainder, then the length of string is not divisible
            # hence return false
            if (str1_len % k) or (str2_len % k):
                return False
            
            # Now we know, both strings are divisible

            # get the ratio of string
            
            n1 = str1_len // k # --> 2
            n2 = str2_len // k # --> 1
            base = str1[:k]

            # if both conditions are true, return true
            return str1 == n1 * base and str2 == n2 * base
       
        # start with length of smaller string in reverse order until 
        for i in range(min(str1_len, str2_len),0,-1):

            if valid(i):
                return str1[:i]
        return ""


        

if __name__ == '__main__':
    object = Solution()
    merged_string = object.GCDofString("ab" , "ababab") 
    print(merged_string)