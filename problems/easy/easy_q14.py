# Vowel or Consonant: Accept a character and use a switch case to determine if it is a vowel or a consonant.
def vowel_or_consonant(char):
    char=char.lower()
    switch = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
    }
 
    return switch.get(char, "constant")   
if __name__ == "__main__":
    character_input = input("Enter a character: ").strip()
    if len(character_input) == 1 and character_input.isalpha():
        res = vowel_or_consonant(character_input)
        print(res)
    else:
        print("Invalid")

    
 
 
    return switch.get(char,"Consonant")   
if __name__ == "__main__":
    characterInput  = input("Enter the character : ")
 
 
    return switch.get(char, "consonants")   
if __name__ == "__main__":
    characterInput  = (input("Enter the charactrer : "))
 
    res = vowel_or_consonant(characterInput)
    print(res)
 
 
 