class Solution:
    def GCDofString(self, str1, str2):
        str1_len, str2_len = len(str1), len(str2)

        def valid(k):
            if str1_len % k or str2_len % k:
                print("-->",str1_len % k)
                return False
        # if str1_len < str2_len:
        #     substr = str1
        #     mystring = str2
        # substr = str2
        # mystring = str1

        # count = 0

        # for i in range(len(mystring)):
        #     if mystring[i:len(substr)]:
        for i in range(4,0,-1):
            if valid(i):
                print(i)


        

if __name__ == '__main__':
    object = Solution()
    merged_string = object.GCDofString("ab" , "ababab") 