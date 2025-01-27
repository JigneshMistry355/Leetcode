def isVowel(character):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if character in vowel:
        return True
    return False

def extractVowels(word):
    vowels_in_word = [i for i in word if isVowel(i)][::-1]
    # vowels_in_word = []
    # for i in range(len(word)):
    #     if isVowel(word[i]):
    #         vowels_in_word.append(word[i])
    # vowels_in_word = vowels_in_word[::-1]
    return vowels_in_word

def replaceVowels(word):
    vowels_in_word = extractVowels(word)
    index = 0
    result = []

    for char in word:
        if isVowel(char):
            result.append(vowels_in_word[index])
            index += 1
        else:
            result.append(char)

    return ''.join(result)

    # for i in range(len(word)):
    #     if isVowel(word[i]):
    #         word = word.replace(word[i], vowels_in_word[0], 1)
    #         print(word)
    #         vowels_in_word.pop(0)
    #         print(vowels_in_word, "after pop")
    # return word

    ##################################################################################################################
    # Effective solution
    ##################################################################################################################

def reverseVowels2(word):
    vowels = set("aeiouAEIOU")
    word_array = list(word)

    l, r = 0, len(word)-1
    while l < r:
        if word_array[l] not in vowels:
            l += 1
        elif word_array[r] not in vowels:
            r -= 1
        else:
            word_array[l], word_array[r] =  word_array[r], word_array[l]
            l += 1
            r -= 1
    return ''.join(word_array)



if __name__ == '__main__':
    
    word = "IceCreAm"
    output = "eba"
    character = "a"
    # isVowel_result = isVowel(character, vowel)
    # vowels_in_word = extractVowels(word)
    result = reverseVowels2(word)
    print(result)