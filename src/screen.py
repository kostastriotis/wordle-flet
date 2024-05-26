import flet as ft
class Screen(ft.UserControl):
    def build(self):
        self.main_screen=ft.Text("WORDLE", 
                            size=30, 
                            weight= ft.FontWeight.BOLD, 
                            color="Black",  
                            font_family= "Arb"
                            )
        return ft.Row([self.main_screen],
                      spacing= 10,alignment=ft.MainAxisAlignment.CENTER)