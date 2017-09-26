import textract
import sys
import os
import re
import random

###################################
# Extracts text from one or more
# pdf file and selects one sentence
# from each, which the program then
# prints.
#
# Created by Fredrik Omstedt.
###################################

# Extracts texts from pdf files. If given a directory, the
# program will return texts from all pdf files in that directory.
def extractTexts():
    file = sys.argv[1]
    file_names = []
    texts = []
    if os.path.isdir(file):
        for f in os.listdir(file):
            if re.match(r'^.*\.pdf$', f):
                file_names.append(f)
                texts.append(textract.process(file + "/" + f))
    else:
        texts.append(textract.process(file))
    return file_names, texts

# Chooses one sentence randomly from each of the given texts.
def selectSentences(texts):
    chosen_sentences = []
    for text in texts:
        sentence_structure = re.compile(r'([A-Z\xc4\xc5\xd6][^\.!?]*[\.!?])', re.M)
        sentences = sentence_structure.findall(text)
        chosen_sentences.append(
            sentences[random.randint(0, len(sentences)-1)].replace("\n", " ")
        )
    return chosen_sentences

# Extracts texts from one or more pdf files, chooses one random
# sentence from each of the texts, and prints it.
def main():
    file_names, texts = extractTexts()
    sentences = selectSentences(texts)
    for i in range(0, len(sentences)):
        print(file_names[i] + " - " + sentences[i])
        print("\n")

if __name__ == '__main__':
    main()
