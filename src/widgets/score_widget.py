import flet as ft

class UserScoreBox(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        
    def build(self):
        self.ScoreBox = ft.Text(text_align=ft.TextAlign.LEFT,size=25,value=f"Score: 0")
        return self.ScoreBox