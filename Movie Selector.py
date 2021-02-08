import random

def main():
	movie_list = []
	print("Please input a movie for selection or type \"select\" or \"clear\". ")
	while True:
		user_input = input()
		if user_input.lower() == "select":
			print("Tonight you will watch {}.".format(random.choice(movie_list)))
		elif user_input.lower() == "clear":
			print("List cleared.")
			movie_list = []
		else:
			print("{} has been added.".format(user_input))
			movie_list.append(user_input)

if __name__ == '__main__':
	main()