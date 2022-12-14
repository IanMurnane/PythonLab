from config import Color, Icon, Title


class Figure:
    def __init__(self, color, title):
        self.color = color
        self.title = title
        self.ref = None

    def __repr__(self):
        return Icon[self.get_title()].value

    def get_color(self):
        return Color(self.color).name

    def get_title(self):
        return Title(self.title).name
