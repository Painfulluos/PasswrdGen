import random


chrs = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def gen(number, length):
	for num in range(number):
		password = ''
		for i in range(length):
			password += random.choice(chrs)
		print(f'{num}: "{password}"')


def main():
	length, number_pwrds = 0, 0
	while length < 1 and number_pwrds < 1:
		try:
			number_pwrds = int(input('Enter the number of passwords: '))
			length = int(input("Enter number of characters in the passwords: "))
		except:
			print("Input Error.")
	gen(number_pwrds, length)

if __name__ == "__main__":
	main()