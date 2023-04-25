import flet as ft
from solitaire import Solitaire


def main(page: ft.Page):
    page.appbar = ft.AppBar(
        title=ft.Text("SutoSolitaire", color=ft.colors.BLACK87, weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.YELLOW_100,
        center_title=True,
        actions=[
            ft.IconButton(ft.icons.MENU, tooltip="Menu", icon_color=ft.colors.BLACK87),
        ],
        color=ft.colors.WHITE,
    )
    # page.update()
    solitaire = Solitaire()
    page.add(solitaire)


ft.app(target=main, assets_dir="assets")
