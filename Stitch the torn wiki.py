
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
