from config import Title, Icon


class Figure:
    def __init__(self, color, title):
        self.color = color
        self.title = title
        self.ref = None

    def __repr__(self):
        title = Title(self.title).name
        return Icon[title].value
