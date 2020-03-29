import random as rd

def swap(x):
	if len(x) <= 4:
		return x
	else:
		pos = rd.randrange(1, len(x) - 2) 
		return x[:pos] + x[pos+1] + x[pos] + x[pos+2:]


if __name__ == '__main__':
	x = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
	x = x.split(' ')
	x = [swap(w) for w in x]
	x = ' '.join(x)
	print(x)

