# -*- coding: utf-8 -*-
"""AssignmentWeek2NLTK-.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oxL6cKrBzwLzOMNf5O7Fl651Ndm1wfa_
"""

import spacy

nlp = spacy.blank("en")

doc = nlp("Lorem Ipsum is simply dummy text of the printing and typesetting industry.")

for token in doc:
  print(doc)

word = doc[0]

type(nlp)

dir(nlp)

word.is_alpha

word.like_num

word.text

for token in doc:
  print(token, "=>", "index: ", token.i, "is_alpha: ", token.is_alpha)

tamil = spacy.blank("ta")

tdoc = tamil("தமிழ் மொழி தொன்மையான மற்றும் செழுமையான ஒரு மொழியாகும், இது தென்னிந்தியாவில் முக்கியமாகவும், இலங்கையில் வாழும் தமிழ் மக்களின் தாய்மொழியாகவும் பயன்படுத்தப்படுகிறது")

tdoc

for token in tdoc:
  print(token)

