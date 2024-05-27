import flet as ft
import time

boxSide = 72
correct_color = '#6ca965'
wrong_position_color = '#c8b653'
non_existent_color = '#787c7f'

class CharBox(ft.UserControl):
  def updateChar(self, char: str):
    # print(char)
    self.text.value = char
    # if char == "":
      # self.main.border = ft.border.all(2, ft.colors.GREY)    
    
    self.update()

  def right_position(self):
    self.main.animate_scale = ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_IN)
    self.main.scale = 0
    self.main.bgcolor = correct_color
    self.text.color = ft.colors.WHITE
    self.main.border = None
    self.update()
    self.main.animate_scale = ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_OUT)
    time.sleep(0.05)
    self.main.scale = 1
    self.update()
  
  def not_existent(self):
    self.main.animate_scale = ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_IN)
    self.main.scale = 0
    self.main.bgcolor = non_existent_color
    self.text.color = ft.colors.WHITE
    self.main.border = None
    self.update()
    self.main.animate_scale = ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_OUT)
    time.sleep(0.05)
    self.main.scale = 1
    self.update()

  def wrong_position(self):
    self.main.animate_scale = ft.animation.Animation(0, ft.AnimationCurve.BOUNCE_IN)
    self.main.scale = 0
    self.main.bgcolor = wrong_position_color
    self.text.color = ft.colors.WHITE
    self.main.border = None
    self.update()
    self.main.animate_scale = ft.animation.Animation(700, ft.AnimationCurve.BOUNCE_OUT)
    time.sleep(0.05)
    self.main.scale = 1
    self.update()
  


  def build(self):
    self.text = ft.Text(
      "",
      size=32,  # s:18, l:32
      weight=ft.FontWeight.W_700,
      color=ft.colors.BLACK)

    self.main = ft.Container(
      content=self.text,
      alignment=ft.alignment.center,
      bgcolor=ft.colors.GREY_50,
      width=boxSide,
      height=boxSide,
      # expand=1,
      margin=0,
      # aspect_ratio=1,
      border=ft.border.all(2, ft.colors.GREY_300),
      border_radius=5,
      scale = ft.transform.Scale(scale=1),
      animate_scale= ft.animation.Animation(50, ft.AnimationCurve.BOUNCE_IN))
    return self.main
  
  def animation1(self):
    self.main.scale = 1.05
    self.update()
  
  def animation2(self):
    self.main.scale = 1
    self.update()



class WordBox(ft.UserControl):

  def __init__(self):
    super().__init__()
    self.current_char = 0
    self.word = ""
    self.char_boxes = [CharBox(), CharBox(), CharBox(), CharBox(), CharBox()]

  def addChar(self, char: str):
    if self.current_char < 5:
      self.char_boxes[self.current_char].animation1()
      self.char_boxes[self.current_char].updateChar(char)
      self.char_boxes[self.current_char].main.border = ft.border.all(2, ft.colors.GREY)
      self.char_boxes[self.current_char].update()
      time.sleep(0.05)
      self.char_boxes[self.current_char].animation2()
      self.current_char += 1

  def rmChar(self):
    if self.current_char > 0:
      self.current_char -= 1
      self.char_boxes[self.current_char].updateChar("")
      # self.word += char


  def borders(self):
    for i in range(0,5):
      if self.char_boxes[i].text.value == "":
        self.char_boxes[i].main.border = ft.border.all(2, ft.colors.GREY_300)
        self.char_boxes[i].main.update()
      else:
        self.char_boxes[i].main.border = ft.border.all(2, ft.colors.GREY)
        self.char_boxes[i].main.update()


  def build(self):
    return ft.Row(
        spacing=3,
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
    return ft.Column(spacing=3, expand=1, controls=self.word_boxes)
