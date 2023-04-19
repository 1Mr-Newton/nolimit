from flet import *


class Home(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.alignment = alignment.center
        self.bgcolor = 'white'
        self.height = 700
        self.width = 350
        self.content = Column(
            spacing=0,
            horizontal_alignment='center',
            controls=[
                Container(height=50),
                Text(
                    value='No Limit',
                    color='black',
                    weight=FontWeight.BOLD,
                    size=20,
                ),

                Text(
                    value='We always make sure you stay fit',
                    color='black',
                    weight=FontWeight.BOLD,
                    size=14,
                    text_align='center'
                ),
                Image(
                    src='assets/imgs/i2.jpg',
                    scale=0.8
                ),
                Container(height=280),
                Container(
                    alignment=alignment.center,
                    bgcolor='blue',
                    content=Text(
                        value='Get Started'
                    ),
                    width=160,
                    height=35,
                    border_radius=10,
                    on_click=lambda e: self.page.go('/gender')

                ),
                Row(
                    alignment='center',
                    controls=[
                        Text(
                            value='Already have an account?',
                        ),
                        Container(
                            content=Text(
                                value='Sign in',
                            ),
                            on_click=lambda e: print('hello w')
                        )
                    ]
                )
            ]
        )
