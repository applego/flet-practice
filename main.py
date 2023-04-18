import flet
from flet import Column, Container, ElevatedButton, Page, Row, Text, UserControl, border_radius, colors

from Calclator_final import CalculatorApp
from Greetings import GreetingsApp


def main(page: Page):
    page.title = "Calc App"

    # create application instance
    calc = CalculatorApp()

    # add application's root control to the page
    page.add(calc)

    greetings = GreetingsApp()
    page.add(greetings)


flet.app(target=main)
