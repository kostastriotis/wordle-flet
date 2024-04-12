import flet as ft

boxSide = 72

class CharBox(ft.UserControl):
  def updateChar(self, char: str):
    # print(char)
    self.text.value = char
    self.main.border = ft.border.all(2, ft.colors.ON_SECONDARY_CONTAINER)
    if char == "":
      self.main.border = None
    
    self.update()

  def validate(self, response):
    self.main.bgcolor = ft.colors.GREEN
    self.update()

  def build(self):
    self.text = ft.Text(
      "",
      size=32,  # s:18, l:32
      weight=ft.FontWeight.W_700,
      color=ft.colors.ON_SECONDARY_CONTAINER)

    self.main = ft.Container(
      content=self.text,
      alignment=ft.alignment.center,
      bgcolor=ft.colors.SECONDARY_CONTAINER,
      width=boxSide,
      height=boxSide,
      # expand=1,
      margin=3,
      # aspect_ratio=1,
      # border=ft.border.all(2),
      border_radius=5)
    return self.main


class WordBox(ft.UserControl):

  def __init__(self):
    super().__init__()
    self.current_char = 0
    self.word = ""
    self.char_boxes = [CharBox(), CharBox(), CharBox(), CharBox(), CharBox()]

  def addChar(self, char: str):
    if self.current_char < 5:
      self.char_boxes[self.current_char].updateChar(char)
      self.word += char
      self.current_char += 1

  def rmChar(self):
    if self.current_char > 0:
      self.current_char -= 1
      self.char_boxes[self.current_char].updateChar("")
      # self.word += char
      

  def build(self):
    return ft.Row(
        spacing=0,
        # width= 390, # s:250, l: 390
        alignment=ft.MainAxisAlignment.CENTER,
        expand=1,
        controls=self.char_boxes)


class WordScreen(ft.UserControl):

  def __init__(self):
    super().__init__()
    self.current_row = 0
    self.word_boxes = [
        WordBox(),
        WordBox(),
        WordBox(),
        WordBox(),
        WordBox(),
        WordBox()
    ]

  def addChar(self, char: str):
    self.word_boxes[self.current_row].addChar(char)
    # self.update()

  def rmChar(self):
    self.word_boxes[self.current_row].rmChar()

  def build(self):
    return ft.Column(spacing=0, expand=1, controls=self.word_boxes)
