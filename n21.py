import re

def load_England():
	with open('data/イギリス.txt') as f:
		text = f.read()
	return text

if __name__ == '__main__':
	text = load_England()
	lst = [line for line in text.splitlines() if re.search(r'\[\[Category:[^\]]+\]\]', line)]
	for line in lst:
		print(line)

