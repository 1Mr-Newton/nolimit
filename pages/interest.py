from flet import *


class Interest(Container):
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
                Container(
                    Row(
                        alignment='spaceBetween',
                        controls=[
                            Icon(
                                icons.ARROW_BACK_IOS,
                                color='black',
                                size=18
                            ),
                            Container(
                                content=Text(
                                    value='Skip', color='black', size=14
                                )
                            )
                        ]
                    ),
                    padding=padding.symmetric(horizontal=10)
                ),
                Container(height=80),
                Text(
                    value='Time to customize your interest',
                    color='black'
                ),

                GridView(
                    child_aspect_ratio=1,
                    max_extent=100,
                    width=280,
                    spacing=35,
                    run_spacing=30,

                    controls=[
                        Container(
                            height=100, width=100, bgcolor='red'
                        ),
                    ]
                ),
                Container(height=150),
                Container(
                    height=50, width=200, bgcolor='blue',
                    border_radius=15,
                    content=Text('Continue'),
                    alignment=alignment.center,
                    on_click=lambda e: self.page.go('/dashboard')
                ),
            ]
        )
