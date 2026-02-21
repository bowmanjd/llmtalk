#!/usr/bin/env python

import torch

# Our vocabulary: a=0, b=1, c=2
VOCAB = "abc"

weights = torch.tensor(
	[
		# 'a' 'b' 'c'  | 'a' 'b' 'c'  (for 1st and 2nd letter)
		[5.0, 0.0, 4.0, 5.0, 0.0, 4.0],  # predict 'a'
		[0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # predict 'b'
		[5.0, 5.0, 0.0, 4.0, 5.0, 5.0],  # predict 'c'
	]
)


def tokenize(text):
	"""Convert 'ab' -> [1,0,0, 0,1,0]"""
	indices = [VOCAB.index(c) for c in text]
	vector = torch.zeros(6)
	vector[indices[0]] = 1.0  # encode first char
	vector[3 + indices[1]] = 1.0  # encode second char (offset by 3)
	return vector


def infer(input_vector):
	"""Predict the index of the next token from an input vector."""
	# The core logic: multiply input by weights to get scores (logits)
	logits = torch.matmul(weights, input_vector)
	return torch.argmax(logits)


def decode(predicted_index):
	"""Convert a single index like 2 back to the character 'c'."""
	return VOCAB[predicted_index.item()]


if __name__ == "__main__":
	while True:
		text = input("Enter the first two letters: ")
		vector = tokenize(text)
		prediction = infer(vector)
		print(decode(prediction))
