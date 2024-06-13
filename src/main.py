from logging import root
import flet as ft
from widgets.word_widget import *
from widgets.keyboard_widget import *
from widgets.leaderboard_widget import *
from widgets.username_input_widget import *
from widgets.score_widget import *
from helpers.size_aware import *
from functions import *
from leaderboard_functions import *
from screen import *
from widgets.custom_appbar import CustomAppBar

correct_color = '#6ca965'
wrong_position_color = '#c8b653'
non_existent_color = '#787c7f'
current_language = "English"
reset_color = ft.colors.SECONDARY_CONTAINER


def showSnackBar(page: ft.Page, text: str):
  page.snack_bar = ft.SnackBar(ft.Text(text,
                                       size=16,
                                       color=ft.colors.ON_ERROR_CONTAINER,
                                       weight=ft.FontWeight.BOLD),
                               bgcolor=ft.colors.ERROR_CONTAINER)
  page.snack_bar.open = True
  page.update()


class MainApp(ft.UserControl):

  def __init__(self, root_page: ft.Page):
    super().__init__()
    self.root_page = root_page
    # self.logo = wordle_logo()
    self.word_screen = WordScreen()
    self.keyboard = KeyBoard(key_handler=self.handle_keypress,
                             language=current_language)
    self.userbox = UsernameBox()
    self.leaderboard_dict = populate_leaderboard_dict()
    self.leader_board = Leaderboard(self.leaderboard_dict)
    self.score = 0
    self.scorebox = UserScoreBox()
    self.main_screen = Screen()
    self.word = getRandomWord()

  def handle_keypress(self, data):
    players_word = ""
    response = []

    if data == "Back":
      self.word_screen.rmChar()
      self.word_screen.word_boxes[self.word_screen.current_row].borders()

    elif data == "Enter":
      if self.word_screen.word_boxes[
          self.word_screen.current_row].current_char == 5:
        for i in range(0, 5):
          players_word += self.word_screen.word_boxes[
              self.word_screen.current_row].char_boxes[i].text.value
        response = validateWord(self.word, players_word)
        validate = dictionaryCheck(players_word)
        print(response)
        print(self.word, players_word)
        if validate:
          for i in range(0, 5):
            if response[i] == 1:
              self.word_screen.word_boxes[
                  self.word_screen.current_row].char_boxes[i].right_position()
            elif response[i] == 0:
              self.word_screen.word_boxes[
                  self.word_screen.current_row].char_boxes[i].wrong_position()
            else:
              self.word_screen.word_boxes[
                  self.word_screen.current_row].char_boxes[i].not_existent()

          for i in range(0, 5):
            if response[i] == 1:
              if current_language == "English":
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    key.bgcolor = correct_color
                    key.change_color()
                    self.keyboard.update()
              else:
                for key in self.keyboard.list_of_greek_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    key.bgcolor = correct_color
                    key.change_color()
                    self.keyboard.update()

            elif response[i] == 0:
              if current_language == "English":
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.SECONDARY_CONTAINER:
                      continue
                    else:
                      key.bgcolor = wrong_position_color
                      key.change_color()
                      self.keyboard.update()
              else:
                for key in self.keyboard.list_of_greek_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.SECONDARY_CONTAINER:
                      continue
                    else:
                      key.bgcolor = wrong_position_color
                      key.change_color()
                      self.keyboard.update()

            else:
              if current_language == "English":
                for key in self.keyboard.list_of_english_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.SECONDARY_CONTAINER:
                      continue
                    else:
                      key.bgcolor = non_existent_color
                      key.change_color()
                      self.keyboard.update()

              else:
                for key in self.keyboard.list_of_greek_keys:
                  if key.content.value == self.word_screen.word_boxes[
                      self.word_screen.current_row].char_boxes[i].text.value:
                    if key.bgcolor != ft.colors.SECONDARY_CONTAINER:
                      continue
                    else:
                      key.bgcolor = non_existent_color
                      key.change_color()
                      self.keyboard.update()

          self.word_screen.current_row += 1

        else:
          showSnackBar(self.root_page, "Not in Word List")
          # self.main_screen.error_handler.visible = True
          # self.main_screen.error_handler.update()
          # time.sleep(2)
          # self.main_screen.error_handler.visible = False
          # self.main_screen.error_handler.update()

        #Edw prepei na mpei o kwdikas gia reset tou programmatos se periptwsh nikhs
        if response == [1, 1, 1, 1, 1]:
          print("You won, yay!!\n")
          self.score += 1
          print(f"Score: {self.score}")
          self.reset()

        #Edw prepei na mpei o kwdikas gia reset tou programmatos se periptwsh htas
        if (self.word_screen.current_row == 6) and (response
                                                    != [1, 1, 1, 1, 1]):
          print("You lost :(\n")
          time.sleep(1)
          leaderboard_placement(self.leaderboard_dict,
                                self.userbox.textfield.value, self.score)
          save_leaderboard(self.leaderboard_dict)
          self.leader_board.populate()
          for rankbox in self.leader_board.rank_boxes:
            for tbox in rankbox.TextList:
              tbox.update()

          def close_dlg(e):
            dlg_modal.open = False
            self.root_page.update()
            self.score = 0
            self.reset()

          dlg_modal = ft.AlertDialog(
              modal=True,
              title=ft.Text("You lost ☹️"),
              content=ft.Text(f"Your score was: {str(self.score)}\nThe word was: {self.word}"),
              actions=[ft.TextButton("Replay", on_click=close_dlg)],
              actions_alignment=ft.MainAxisAlignment.END,
              on_dismiss=lambda e: print("Modal dialog dismissed!"),
          )
          self.root_page.dialog = dlg_modal
          dlg_modal.open = True
          self.root_page.update()
          ###

    else:
      self.word_screen.addChar(data)

  def reset(self):
    #Update Scorebox
    self.scorebox.ScoreBox.value= f"Score: {self.score}"
    self.scorebox.ScoreBox.update()

    #Adeiasma twn box & Reset to xrwma
    for word_box in self.word_screen.word_boxes:
      for char_box in word_box.char_boxes:
        word_box.rmChar()
        char_box.reset_position()

    #Keyboard Reset
    if current_language == "English":
      for key in self.keyboard.list_of_english_keys:
        key.bgcolor = reset_color
        key.content.color = ft.colors.ON_SECONDARY_CONTAINER
        self.keyboard.update()
    else:
      for key in self.keyboard.list_of_greek_keys:
        key.bgcolor = reset_color
        key.content.color = ft.colors.ON_SECONDARY_CONTAINER
        self.keyboard.update()

    #Epistrefoume thn eisodo sthn arxh twn box
    self.word_screen.current_row = 0
    self.word_screen.word_boxes[0].current_char = 0

    #Neo word
    self.word = getRandomWord()

  def build(self):
    return ft.Column(
        controls=[
            self.main_screen, self.word_screen, self.keyboard,self.scorebox ,self.userbox,
            self.leader_board
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=50,
    )


async def main(page: ft.Page):
  page.fonts = {
      "Arb": "AbrilFatface-Regular.otf",
      "Oswald": "Oswald-Bold.ttf",
      "Poppins-Regular": "Poppins-Regular.otf",
      "Poppins-Bold": "Poppins-Bold.otf",
      "Poppins-Black": "Poppins-Black.otf",
      "Comforta-Regular": "Comfortaa_Regular.ttf",
      "Comforta-Bold": "Comfortaa_Bold.ttf",
      "Clear-Sans-Regular": "ClearSans-Regular.ttf",
      "Clear-Sans-Bold": "ClearSans-Bold.ttf",
      "Clear-Sans-Medium": "ClearSans-Medium.ttf"
  }
  # page.theme = ft.Theme(font_family="Clear-Sans-Medium")
  page.theme_mode = ft.ThemeMode.SYSTEM
  page.title = "Wordle Game"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.scroll = ft.ScrollMode.ADAPTIVE
  # create app control and add it to the page
  page.appbar = CustomAppBar(page)
  page.add(MainApp(page))


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080, assets_dir="Fonts")
