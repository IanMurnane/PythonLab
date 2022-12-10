from utils import Color, Title, BlackIcon, WhiteIcon


class Figure:
    def __init__(self, color, title):
        self.color = color
        self.title = title

    def move(self):
        pass

    def beat(self):
        pass

    def __repr__(self):
        title = Title(self.title).name
        if self.color == Color.WHITE:
            return WhiteIcon[title].value
        else:
            return BlackIcon[title].value
