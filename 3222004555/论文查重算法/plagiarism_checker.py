import sys
from collections import Counter
import math


def get_cosine_similarity(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = text.split()
    return Counter(words)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') as f:
        text1 = f.read()

    with open(sys.argv[2], 'r') as f:
        text2 = f.read()

    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)

    cosine_sim = get_cosine_similarity(vector1, vector2)

    with open(sys.argv[3], 'w') as f:
        f.write("{:.2f}".format(cosine_sim))

