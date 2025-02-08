class Solution:
    def compressString(self, chars):
        result = []
        myset = {}
        count = 1
        for i in chars:
            if (i in myset.keys()):
                count += 1
                myset[i] = count
                if len(result) >= 2:
                    result = list(result)
                    result[-1] = str(count)
                    
                continue
            result += i
            result += str(count)
            myset[i] = count
            count = 1
        return result
    
if __name__ == '__main__':
    obj = Solution()
    chars = ["a","a","b","b","c","c","c"] #
    result = obj.compressString(chars)
    print(result)
