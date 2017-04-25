# coding: utf-8
import argparse, codecs, sys, os, re
import MeCab

class stdout:
	BOLD = "\033[1m"
	END = "\033[0m"
	CLEAR = "\033[2K"

def main(args):
	files = []
	assert os.path.exists(args.input_dir)
	fs = os.listdir(args.input_dir)
	for filename in fs:
		files.append(args.input_dir + "/" + filename)

	for filepath in files:
		if filepath.endswith(".txt") == False:
			continue
		dataset = []
		sys.stdout.write(stdout.CLEAR)
		sys.stdout.write("\rprocessing {}".format(filepath))
		sys.stdout.flush()
		with codecs.open(filepath, "r", "utf-8") as f:
			for sentence in f:
				sentence = sentence.strip()
				if len(sentence) == 0:
					continue
				dataset.append(sentence)

	with codecs.open(args.output_filename, "w", "utf-8") as f:
		for sentence in dataset:
			f.write(sentence)
			if i < len(dataset) - 1:
				f.write("\n")

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", "--input-dir", type=str, default=None)
	parser.add_argument("-o", "--output-filename", type=str, default=None)
	args = parser.parse_args()
	main(args)