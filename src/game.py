from random import randrange

def main():
	MIN = 1
	MAX = 100
	NUMBER = randrange(MIN, MAX + 1)

	guesses = 9

	print(f"Guess a number from {MIN} to {MAX}.\nYou have {guesses} chances. Start now!\n")

	while guesses > 0:
		guess = input(f"Guess ({guesses}): ")
		guesses -= 1
		try:
			guess = int(guess)
			if guess == NUMBER:
				print("You won!")
				break
			if guesses == 0:
				print(f"\nYou ran out of guesses... Best luck next time.\nThe number was [{NUMBER}].")
			else:
				print("Smaller\n" if (guess > NUMBER) else "Bigger\n")
		except ValueError:
			print("Enter just the number.\n")


if __name__ == "__main__":
	main()