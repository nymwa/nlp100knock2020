import gzip
import json

if __name__ == '__main__':
	with gzip.open('data/jawiki-country.json.gz', 'rb') as f:
		for line in f:
			line = line.strip()
			data = json.loads(line)
			if data['title'] == 'イギリス':
				text = data['text']

	with open('data/イギリス.txt', 'w') as f:
		f.write(text)

