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
    self.get_word_of_the_day()

  def get_word_of_the_day(self):
    client = swagger.ApiClient(WORDNIK_API_KEY, WORDNIK_URL)
    words_api = WordsApi.WordsApi(client)
    self.wotd = words_api.getWordOfTheDay()

  def display_word_of_the_day(self):
    output = self.wotd.word + " - " + self.wotd.definitions[0].text
    sentence_length = len(output)
    overflow = sentence_length - 16
    self.lcd.write(output)

    while overflow > 0:
      time.sleep(0.5)
      self.lcd.move_right()
      overflow -= 1

    time.sleep(5)

    self.exit_gracefully()

  def exit_gracefully(self):
    self.lcd.clear()
    self.lcd.cursor_off()
    self.lcd.display_off()
    self.lcd.backlight_off()
    os._exit

if __name__ == "__main__":
  lcd = LCD()
  lcd.display_word_of_the_day()
