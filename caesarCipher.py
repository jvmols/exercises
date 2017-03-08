

# the string to be encrypted/decrypted
message = raw_input("Give a string to be encrypted/decrypted:\n")

# encryption/decryption key
while True:
	try:
		key = int(raw_input("Give encryption/decryption key:\n"))
	except ValueError:
		print("Schhit input!")
		continue
	else:
		break

# Choose encryption or decryption
mode = None
modeList = ['e', 'd']

while not mode:
	user_input = raw_input("Choose 'e' for encryption or 'd' for decryption':\n")
	if user_input in modeList:
		mode  = user_input

# every possible symbol that can be encrypted/decrypted
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# stores the encrypted/decrypted form of the message
translated = ''

# capitalize the message string
message = message.upper()


# run the encryption/decryption code on each symbol in the message string
for symbol in message:
	if symbol in LETTERS:
		# get the encrypted/decrypted code on each symbol in the message string
		num = LETTERS.find(symbol) # get the number of the symbol
		if mode == 'e':
			num = num + key
		elif mode == 'd':
			num = num - key

		# handle the mod(LETTERS) wrap-around if num is larger than len(LETTERS)	
		if num >= len(LETTERS):
			num = num - len(LETTERS)
		# OR num is less than 0
		elif num < 0:
			num = num + len(LETTERS)

		# add encrypted/decrypted number's symbol at the end of translated
		translated = translated + LETTERS[num]

	else:
		# just add the symbol without encryption
		translated = translated + symbol

# print
print(translated)
