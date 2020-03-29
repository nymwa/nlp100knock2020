def ngram(n, lst):
	return list(zip(*[lst[i:] for i in range(n)]))

if __name__ == '__main__':
	xs = 'I am an NLPer'
	char_bi_gram = ngram(2, xs)

	ys = xs.split(' ')
	word_bi_gram = ngram(2, ys)

	print('文字bi-gram', char_bi_gram)
	print('単語bi-gram', word_bi_gram)

