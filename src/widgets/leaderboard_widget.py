import flet as ft
import tinydb 
#Widget gia emfanish tou leaderboard

#Gold Hex: #FFD700
#Silver Hex: #C0C0C0
#Bronze Hex: #CD7F32
#4th~10th Hex: Idk lefko gia thn wra

class RankBox(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.rankText  = ft.Text("Rank",color = "white",text_align=ft.TextAlign.LEFT,width=100,size=20,weight=ft.FontWeight.BOLD)
        self.nameText  = ft.Text("Name",color = "white",expand=1,size=18)
        self.scoreText = ft.Text("Score",color = "white",text_align=ft.TextAlign.RIGHT,expand=1,size=18)
        
        self.TextList = [self.rankText,self.nameText,self.scoreText]
        
    def build(self):
        self.container = ft.Container(ft.Row(controls=[self.rankText,self.nameText,self.scoreText],
                      expand=1))
        
        return self.container
    

class Leaderboard(ft.UserControl):
    def __init__(self,l_db = tinydb.TinyDB):
        super().__init__()
        self.leaderboard_db = l_db
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
        
    def populate(self):
        l_Query = tinydb.Query()
        
        for rank in range(1,11):
            if rank == 1:
                for box in self.rank_boxes[rank].TextList:
                    box.color = "#FFD700"
                    box.weight = ft.FontWeight.W_600
            if rank == 2:
                #Silver
                for box in self.rank_boxes[rank].TextList:
                    box.color = "#C0C0C0"
                    box.weight = ft.FontWeight.W_600
            if rank == 3:
                #Bronze
                for box in self.rank_boxes[rank].TextList:
                    box.color = "#CD7F32"
                    box.weight = ft.FontWeight.W_600
            self.rank_boxes[rank].rankText.value = rank
            self.rank_boxes[rank].nameText.value =  self.leaderboard_db.all()[rank-1]['name']
            self.rank_boxes[rank].scoreText.value = self.leaderboard_db.all()[rank-1]['score']
    
    def update_boxes(self):
        self.populate()
        for box in self.rank_boxes:
            for item in box.TextList:
                item.update()
        print('Boxes updated(*)')
    
    def build(self):
        #Title Box Attributes
        for box in self.rank_boxes[0].TextList:
            box.size = 23
            box.weight = ft.FontWeight.BOLD
            
        #Populate RankBoxes
        self.populate()
        
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
                                      bgcolor="#3005375c",
                                      width=750
                                      )
        
        self.ld_title = ft.Text(value="Leaderboard",size=40,text_align=ft.TextAlign.LEFT,weight=ft.FontWeight.BOLD)
        return ft.Column([self.ld_title,self.container])
    
