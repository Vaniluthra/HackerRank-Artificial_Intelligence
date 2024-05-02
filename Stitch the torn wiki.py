''' 
Problem:
Text blocks which are approximately 500 to 1000 words in length are picked up from N different Wikipedia articles. Every block of text has been picked up from a unique Wikipedia article, about a well known person or place.

Each of these text blocks is split into two parts of roughly equal length.

The first (starting) part obtained after splitting is placed in Set A which will hold all the starting blocks. The second part of the block, is placed in Set B which will contain the second part for all the text fragments which we selected. Both the Sets A and B are shuffled up, and the ordering of elements is lost.

Your task is to identify, for each text fragment (a) in Set A, which is the correct, corresponding text fragment (b) in Set B, such that both a and b were in the same text block initially.
''' 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def calculate_similarity(set_a, set_b):
    all_text = set_a + set_b

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_text)

    cosine_sim = cosine_similarity(tfidf_matrix[:len(set_a)], tfidf_matrix[len(set_a):])

    most_similar_indices = cosine_sim.argmax(axis=1)

    return most_similar_indices

N = int(input())
fragments_a = [input() for _ in range(N)]
separator = input()  # Read separator
fragments_b = [input() for _ in range(N)]

result_indices = calculate_similarity(fragments_a, fragments_b)
for index in result_indices:
    print(index + 1)
