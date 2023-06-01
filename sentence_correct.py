import os

def correct_sentences(input_file, output_file):
    """
    This function reads sentences from an input file, corrects them, and saves the corrected sentences to an output file.
    
    Parameters:
    input_file (str): The name of the input file
    output_file (str): The name of the output file
    
    Returns:
    None
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError("Input file not found")
        
        # Open input and output files
        with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
            # Read each line from input file
            for line in f_in:
                # Split line into sentences
                sentences = line.strip().split(". ")
                
                # Correct each sentence and write to output file
                for sentence in sentences:
                    corrected_sentence = sentence.capitalize() + "."
                    f_out.write(corrected_sentence + "\n")
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
