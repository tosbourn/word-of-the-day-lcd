#!/usr/bin/env/ python3

import os
from wordnik import *

WORDNIK_URL = 'http://api.wordnik.com/v4'
WORDNIK_API_KEY = os.environ["worknik_api_key"]

def get_word_of_the_day():
  client = swagger.ApiClient(WORDNIK_API_KEY, WORDNIK_URL)
  words_api = WordsApi.WordsApi(client)
  return words_api.getWordOfTheDay()

def display_word_of_the_day(wotd):
  print wotd.word
  print wotd.definitions[0].text

if __name__ == "__main__":
  wotd = get_word_of_the_day()
  display_word_of_the_day(wotd)
