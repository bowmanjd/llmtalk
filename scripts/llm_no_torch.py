#!/usr/bin/env python

# Our vocabulary: a=0, b=1, c=2
VOCAB = "abc"

# The model's "brain" is just a list of lists.
# These numbers encode our rules.
weights = [
	#a  b  c  a  b  c    (for 1st and 2nd letter)
	[5, 0, 4, 5, 0, 4],  # predict 'a'
	[0, 0, 5, 5, 0, 0],  # predict 'b'
	[5, 5, 0, 4, 5, 5],  # predict 'c'
]


def tokenize(text):
	"""Convert 'ab' -> [1, 0, 0, 0, 1, 0]"""
	indices = [VOCAB.index(c) for c in text]
	vector = [0.0] * 6
	vector[indices[0]] = 1.0  # One-hot encode first char
	vector[3 + indices[1]] = 1.0  # One-hot encode second char (offset by 3)
	return vector


def infer(input_vector):
	"""Predict the index of the next token from an input vector."""
	# The core logic: matrix-vector multiplication, done manually.
	# This calculates the dot product of the input_vector with each row in the weights matrix.
	logits = [sum(w * v for w, v in zip(row, input_vector)) for row in weights]

	# Find the index of the highest score (logit). This is argmax.
	return logits.index(max(logits))


def decode(predicted_index):
	"""Convert a single index like 2 back to the character 'c'."""
	return VOCAB[predicted_index]


if __name__ == "__main__":
	while True:
		text = input("Enter the first two letters: ")
		vector = tokenize(text)
		prediction = infer(vector)
		print(decode(prediction))
