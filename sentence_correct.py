def create_bigrams(word):
    return [word[i] + word[i+1] for i in range(len(word)-1)]

def get_similarity_ratio(word1, word2):
    word1, word2 = word1.lower(), word2.lower()
    common = []
    bigram1, bigram2 = create_bigrams(word1), create_bigrams(word2)
    
    for i in range(len(bigram1)):
        try:
            cmn_elt = bigram2.index(bigram1[i])
            common.append(bigram1[i])
        except ValueError:
            continue
    
    return len(common) / max(len(bigram1), len(bigram2))

def AutoCorrect(word, database={'etc'}, sim_threshold=0.5):
    max_sim = 0.0
    most_sim_word = word

    for data_word in database:
        cur_sim = get_similarity_ratio(word, data_word)
        if cur_sim > max_sim:
            max_sim = cur_sim
            most_sim_word = data_word

    return most_sim_word if max_sim > sim_threshold else word

# Example usage:
input_word = input("Enter a word: ")
corrected_word = AutoCorrect(input_word)
print("Corrected word:", corrected_word)

# Save the corrected word in a text file
output_file = "corrected_word.txt"
with open(output_file, 'w') as file:
    file.write(corrected_word)
print("Corrected word saved in", output_file)

      
