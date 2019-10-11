def removeVowels(word):
    letters = []            # make an empty list to hold the non-vowels
    for char in word:       # for each character in the word
        if char.lower() and char.upper() not in 'aeiouAEIOU':    # if the letter is not a vowel
            letters.append(char)           # add it to the list of non-vowels
    return ''.join(letters)

result=removeVowels("SIVAkumar")
print(result)