import sys

def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	book_path = sys.argv[1]
	text = get_book_text(book_path)
	num_words = get_num_words(text)
	ch_count_dic = get_char_count(text)
	org_result = convert_to_list(ch_count_dic)
	new_org_letters = []
	for item in org_result:
		ch = item["char"]
		if not ch.isalpha():
			continue
		new_org_letters.append(item)
	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for item in new_org_letters:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

def get_book_text(path):
	with open(path) as f:
		return f.read()

from stats import get_num_words
from stats import get_char_count
from stats import convert_to_list

main()
