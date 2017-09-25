import textract
import sys

###################################
# Extracts text from a pdf file and
# selects one sentence, which it
# then prints.
#
# Created by Fredrik Omstedt.
###################################

text = textract.process(sys.argv[1])
print(text)
