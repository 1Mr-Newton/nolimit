from flet import *


class Gender(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.padding = 10
        self.alignment = alignment.center
        self.bgcolor = 'white'
        self.height = 700
        self.width = 350
        self.content = Column(
            horizontal_alignment='center',
            controls=[
                Row(
                    controls=[
                        Icon(
                            icons.ARROW_BACK_IOS,
                            color='black',
                            size=18
                        )
                    ]
                ),
                Container(height=80),
                Text(
                    value='Which one are you?',
                    color='black'
                ),
                Row(
                    alignment='center',
                    controls=[
                        Container(
                            height=180, width=130,
                            border_radius=20,
                            bgcolor='blue'
                        ),
                        Container(
                            height=180, width=130,
                            border_radius=20,
                            bgcolor='blue'
                        ),
                    ]
                ),
                Text(
                    value='To give you a customize experience we need to know your gender',
                    text_align='center',
                    width=250
                ),
                Container(height=80),
                Container(
                    height=50, width=200, bgcolor='blue',
                    border_radius=15,
                    content=Text('Continue'),
                    alignment=alignment.center,
                    on_click=lambda e: self.page.go('/interest')
                ),
                Text(
                    value='Prefer not to choose',
                    size=14, color='black'
                )
            ]
        )
