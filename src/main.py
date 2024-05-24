import flet as ft
from widgets.word_widget import *
from widgets.keyboard_widget import *
from helpers.size_aware import *
from functions import *


class MainApp(ft.UserControl):
  def __init__(self):
    super().__init__()
    self.word_screen = WordScreen()
    self.keyboard = KeyBoard(key_handler=self.handle_keypress)
    self.word = getRandomWord()

  # def handle_resize(self, e: ft.canvas.CanvasResizeEvent):
  #   # instead of e.width for example, you can use the e.control.size namedtuple (e.control.size.width or e.control.size[0])
  #   self.size = e
  #   self.update()

  def handle_keypress(self, data):
    players_word = ""
    response = []
    if data == "Back":
      self.word_screen.rmChar()
      self.word_screen.word_boxes[self.word_screen.current_row].borders()
    elif data == "Enter":
      if self.word_screen.word_boxes[self.word_screen.current_row].current_char == 5:
        for i in range(0,5):
          players_word += self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value
        response = validateWord(self.word, players_word)
        print(response)
        print(self.word,players_word)
        for i in range(0,5):
          if response[i] == 1: self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].right_position()
          elif response[i] == 0: self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].wrong_position()
          else:self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].not_existent()

        if self.word_screen.current_row < 5:
          self.word_screen.current_row += 1 
      else: 
        print("The word should consist of 5 characters")
      # Handle Enter key press
    else:
      self.word_screen.addChar(data)
      self.word_screen.word_boxes[self.word_screen.current_row].borders()

  def build(self):
    return ft.Column(controls=[self.word_screen, self.keyboard],
                     horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                     spacing=100, )


async def main(page: ft.Page):
  page.title = "Wordle Game"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.scroll = ft.ScrollMode.ADAPTIVE
  # create app control and add it to the page
  page.add(MainApp())


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
