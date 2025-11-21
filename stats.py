def get_num_words(text):
        words = text.split()
        return len(words)

def get_char_count(original_text):
	text = original_text.lower()
	dic = {}
	for ch in text:
		if ch in dic:
			dic[ch] += 1
		else:
			dic[ch] = 1
	return dic

def sort(items):
	return items["num"]

def convert_to_list(dic):
	result = []
	for key, value in dic.items():
		result.append({"char": key, "num": value})
	result.sort(reverse=True, key=sort)
	return result




