import textract
import sys
import os
import re
import random

###################################
# Extracts text from a pdf file and
# selects one sentence, which it
# then prints.
#
# Created by Fredrik Omstedt.
###################################

# Extracts texts from pdf files. If given a directory, the
# program will return texts from all pdf files in that directory.
def extractTexts():
    file = sys.argv[1]
    texts = []
    if os.path.isdir(file):
        for f in os.listdir(file):
            if re.match(r'^.*\.pdf$', f):
                texts.append(textract.process(file + "/" + f))
    else:
        texts.append(textract.process(file))
    return texts

# Chooses one sentence randomly from each of the given texts.
def selectSentences(texts):
    chosen_sentences = []
    for text in texts:
        sentence_structure = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)
        sentences = sentence_structure.findall(text)
        chosen_sentences.append(
            sentences[random.randint(0, len(sentences)-1)].replace("\n", " ")
        )
    return chosen_sentences

def main():
    texts = extractTexts()
    sentences = selectSentences(texts)
    for sentence in sentences:
        print(sentence)
        print("\n")

if __name__ == '__main__':
    main()
