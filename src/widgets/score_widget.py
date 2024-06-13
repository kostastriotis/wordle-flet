import flet as ft

class UserScoreBox(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        
    def build(self):
        self.ScoreBox = ft.Text(text_align=ft.TextAlign.LEFT,size=25,value=f"Score: 0")
        self.main = ft.Container(
            content=self.ScoreBox,
            alignment=ft.alignment.center,
            bgcolor=ft.colors.SECONDARY_CONTAINER,
            expand_loose=1,
            width=300,
            height=50,
            margin=0,
            border=ft.border.all(2, ft.colors.GREY),
            border_radius=5,
            scale = ft.transform.Scale(scale=1),
            animate_scale= ft.animation.Animation(50, ft.AnimationCurve.BOUNCE_IN))
        return self.main