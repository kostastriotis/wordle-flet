import flet as ft
from widgets.word_widget import *
from widgets.keyboard_widget import *
from widgets.leaderboard_widget import *
from widgets.username_input_widget import *
from helpers.size_aware import *
from functions import *
from leaderboard_functions import *
from screen import*

correct_color = '#6ca965'
wrong_position_color = '#c8b653'
non_existent_color = '#787c7f'
current_language = "English"


class MainApp(ft.UserControl):
  def __init__(self):
    super().__init__()
    self.logo = wordle_logo()
    self.word_screen = WordScreen()
    self.keyboard = KeyBoard(key_handler=self.handle_keypress, language= current_language )
    self.userbox = UsernameBox()
    self.leaderboard_dict = populate_leaderboard_dict()
    self.leader_board = Leaderboard(self.leaderboard_dict)
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
        validate =  dictionaryCheck(players_word)
        print(response)
        print(self.word,players_word)
        if validate:
          for i in range(0,5):
            if response[i] == 1: 
              self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].right_position()
            elif response[i] == 0: 
              self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].wrong_position()
            else:
              self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].not_existent()
          
          
          
          for i in range(0,5):
            if response[i] == 1:
              if current_language == "English" :
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                    key.bgcolor = correct_color
                    key.change_color()
                    self.keyboard.update()
              else:
                for key in self.keyboard.list_of_greek_keys:
                  if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                    key.bgcolor = correct_color
                    key.change_color()
                    self.keyboard.update()


            elif response[i] == 0: 
              if current_language == "English" :
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.GREY_300:
                      continue
                    else:
                      key.bgcolor = wrong_position_color
                      key.change_color()
                      self.keyboard.update()
              else:
                for key in self.keyboard.list_of_greek_keys:
                  if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.GREY_300:
                      continue
                    else:
                      key.bgcolor = wrong_position_color
                      key.change_color()
                      self.keyboard.update()


            else:
              if current_language == "English" :
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.GREY_300:
                      continue
                    else:
                      key.bgcolor = non_existent_color
                      key.change_color()
                      self.keyboard.update()
              
              
              else:
                for key in self.keyboard.list_of_greek_keys:
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
          self.main_screen.error_handler.visible = True
          self.main_screen.error_handler.update()
          time.sleep(2)
          self.main_screen.error_handler.visible = False
          self.main_screen.error_handler.update()
          
         #Edw
   
   
    else:
      self.word_screen.addChar(data)

  def build(self):
    return ft.Column(controls=[self.logo, self.main_screen, self.word_screen, self.keyboard,self.userbox,self.leader_board],
                     horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                     spacing=50, )

async def main(page: ft.Page):
  page.fonts = {
        "Arb" : "AbrilFatface-Regular.otf",
        "Oswald" : "Oswald-Bold.ttf",
        "Poppins-Regular" : "Poppins-Regular.otf",
        "Poppins-Bold" : "Poppins-Bold.otf",
        "Poppins-Black" : "Poppins-Black.otf",
        "Comforta-Regular" : "Comfortaa_Regular.ttf",
        "Comforta-Bold" : "Comfortaa_Bold.ttf",
        "Clear-Sans-Regular" : "ClearSans-Regular.ttf",
        "Clear-Sans-Bold" : "ClearSans-Bold.ttf",
        "Clear-Sans-Medium" : "ClearSans-Medium.ttf"
        }
  page.theme = ft.Theme(font_family= "Clear-Sans-Medium")
  page.title = "Wordle Game"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.scroll = ft.ScrollMode.ADAPTIVE
  # create app control and add it to the page
  page.add(MainApp())


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="Fonts")
