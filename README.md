# In  short

Running this program lets you locate conceptual/non-action/non-instruction content in all your DITA content that is incorrectly tagged as `step > cmd` in tasks. You can run this on the local copy of your DITA repository and do not have to read through all the steps in your content for QA.

# Detect Non-Action content in `cmd` Elements in all your DITA content

A technical writer should write only action verb instructions in the cmd elements in the task type topics of DITA, such as: do this ... click this... type in this... The writer is not supposed to write non-action/conceptual content in the `cmd` elements, such as "this is a good idea..." or "This program is important, as it allows you to do abc.." You get the drift?

But some writers (maybe you only) along the way may have written some philisophical thoughts in the `cmd` elements, which don't belong there. Now, what are you supposed to do? Read all the task topics in the docset to find out such content? Nah.

This is a Python program that checks the contents of `cmd` elements in all your DITA files to see if they are action-oriented (imperative) or not. All you have to do is specify the folder on your machine that has all the task topics.

If any non-action content `cmd` elements are found, the program prints a report listing the filenames and contents of the non-action `cmd` elements.

## Requirements

To run this program, you will need:

* Python 3.6 or later
* The `spacy` Python library (you can install it using `pip install spacy`)
* The `en_core_web_sm` Spacy model (you can download it using `python -m spacy download en_core_web_sm`)
* The `tkinter` Python library (should be included with your Python distribution)

## Usage

To run the program:
1. Ensure python and the required libraries are installed.
2. Download the program to your machine.
3. Run the program and select the folder with your DITA content. 

The program prompts you to select a directory to process. After you select a directory and press OK, the program will walk through the directory tree, process all XML files it finds, and print a report if any non-action `cmd` elements are found.
![image](https://user-images.githubusercontent.com/67150538/221145769-dbafa6cf-7677-4377-ad08-b8cf3551db5f.png)



