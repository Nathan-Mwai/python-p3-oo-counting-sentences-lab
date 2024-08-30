#!/usr/bin/env python3
import re
class MyString:
  def __init__(self,value = ''):
    self._value = ''
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self,value):
    if not isinstance(value, str):
      print("The value must be a string.")
    self._value = value
    
  def is_sentence(self):
    # Do not forget that return prints true ot false
    return self.value.endswith('.')
  def is_question(self):
    return self.value.endswith('?')
  def is_exclamation(self):
    return self.value.endswith('!')
  
  def count_sentences(self):
    #I used re method  so that I can stop repeating myself and prevent myself from replacing staff
    punctuation = re.split(r"[.!?]",self.value)
    not_count_space = [sentence for sentence in punctuation if len(sentence) > 0 and not sentence.isspace()]
    return len((not_count_space))
