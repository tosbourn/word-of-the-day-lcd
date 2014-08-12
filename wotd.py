#!/usr/bin/env/ python3

import os
from wordnik import *
import pifacecad

WORDNIK_URL = 'http://api.wordnik.com/v4'
WORDNIK_API_KEY = os.environ["wordnik_api_key"]

def get_word_of_the_day():
  client = swagger.ApiClient(WORDNIK_API_KEY, WORDNIK_URL)
  words_api = WordsApi.WordsApi(client)
  return words_api.getWordOfTheDay()

def display_word_of_the_day(wotd, displayer):
  displayer.output(wotd)

class LCD:
  def __init__(self):
    self.cad = pifacecad.PiFaceCAD()
    self.lcd = self.cad.lcd
    self.lcd.backlight_on()
    self.lcd.blink_off()
  def output(self, object):
    self.lcd.write(object.word + "\n")
    self.lcd.write(object.definitions[0].text)

if __name__ == "__main__":
  wotd = get_word_of_the_day()
  displayer = LCD()
  display_word_of_the_day(wotd, displayer)
