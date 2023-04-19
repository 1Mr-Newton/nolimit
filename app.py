from flet import *
from pages.home import Home
from pages.interest import Interest
from pages.login import Login
from pages.signup import Signup
from pages.gender import Gender
from pages.dashboard import Dashboard


class App(UserControl):
    def __init__(self, page: Page):
        self.page = page
        self.page.on_route_change = self.route_change
        self.page.go('/')

    def route_change(self, route):
        self.page.views.clear()
        self.page.views.append(
            self.views_handler()[self.page.route]
        )

    def views_handler(self):
        return {
            '/': View(
                route='/',
                controls=[
                    Home(self.page)
                ]
            ),
            '/login': View(
                route='/login',
                controls=[
                    Login(self.page)
                ]
            ),
            '/signup': View(
                route='/signup',
                controls=[
                    Signup(self.page)
                ]
            ),
            '/gender': View(
                route='/gender',
                controls=[
                    Gender(self.page)
                ]
            ),
            '/interest': View(
                route='/interest',
                controls=[
                    Interest(self.page)
                ]
            ),
            '/dashboard': View(
                route='/dashboard',
                controls=[
                    Dashboard(self.page)
                ]
            ),
        }


app(target=App, assets_dir='assets')
