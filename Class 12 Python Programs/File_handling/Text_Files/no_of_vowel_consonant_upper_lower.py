#To display the number of vowels, consonants, uppercase and lowercase letters
f = open(r'Class 12 Python Programs\File_handling\Text_Files\new.txt', 'r')

count_vowel = 0
count_consonant = 0
count_upper = 0
count_lower = 0

s = f.readline()
while s:
    for i in s:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            count_vowel += 1
        if i.islower():
            count_lower += 1
        if i.isupper():
            count_upper += 1
        else:
            if i.isalpha():
                count_consonant += 1

    s = f.readline()

f.close()
print("Vowels: ", count_vowel)
print("Consonants: ", count_consonant)
print("Uppercase Letters: ", count_upper)
print("lower case letters: ", count_lower)
# print(f"Vowels: {count_vowel} \nConsonants: {count_consonant} \nUpper case: {count_upper} \nLower case: {count_lower}")
