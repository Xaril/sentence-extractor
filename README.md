# sentence-extractor
Sentence extractor consists of scripts helping when **singular random sentences** must be extracted from pdf files, i.e. when a course that doesn't matter (swedish: _flumkurs_) requires you to bring one sentence from every text that you should have read for a seminar.

Sentence extractor makes use of **textract**, which requires some files to work. Run the correct initializations script using `bash init_**.sh` and these will be installed.

Sentence extractor is used the following way: `python sentence_extractor.py <folder/pdf-file>`. If used on a folder, it will run on each pdf file in that folder,
and if used on a file it will run on that file only.
