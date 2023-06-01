from textblob import Textblob
import subprocess

file1=open("input.txt", "r+")
a=file1.read()

print("You: ",str(a))

b=TextBlob(a)

file1.close()

d=open("input.txt", "w")
d.write(str(b.correct()))
d.close()

def run_another_file():
    file_path = "converter.py"  # Replace with the actual path of the file you want to run

    # Launch a new process to execute the file
    subprocess.Popen(["python", file_path])

# Main program
if __name__ == "__main__":
    run_another_file()
