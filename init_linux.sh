# Installs the necessary files to use sentence_extractor.py
# Assumes the user already has apt-get and pip.
#
# Created by Fredrik Omstedt.
sudo apt-get install python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils pstotext tesseract-ocr \
flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig
sudo pip install textract
