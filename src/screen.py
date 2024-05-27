import flet as ft
class Screen(ft.UserControl):
    def build(self):
        self.error_handler = ft.Container(
            content= ft.Text("Not in Word List", color= "White"),
            alignment= ft.alignment.center,
            bgcolor= ft.colors.BLACK,
            width= 150,
            height= 30 ,
            visible= False
        )
        return ft.Column([self.error_handler])
def wordle_logo():
    main_screen=ft.Text("WORDLE", 
                            size=30, 
                            weight= ft.FontWeight.BOLD, 
                            color="Black",  
                            font_family= "Arb",
                            )
    return ft.Column([main_screen])
