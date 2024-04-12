import flet as ft
from widgets.word_widget import *
from widgets.keyboard_widget import *
from helpers.size_aware import *


class MainApp(ft.UserControl):
  def __init__(self):
    super().__init__()
    self.word_screen = WordScreen()
    self.keyboard = KeyBoard(key_handler=self.handle_keypress)

  # def handle_resize(self, e: ft.canvas.CanvasResizeEvent):
  #   # instead of e.width for example, you can use the e.control.size namedtuple (e.control.size.width or e.control.size[0])
  #   self.size = e
  #   self.update()

  def handle_keypress(self, data):
    if data == "Back":
      self.word_screen.rmChar()
    elif data == "Enter":
      # Handle Enter key press
      pass
    else:
      self.word_screen.addChar(data)

  def build(self):
    return ft.Column(horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                     controls=[self.word_screen, self.keyboard])


async def main(page: ft.Page):
  page.title = "Wordle Game"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.scroll = ft.ScrollMode.ADAPTIVE
  # create app control and add it to the page
  page.add(MainApp())


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
