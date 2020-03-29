from n05 import ngram

if __name__ == '__main__':
	str1 = 'paraparaparadise'
	str2 = 'paragraph'
	X = set(ngram(2, str1))
	Y = set(ngram(2, str2))
	print('積集合', X & Y)
	print('差集合', X - Y)
	print('se in X?', ('s', 'e') in X)
	print('se in Y?', ('s', 'e') in Y)

