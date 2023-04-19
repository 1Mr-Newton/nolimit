from flet import *


class Dashboard(Container):
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.alignment = alignment.center
        self.bgcolor = 'white'
        self.height = 700
        self.width = 350
        self.content = Column(
            controls=[
                Row(
                    alignment='spaceBetween',
                    controls=[
                        Text(
                            value='Hi, Grace'
                        ),
                        CircleAvatar(
                            radius=10
                        )
                    ]
                )
            ]
        )
