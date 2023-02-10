import unittest
from film import Film


class Test(unittest.TestCase):
    def setUp(self):
        self.films = [
            Film("film 1", "director 1", ["actor A", "actor B"], "genre 1", "origin 1", "language 1", 2.2, 10),
            Film("film 2", "director 2", ["actor C", "actor D"], "genre 2", "origin 2", "language 2", 4.3, 20),
            Film("film 3", "director 3", ["actor E", "actor F"], "genre 3", "origin 1", "language 1", 2.3, 30),
            Film("film 4", "director 4", ["actor G", "actor H"], "genre 4", "origin 2", "language 2", 3.4, 40),
        ]

    # check for dependency between origin and imdb_rate
    def test_dependency_of_country_and_origin(self):
        for i in range(len(self.films)):
            for j in range(i + 1, len(self.films)):
                self.assertFalse(
                    self.films[i].get_origin() == self.films[j].get_origin()
                    and self.films[i].get_imdb_rate() == self.films[j].get_imdb_rate()
                )

    # check for dependency between language and popularity
    def test_dependency_of_language_and_popularity(self):
        for i in range(len(self.films)):
            for j in range(i + 1, len(self.films)):
                self.assertFalse(
                    self.films[i].get_language() == self.films[j].get_language()
                    and self.films[i].get_popularity() == self.films[j].get_popularity()
                )


if __name__ == '__main__':
    unittest.main()
