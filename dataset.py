# coding: utf-8
import random, codecs
import numpy as np

def load(filepath, train_split=0.9, seed=0):
	id_bos = 0
	id_eos = 1
	vocab = {
		"<bos>": id_bos,
		"<eos>": id_eos,
	}
	dataset = []
	with codecs.open(filepath, "r", "utf-8") as f:
		for sentence in f:
			sentence = sentence.strip()
			if len(sentence) == 0:
				continue
			word_ids = [id_bos]
			words = sentence.split(" ")
			for word in words:
				if word not in vocab:
					vocab[word] = len(vocab)
				word_id = vocab[word]
				word_ids.append(word_id)
			word_ids.append(id_eos)
			dataset.append(word_ids)

	random.seed(seed)
	random.shuffle(dataset)
	split = int(len(dataset) * train_split)
	train_words = dataset[:split]
	test_words = dataset[split:]

	train_sequence = []
	for word_ids in train_words:
		for word_id in word_ids:
			train_sequence.append(word_id)

	test_sequence = []
	for word_ids in test_words:
		for word_id in word_ids:
			test_sequence.append(word_id)

	return np.asarray(train_sequence, dtype=np.int32), np.asarray(test_sequence, dtype=np.int32), vocab