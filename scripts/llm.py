#!/usr/bin/env python

import torch


def tokenize(text):
    """Split into tokens and represent as vector"""
    # a = 0, b = 1, c = 2
    tokens = ["abc".index(char) for char in text]
    vector = torch.zeros(6)
    # One-hot encode: first 3 dims for token 0, last 3 dims for token 1
    vector[tokens[0]] = 1.0
    vector[3 + tokens[1]] = 1.0
    return vector


def untokenize(vector):
    """Convert vector back into text"""
    return "".join("abc"[i] for i in vector.flatten())


def infer(vector):
    return torch.argmax(torch.matmul(weights, vector))


with torch.no_grad():
    weights = torch.tensor(
        [
            [5.0, 0.0, 4.0, 5.0, 0.0, 4.0],  # logits for 'a'
            [0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # logits for 'b'
            [5.0, 4.0, 0.0, 4.0, 5.0, 0.0],  # logits for 'c'
        ]
    )


if __name__ == "__main__":
    while True:
        text = input("Enter the first two letters: ")
        vector = tokenize(text)
        prediction = infer(vector)
        print(untokenize(prediction))
