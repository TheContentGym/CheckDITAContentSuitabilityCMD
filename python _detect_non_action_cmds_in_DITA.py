import os
import spacy
import xml.etree.ElementTree as ET
from tkinter import filedialog
from tkinter import Tk

# Load the English language model in Spacy
nlp = spacy.load("en_core_web_sm")

# Function to check if text is imperative
def is_imperative(text):
    doc = nlp(text)
    if len(doc) > 0 and doc[0].pos_ == "VERB" and doc[0].tag_ == "VB":
        return True
    else:
        return False

# Walk through a directory tree and process XML files
def process_dir(dirname, non_action_cmds):
    for root, dirs, files in os.walk(dirname):
        for file in files:
            if file.endswith(".xml"):
                filename = os.path.join(root, file)
                try:
                    tree = ET.parse(filename)
                    for elem in tree.iter("cmd"):
                        if elem.text and not is_imperative(elem.text):
                            non_action_cmds.append((filename, elem.text))
                except ET.ParseError as e:
                    print(f"Error parsing {filename}: {e}")
    return non_action_cmds

# Main program
if __name__ == "__main__":
    # Prompt the user to select a directory
    root = Tk()
    root.withdraw()
    dirname = filedialog.askdirectory(title="Select directory to process")

    if not dirname:
        print("No directory selected.")
    else:
        non_action_cmds = process_dir(dirname, [])
        if len(non_action_cmds) > 0:
            report_title = "cmd elements that contain non action content"
            print(report_title)
            print("-" * len(report_title))
            for filename, text in non_action_cmds:
                print(f"{filename}: {text}")
        else:
            print("All cmd elements are action-oriented.")
