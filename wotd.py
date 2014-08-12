#!/usr/bin/env/ python

import os
from wordnik import *
import pifacecad

WORDNIK_URL = 'http://api.wordnik.com/v4'
WORDNIK_API_KEY = os.environ["wordnik_api_key"]

class LCD:
  def __init__(self):
    self.cad = pifacecad.PiFaceCAD()
    self.lcd = self.cad.lcd
    self.lcd.backlight_on()
    self.lcd.blink_off()
    self.get_word_of_the_day(self)

  def get_word_of_the_day(self):
    client = swagger.ApiClient(WORDNIK_API_KEY, WORDNIK_URL)
    words_api = WordsApi.WordsApi(client)
    self.wotd = words_api.getWordOfTheDay()

  def display_word_of_the_day(self):
    self.lcd.write(self.wotd.word + "\n")
    self.lcd.write(self.wotd.definitions[0].text)

if __name__ == "__main__":
  lcd = LCD()
  lcd.display_word_of_the_day()
