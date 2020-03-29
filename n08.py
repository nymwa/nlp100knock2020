def cipher(xs):
	xs = [chr(219 - ord(x)) if x.islower() else x for x in xs]
	return ''.join(xs)

if __name__ == '__main__':
	x = 'The quick brown fox jumps over the lazy dog. 1234567890'
	print('平文', x)
	x = cipher(x)
	print('暗号文', x)
	x = cipher(x)
	print('復号文', x)

