import crypt

while True:
	text = input("Type text: ")
	if text == 'q':
		break
	print(crypt.keywordEncrypt(text, "python"))