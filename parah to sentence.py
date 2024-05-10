import re

def sentence_segmentation(text):
    sentences = re.split(r'(?<=[.!?])', text)
    cleaned_sentences = []
    inside_quote = False
    current_sentence = ''
    for sentence in sentences:
        if inside_quote:
            current_sentence += sentence.strip()
            if sentence.strip().endswith('"'):
                cleaned_sentences.append(current_sentence)
                current_sentence = ''
                inside_quote = False
        else:
            if sentence.strip().startswith('"'):
                current_sentence += sentence.strip()
                if sentence.strip().endswith('"'):
                    cleaned_sentences.append(current_sentence)
                    current_sentence = ''
                else:
                    inside_quote = True
            else:
                cleaned_sentences.append(sentence.strip())
    return cleaned_sentences

input_text = input()

sentences = sentence_segmentation(input_text)

for sentence in sentences:
    print(sentence)
