import flet as ft
from widgets.word_widget import *
from widgets.keyboard_widget import *
from helpers.size_aware import *
from functions import *
from screen import*

correct_color = '#6ca965'
wrong_position_color = '#c8b653'
non_existent_color = '#787c7f'


class MainApp(ft.UserControl):
  def __init__(self):
    super().__init__()
    self.word_screen = WordScreen()
    self.keyboard = KeyBoard(key_handler=self.handle_keypress)
    self.main_screen = Screen()
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
          if response[i] == 1: 
            self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].right_position()
            for key in self.keyboard.list_of_keys:
              if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                key.bgcolor = correct_color
                key.change_color()
                self.keyboard.update()


          elif response[i] == 0: 
            self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].wrong_position()
            for key in self.keyboard.list_of_keys:
              if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                if key.bgcolor != ft.colors.GREY_300:
                  continue
                else:
                  key.bgcolor = wrong_position_color
                  key.change_color()
                  self.keyboard.update()

          else:
            self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].not_existent()
            for key in self.keyboard.list_of_keys:
              if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                if key.bgcolor != ft.colors.GREY_300:
                  continue
                else:
                  key.bgcolor = non_existent_color
                  key.change_color()
                  self.keyboard.update()


        if self.word_screen.current_row < 5:
          self.word_screen.current_row += 1 
      else: 
        print("The word should consist of 5 characters")
      # Handle Enter key press
    else:
      self.word_screen.addChar(data)

  def build(self):
    return ft.Column(controls=[self.main_screen, self.word_screen, self.keyboard],
                     horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                     spacing=100, )


async def main(page: ft.Page):
  page.fonts = {
        "Arb" : "AbrilFatface-Regular.otf",
        "Oswald" : "Oswald-Bold.ttf",
        "Poppins-Regular" : "Poppins-Regular.otf",
        "Poppins-Bold" : "Poppins-Bold.otf",
        "Poppins-Black" : "Poppins-Black.otf"
        }
  page.theme = ft.Theme(font_family= "Poppins-Regular")
  page.title = "Wordle Game"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.scroll = ft.ScrollMode.ADAPTIVE
  # create app control and add it to the page
  page.add(MainApp())


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="Fonts")
