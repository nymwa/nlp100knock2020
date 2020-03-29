if __name__ == '__main__':
	xs = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
	xs = xs.split(' ')
	idx = {1, 5, 6, 7, 8, 9, 15, 16, 19}
	d1 = [(n + 1, x[:1]) for n, x in enumerate(xs) if n + 1 in idx]
	d2 = [(n + 1, x[:2]) for n, x in enumerate(xs) if n + 1 not in idx]
	dct = {x:n for n, x in d1 + d2}
	print(dct)

