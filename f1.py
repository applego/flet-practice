import flet as ft


def main(page: ft.Page):
    # add/update controls on Page
    page.add(ft.Text(value="Hello World!"))


ft.app(target=main)
