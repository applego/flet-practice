import flet as ft
from solitaire import Solitaire


def main(page: ft.Page):
    def reset_clicked(e):
        solitaire.did_mount()

    page.appbar = ft.AppBar(
        title=ft.Text("SutoSolitaire", color=ft.colors.BLACK87, weight=ft.FontWeight.BOLD),
        bgcolor=ft.colors.YELLOW_100,
        center_title=True,
        actions=[
            ft.PopupMenuButton(
                icon=ft.icons.MENU,
                # tooltip="Menu",
                # icon_color=ft.colors.BLACK87,
                # on_click=menu_click
                items=[
                    ft.PopupMenuItem(
                        icon=ft.icons.RESTORE_PAGE,
                        content=ft.Image(src="card_back.png"),
                        text="Reset",
                        on_click=reset_clicked,
                    )
                ],
            ),
        ],
        color=ft.colors.BLACK87,
    )
    # page.update()
    solitaire = Solitaire()
    page.add(solitaire)


ft.app(target=main, assets_dir="assets")
