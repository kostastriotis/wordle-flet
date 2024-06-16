import flet as ft

keyHeight = 60


class Key(ft.Container):

  def __init__(self, key: str, on_click=None):
    super().__init__()
    self.content = ft.Text(size=24,
                           weight=ft.FontWeight.W_700,
                           color=ft.colors.ON_SECONDARY_CONTAINER)
    self.alignment = ft.alignment.center
    self.bgcolor = ft.colors.SECONDARY_CONTAINER
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

  def change_color(self):
    self.content.color = ft.colors.WHITE


class KeyBoard(ft.UserControl):
  def __init__(self, key_handler):
    super().__init__()
    self.key_handler = key_handler
    self.list_of_keys = []
    
  def button_clicked(self, e):
    data = e.control.data
    self.key_handler(data)

  def build(self):
    Q = Key("Q", on_click=self.button_clicked)
    W = Key("W", on_click=self.button_clicked)
    E = Key("E", on_click=self.button_clicked)
    R = Key("R", on_click=self.button_clicked)
    T = Key("T", on_click=self.button_clicked)
    Y = Key("Y", on_click=self.button_clicked)
    U = Key("U", on_click=self.button_clicked)
    I = Key("I", on_click=self.button_clicked)
    O = Key("O", on_click=self.button_clicked)
    P = Key("P", on_click=self.button_clicked)
    A = Key("A", on_click=self.button_clicked)
    S = Key("S", on_click=self.button_clicked)
    D = Key("D", on_click=self.button_clicked)
    F = Key("F", on_click=self.button_clicked)
    G = Key("G", on_click=self.button_clicked)
    H = Key("H", on_click=self.button_clicked)
    J = Key("J", on_click=self.button_clicked)
    K = Key("K", on_click=self.button_clicked)
    L = Key("L", on_click=self.button_clicked)
    Z = Key("Z", on_click=self.button_clicked)
    X = Key("X", on_click=self.button_clicked)
    C = Key("C", on_click=self.button_clicked)
    V = Key("V", on_click=self.button_clicked)
    B = Key("B", on_click=self.button_clicked)
    N = Key("N", on_click=self.button_clicked)
    M = Key("M", on_click=self.button_clicked)
    
    self.list_of_english_keys = [Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M]
    row1_english = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        Q,W,E,R,T,Y,U,I,O,P
      ]
    )
    row2_english = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        A,S,D,F,G,H,J,K,L
      ]
    )
    enterKey = Key("Enter", on_click=self.button_clicked)
    enterKey.expand = 2
    backKey = Key("Back", on_click=self.button_clicked)
    backKey.expand = 2
    row3_english = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        backKey,
        Z,X,C,V,B,N,M,
        enterKey,
      ],
    )
    
    return ft.Column(
        spacing=0,
        # width= 5,
        alignment=ft.MainAxisAlignment.CENTER,
        # expand=1,
        controls=[
          row1_english,
          row2_english,
          row3_english
        ])
