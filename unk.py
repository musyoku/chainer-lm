# coding: utf-8
import argparse, codecs, sys, os, re
import MeCab

class stdout:
	BOLD = "\033[1m"
	END = "\033[0m"
	CLEAR = "\033[2K"

def main(args):
	assert args.input_filename.endswith(".txt")
	assert args.input_filename != args.output_filename
	freq = {}
	dataset = []
	with codecs.open(args.input_filename, "r", "utf-8") as f:
		# tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
		tagger = MeCab.Tagger("-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
		for i, sentence in enumerate(f):
			sentence = sentence.strip()
			words = sentence.split(" ")
			for word in words:
				if word not in freq:
					freq[word] = 0
				freq[word] += 1
			dataset.append(words)

	with codecs.open(args.output_filename, "w", "utf-8") as f:
		for words in dataset:
			for i, word in enumerate(words):
				if freq[word] <= args.count:
					words[i] = "<unk>"
			sentence = " ".join(words)
			f.write(sentence)
			if i < len(dataset) - 1:
				f.write("\n")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input-filename", type=str, default=None)
	parser.add_argument("-o", "--output-filename", type=str, default=None)
	parser.add_argument("-c", "--count", type=int, default=1)
	args = parser.parse_args()
	main(args)