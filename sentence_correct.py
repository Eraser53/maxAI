import difflib

def create_bigrams(sentence):
    return [sentence[i:i+2] for i in range(len(sentence)-1)]

def get_sentence_similarity(sentence1, sentence2):
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()
    bigrams1 = create_bigrams(sentence1)
    bigrams2 = create_bigrams(sentence2)
    matcher = difflib.SequenceMatcher(None, bigrams1, bigrams2)
    return matcher.ratio()

def auto_correct(sentence, database={'etc'}, sim_threshold=0.5):
    max_sim = 0.0
    most_sim_sentence = sentence

    for data_sentence in database:
        cur_sim = get_sentence_similarity(sentence, data_sentence)
        if cur_sim > max_sim:
            max_sim = cur_sim
            most_sim_sentence = data_sentence

    return most_sim_sentence if max_sim > sim_threshold else sentence

# Example usage:
input_sentence = input("Enter a sentence: ")
corrected_sentence = auto_correct(input_sentence)
print("Corrected sentence:", corrected_sentence)

# Save the corrected sentence in a text file
output_file = "corrected_sentence.txt"
with open(output_file, 'w') as file:
    file.write(corrected_sentence)
print("Corrected sentence saved in", output_file)

