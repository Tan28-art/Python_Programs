'''String functions assuming s is defined as a string

    1.) len(s) : Returns length of the string

    2.) s.find('c') : Finds and returns index of given character
        # If it cannot find the character it returns -1

    3.) s.capitalize() : capitalizes first letter of the string and the rest of the letters will be lower case

    4.) s.count('s') : Finds out how many times given letter comes in the string

    5.) s.islower() : Checks if the string is completely in lower case [returns True if it is]

    6.) s.isupper() : Checks if the string is completely in UPPER case [returns True if it is]

    7.) s.isdigit() : Checks if the string is a number [returns True if it is]

    8.) s.isalpha() : Checks if the string consists of only alphabets [returns True if it is]

    9.) s.lower() : converts the string to lower case

    10.) s.upper() : converts the string to UPPER case

    11.) s.isalnum() : Checks if the string has only alphabets and numbers [returns True if it is]

    12.) ord() : This function takes a single character and returns the corresponding ordinal value
        # Eg ord('z') will give 122

    13.) chr() : This function takes the ordinal value in integer form and returns the character corresponding to that ordinal value
        # Eg chr(65) will give 'A' 

    14.) join() : This function returns a string in which string 2 is merged with string 1
        # Eg '*'.join("Hello") will give H*e*l*l*o

    15.) s.swapcase() : This function interchanges lower case chars to upper case and upper case chars to lower case
        # Eg "HeLlo".swapcase() will give helLO

    16.) s.title() : This returns a string with first letter of every word in upper case and the rest in lower case
        # Eg "hello, how are you?".title() will give Hello, How Are You?

    17.) s.startswith() : This function returns True if the given string starts with the supplied substring, otherwise returns False

    18.) s.endswith() : This function returns True if the given string ends with the supplied substring, otherwise returns False

    19.) s.replace() : This function replaces all the occurrences of the old string with the new string 

    20.) s.strip() : This function returns the string after removing all the leading and the trailing spaces 
        # Eg "  Hello world  ".strip() will give "Hello world"

    21.) s.lstrip() : This function returns the string after removing the leading spaces

    22.) s.rstrip() : This function returns the string after removing the trailing spaces
'''      
l = []
l.sort()