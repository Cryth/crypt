def words(chars, length, filename, can_repeat=True):
    chars = set(chars)
    print(chars)
    print(f"Number of words: {num_of_words(chars, length, can_repeat)}")
    print(f"Calculated size: {size(chars, length, can_repeat)} B")

    if input("Would you like to continue?[Y/n]") != "Y":
        print("Cancelled..")
        return None

    if can_repeat:
    	create_file(filename, product(chars, length))
    else:
    	create_file(filename, permutations(chars, length))
    print(f"The file {filename} was created.")

def create_file(filename, generator):
	with open(filename, 'w') as f:
		for i in generator:
			print(i)
			f.write(i + "\n")

def permutations(chars, length):
	from itertools import permutations

	for i in permutations(chars, length):
		yield ''.join(i)

def product(chars, length):
	from itertools import product

	for i in product(chars, repeat=length):
		yield ''.join(i)


def num_of_words(chars, length, can_repeat=True):
    chars_length = len(chars)
    if can_repeat:
        return chars_length**length
    else:
        return factorial(chars_length) // factorial(chars_length - length) if chars_length >= length else 0


def size(chars, length, can_repeat=True):
    return num_of_words(chars, length, can_repeat) * (2 + length)


def factorial(n):
    return 1 if n <= 0 else n * factorial(n-1)


if __name__ == '__main__':
    displayed_text = "chars len filename can_repeat[0/1]: "
    input_received = input(displayed_text).split()

    if len(input_received) == len(displayed_text):
        can_repeat = True if input_received[-1] == '1' else False
        words(input_received[0], int(input_received[1]), input_received[2], can_repeat)
    else:
        words(input_received[0], int(input_received[1]), input_received[2])
