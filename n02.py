if __name__ == '__main__':
	x1 = 'パトカー'
	x2 = 'タクシー'
	x = [c for cs in zip(x1, x2) for c in cs]
	x = ''.join(x)
	print(x)

