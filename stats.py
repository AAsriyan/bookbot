def get_word_count(text: str) -> int:
	return len(text.split())

def get_char_count(text: str) -> dict[str, int]:
	char_count_map = {}

	for char in text:
		lowerChar = char.lower()
		char_count_map[lowerChar] = char_count_map.get(lowerChar, 0) + 1
	
	return char_count_map

def get_char_count_sorted(char_count_map: dict[str, int]) -> list[dict[str, int]]:
	char_list = []
	for char, count in char_count_map.items():
		char_list.append({char: count})

	char_list_sorted = sorted(char_list, key=lambda item: list(item.values())[0], reverse=True)
	return char_list_sorted
