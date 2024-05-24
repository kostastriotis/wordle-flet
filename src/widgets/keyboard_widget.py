import flet as ft

keyHeight = 60


class Key(ft.Container):

  def __init__(self, key: str, on_click=None):
    super().__init__()
    self.content = ft.Text(size=24,
                           weight=ft.FontWeight.W_700,
                           color=ft.colors.ON_PRIMARY_CONTAINER)
    self.alignment = ft.alignment.center
    self.bgcolor = ft.colors.PRIMARY_CONTAINER
    # self.width = 54
    self.height = keyHeight
    self.expand = 1
    self.margin = 3
    self.padding = 3
    self.border_radius = 4
    self.ink = True
    self.content.value = key
    self.on_click=on_click
    self.data = key


class KeyBoard(ft.UserControl):
  def __init__(self, key_handler):
    super().__init__()
    self.key_handler = key_handler
    
  def button_clicked(self, e):
    data = e.control.data
    self.key_handler(data)

  def build(self):
    row1 = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        Key("Q", on_click=self.button_clicked),
        Key("W", on_click=self.button_clicked),
        Key("E", on_click=self.button_clicked),
        Key("R", on_click=self.button_clicked),
        Key("T", on_click=self.button_clicked),
        Key("Y", on_click=self.button_clicked),
        Key("U", on_click=self.button_clicked),
        Key("I", on_click=self.button_clicked),
        Key("O", on_click=self.button_clicked),
        Key("P", on_click=self.button_clicked),
      ]
    )
    row2 = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        Key("A", on_click=self.button_clicked),
        Key("S", on_click=self.button_clicked),
        Key("D", on_click=self.button_clicked),
        Key("F", on_click=self.button_clicked),
        Key("G", on_click=self.button_clicked),
        Key("H", on_click=self.button_clicked),
        Key("J", on_click=self.button_clicked),
        Key("K", on_click=self.button_clicked),
        Key("L", on_click=self.button_clicked),
      ]
    )
    enterKey = Key("Enter", on_click=self.button_clicked)
    enterKey.expand = 2
    backKey = Key("Back", on_click=self.button_clicked)
    backKey.expand = 2
    row3 = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        backKey,
        Key("Z", on_click=self.button_clicked),
        Key("X", on_click=self.button_clicked),
        Key("C", on_click=self.button_clicked),
        Key("V", on_click=self.button_clicked),
        Key("B", on_click=self.button_clicked),
        Key("N", on_click=self.button_clicked),
        Key("M", on_click=self.button_clicked),
        enterKey,
      ]
    )
    return ft.Column(
        spacing=0,
        # width= 5,
        alignment=ft.MainAxisAlignment.CENTER,
        # expand=1,
        controls=[
          row1,
          row2,
          row3
        ])