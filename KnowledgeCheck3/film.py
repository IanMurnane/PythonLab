class Film:
    def __init__(self, title, director, actors, genre, origin, language, imdb_rate, popularity):
        self.title = title
        self.director = director
        self.actors = actors
        self.genre = genre
        self.origin = origin
        self.language = language
        self.imdb_rate = imdb_rate
        self.popularity = popularity

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_actors(self):
        return self.actors

    def set_actors(self, actors):
        self.actors = actors

    def get_genre(self):
        return self.genre

    def set_genre(self, genre):
        self.genre = genre

    def get_origin(self):
        return self.origin

    def set_origin(self, origin):
        self.origin = origin

    def get_language(self):
        return self.language

    def set_language(self, language):
        self.language = language

    def get_imdb_rate(self):
        return self.imdb_rate

    def set_imdb_rate(self, imdb_rate):
        self.imdb_rate = imdb_rate

    def get_popularity(self):
        return self.popularity

    def set_popularity(self, popularity):
        self.popularity = popularity
