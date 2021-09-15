import string

my_text = input('enter something: ')
shift = 3

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted)
after_translatation = str.translate(my_text, table)

print(after_translatation)
