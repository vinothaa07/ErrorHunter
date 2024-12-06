# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
        'A': "Vowel",
        'E': "Vowel",
        'I': "Vowel",
        'O': "Vowel",
        'U': "Vowel",
    }
    return switch.get(char)

if __name__ == "__main__":
    charInput = input("Enter a alphabet: ")
    if len(charInput) == 1 and charInput.isalpha():
        res = vowel_or_consonant(charInput)
        print(res)
    else:
        print("Please enter a single alphabet.")