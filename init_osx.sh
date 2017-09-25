# Installs the necessary files to use sentence_extractor.py
# Assumes the user already has brew and pip.
#
# Created by Fredrik Omstedt.
brew install cask
brew cask install xquartz
brew install poppler antiword unrtf tesseract swig
sudo pip install textract
