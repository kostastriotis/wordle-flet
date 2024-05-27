import flet as ft

keyHeight = 60


class Key(ft.Container):

  def __init__(self, key: str, on_click=None):
    super().__init__()
    self.content = ft.Text(size=24,
                           weight=ft.FontWeight.W_700,
                           color=ft.colors.BLACK)
    self.alignment = ft.alignment.center
    self.bgcolor = ft.colors.GREY_300
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
  def __init__(self, key_handler, language):
    super().__init__()
    self.language = language
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
    
    A_gr = Key("Α", on_click=self.button_clicked)
    B_gr = Key("Β", on_click=self.button_clicked)
    E_gr = Key("Ε", on_click=self.button_clicked)
    R_gr = Key("Ρ", on_click=self.button_clicked)
    T_gr = Key("Τ", on_click=self.button_clicked)
    U_gr = Key("Υ", on_click=self.button_clicked)
    L_gr = Key("Λ", on_click=self.button_clicked)
    I_gr = Key("Ι", on_click=self.button_clicked)
    O_gr = Key("Ο", on_click=self.button_clicked)
    J_gr = Key("Ξ", on_click=self.button_clicked)
    Omega_gr = Key("Ω", on_click=self.button_clicked)
    K_gr = Key("Κ", on_click=self.button_clicked)
    S_gr = Key("Σ", on_click=self.button_clicked)
    F_gr = Key("Φ", on_click=self.button_clicked)
    G_gr = Key("Γ", on_click=self.button_clicked)
    Ps_gr = Key("Ψ", on_click=self.button_clicked)
    Z_gr = Key("Ζ", on_click=self.button_clicked)
    D_gr = Key("Δ", on_click=self.button_clicked)
    M_gr = Key("Μ", on_click=self.button_clicked)
    N_gr = Key("Ν", on_click=self.button_clicked)
    X_gr = Key("Χ", on_click=self.button_clicked)
    H_gr = Key("Η", on_click=self.button_clicked)
    Th_gr = Key("Θ", on_click=self.button_clicked)
    P_gr = Key("Π", on_click=self.button_clicked)
    self.list_of_english_keys = [Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M]
    self.list_of_greek_keys = [A_gr,B_gr,G_gr,D_gr,E_gr,Z_gr,H_gr,Th_gr,I_gr,K_gr,L_gr,M_gr,N_gr,J_gr,O_gr,P_gr,R_gr,S_gr,T_gr,U_gr,F_gr,X_gr,Ps_gr,Omega_gr]
    row1_english = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        Q,W,E,R,T,Y,U,I,O,P
      ]
    )
    row1_greek = ft.Row(
      spacing = 3,
      width= 600,
      controls= [E_gr,R_gr,T_gr,U_gr,Th_gr,I_gr,O_gr,P_gr],
    )
    row2_english = ft.Row(
      spacing = 3,
      width= 750,
      controls=[
        A,S,D,F,G,H,J,K,L
      ]
    )
    row2_greek = ft.Row(
      spacing=3,
      width=600,
      controls=[A_gr,S_gr,D_gr,F_gr,G_gr,H_gr,J_gr,K_gr,L_gr],
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
    row3_greek = ft.Row(
      spacing=3,
      width=600,
      controls=[backKey,Z_gr,X_gr,Ps_gr,Omega_gr,B_gr,N_gr,M_gr,enterKey]
    )
    if self.language == "English":
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
    else:
      return ft.Column(
          spacing=0,
          # width= 5,
          alignment=ft.MainAxisAlignment.CENTER,
          # expand=1,
          controls=[
            row1_greek,
            row2_greek,
            row3_greek
          ])

