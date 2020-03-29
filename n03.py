import re

if __name__ == '__main__':
	x = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
	x = re.sub(r'[^\w\s]', '', x)
	x = x.split(' ')
	x = [len(w) for w in x]
	print(x)

