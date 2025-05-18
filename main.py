from sys import argv
from stats import get_word_count, get_char_count, get_char_count_sorted

def get_book_text(path_to_file: str) -> str:
	with open(path_to_file, "r") as f:
		return f.read()

def main():
	if len(argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		exit(1)

	print("============ BOOKBOT ============")

	# Get the book text
	book_path = argv[1]
	print(f"Analyzing book found at {book_path}...")
	book_text = get_book_text(book_path)

	# Get the word count
	print("----------- Word Count ----------")
	word_count = get_word_count(book_text)
	print(f"Found {word_count} total words")

	# Get the character count
	print("--------- Character Count -------")
	char_count_map = get_char_count(book_text)
	char_count_sorted = get_char_count_sorted(char_count_map)

	for char_dict in char_count_sorted:
		for key, value in char_dict.items():
			if key.isalpha():
				print(f"{key}: {value}")

	print("============= END ===============")

if __name__ == "__main__":
	main()
