import re
from n21 import load_England

if __name__ == '__main__':
	text = load_England()
	lst = re.findall(r'(?<=Category:)[^\]]+', text)
	for line in lst:
		print(line)

