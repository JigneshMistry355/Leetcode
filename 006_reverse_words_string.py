s = "the sky is  blue"

# strip each word to remove blank spaces
# split converts string to list separating by spaces
s=s.strip().split()[::-1] # reverse the list
s = " ".join(s)

# print(s)