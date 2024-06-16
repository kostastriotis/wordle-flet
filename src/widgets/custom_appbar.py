import flet as ft


class GithubButton(ft.IconButton):

  def __init__(self, on_click):
    super().__init__()
    self.on_click = on_click
    self.content = ft.Image(
        src=
        "https://raw.githubusercontent.com/flet-dev/examples/main/python/apps/controls-gallery/assets/github-mark.svg",
        width=32,
        height=32,
        fit=ft.ImageFit.CONTAIN,
        color=ft.colors.ON_BACKGROUND)
    self.tooltip="Fork me on Github"


class CustomAppBar(ft.AppBar):

  def __init__(self, page: ft.Page):
    super().__init__()
    self.root_page = page
    # self.bgcolor = ft.colors.RED
    self.title = ft.Text(
        "WORDLE",
        size=42,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.ON_BACKGROUND,
        font_family="ManX",
    )
    self.center_title = True
    self.actions = [
      GithubButton(lambda _: self.root_page.launch_url("https://github.com/kostastriotis/wordle-flet"))
    ]