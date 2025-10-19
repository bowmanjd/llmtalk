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
    return torch.argmax(model(vector))


# Model weights encode learned patterns: each row is logits for a token
model = torch.nn.Linear(6, 3)

with torch.no_grad():
    weights = torch.tensor(
        [
            # [5.0, 0.0, 0.0, 5.0, 0.0, 0.0],  # logits for 'a'
            # [0.0, 0.0, 5.0, 5.0, 0.0, 0.0],  # logits for 'b'
            # [5.0, 4.0, 0.0, 4.0, 5.0, 0.0],  # logits for 'c'
            [
                1000.123456,
                -500.987654,
                3.1926,
                255.9873,
                0.00000123,
                -9998.795,
            ],  # logits for 'a'
            [
                -128.555555,
                -129.444444,
                0.12345678,
                256.654321,
                -0.98765432,
                -999.999,
            ],  # logits for 'b'
            [
                4.000001,
                3.120001,
                -127.899,
                42.0001,
                128.42424242,
                -42.42424242,
            ],  # logits for 'c'
        ]
    )
    print("Original weights:\n", weights)

    min_w = weights.min()
    max_w = weights.max()
    scale = (max_w - min_w) / 255

    # Quantize
    weights_int8 = torch.clamp(((weights - min_w) / scale).round(), 0, 255).to(torch.uint8)
    print("Quantized weights (uint8):\n", weights_int8)

    # Dequantize
    dequantized_weights = weights_int8.float() * scale + min_w
    print("Dequantized weights (float):\n", dequantized_weights)

    model.weight.data = dequantized_weights


if __name__ == "__main__":
    while True:
        text = input("Enter the first two letters: ")
        vector = tokenize(text)
        prediction = infer(vector)
        print(untokenize(prediction))
