import flet as ft

class UsernameBox(ft.UserControl):
    def __init__(self):
        super().__init__()
        
        #Functions Start
        def submit_button_clicked(e):
            if self.textfield.value!='':
                self.TextBox.value = f"Hello {self.textfield.value}!"
                while self.control!=[]:
                    self.control.pop()
                self.control.append(self.TextBox)
                ft.View.update(self)
                print("Name Entered(*)")
            
        def hide_button_clicked(e):
            while self.control!=[]:
                    self.control.pop()
            ft.View.update(self)
            print("Userbox Hidden(*)")
        
        #Functions End
        
        #Empty box
        self.textfield = ft.TextField(autocorrect=False,
                                      label="Enter Name",
                                      max_length=30)
        self.button_submit = ft.ElevatedButton(text="Submit",on_click=submit_button_clicked)#-->Allazei ta controls tou ft.Row sto self.TextBox
        self.button_ignore = ft.ElevatedButton(text="Hide",on_click=hide_button_clicked)#--> Krybei to ft.Row
        
        #Entered
        self.TextBox= ft.Text(text_align=ft.TextAlign.LEFT,size=20)
        
    
    def build(self):
        self.control=[self.textfield,self.button_submit,self.button_ignore]   
        
        return ft.Row(controls=self.control,vertical_alignment=ft.CrossAxisAlignment.CENTER,alignment=ft.MainAxisAlignment.CENTER)