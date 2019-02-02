# Classe principal onde é informada os atributos dos filmes
class Movie():

    """ Represents a way to store informations about a Movie.

    Attributes:
        title: Movie title
        storyline: A briefly description about movie storyline
        poster_image_url: URL for Movie poster image
        trailer_youtube_url: URL for Movie youtube trailer"""

    def __init__(
            self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
