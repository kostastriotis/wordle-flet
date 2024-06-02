import flet as ft
#Widget gia emfanish tou leaderboard

class RankBox(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.rankText  = ft.Text("Rank",color = "white",text_align=ft.TextAlign.LEFT,width=100)
        self.nameText  = ft.Text("Name",color = "white",expand=1)
        self.scoreText = ft.Text("Score",color = "white",text_align=ft.TextAlign.RIGHT,expand=1)
        
    def build(self):
        self.container = ft.Container(ft.Row(controls=[self.rankText,self.nameText,self.scoreText],
                      expand=1))
        
        return self.container
    

class Leaderboard(ft.UserControl):
    def __init__(self,leaderboard_dict:dict):
        super().__init__()
        self.leaderboard = leaderboard_dict
        self.rank_boxes = [
            RankBox(),#gia titlos 0
            RankBox(),#1
            RankBox(),#2
            RankBox(),#3
            RankBox(),#4
            RankBox(),#5
            RankBox(),#6
            RankBox(),#7
            RankBox(),#8
            RankBox(),#9
            RankBox()#10
        ]
    def build(self):
        #Populate RankBoxes
        for rank in self.leaderboard:
            self.rank_boxes[int(rank)].rankText.value = rank
            self.rank_boxes[int(rank)].nameText.value =  self.leaderboard[rank][0]
            self.rank_boxes[int(rank)].scoreText.value = self.leaderboard[rank][1]
        
        self.container = ft.Container(content=ft.Column(controls= self.rank_boxes,
                                                        expand=1,
                                                        spacing=5,
                                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER
                                                        ),
                                      alignment=ft.alignment.center,
                                      padding=10,
                                      margin=10,
                                      border=ft.border.all(width=3,color="#50023c67"),
                                      border_radius=10,
                                      bgcolor="#3005375c"
                                      )
        return self.container
    
