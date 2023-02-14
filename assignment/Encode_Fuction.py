import string


def encoding_application(word: str):
    key = 6
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase

    lower_letters_code = lower_letters[key:] + lower_letters[:key]
    upper_letters_code = upper_letters[key:] + upper_letters[:key]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters_code

    # print(letters)
    # print(letters_code)

    encoded_word = word.translate(str.maketrans(letters, letters_code))
    print(encoded_word)


def decoding_application(word: str):
    key = 6
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase

    lower_letters_code = lower_letters[key:] + lower_letters[:key]
    upper_letters_code = upper_letters[key:] + upper_letters[:key]

    letters = lower_letters + upper_letters
    letters_code = lower_letters_code + upper_letters_code

    # print(letters)
    # print(letters_code)

    decoded_word = word.translate(str.maketrans(letters_code, letters))
    print(decoded_word)


def brute_force_application(word: str):
    lower_letters = string.ascii_lowercase
    upper_letters = string.ascii_uppercase

    for i in range(1, 27):
        lower_letters_code = lower_letters[i:] + lower_letters[:i]
        upper_letters_code = upper_letters[i:] + upper_letters[:i]

        letters = lower_letters + upper_letters
        letters_code = lower_letters_code + upper_letters_code

        print(word.translate(str.maketrans(letters_code, letters)))


word = input("What would you like to encode: ")
encoding_application(word)
word = input("Enter encoded word: ")
decoding_application(word)
word = input("Enter encoded word again: ")
brute_force_application(word)
