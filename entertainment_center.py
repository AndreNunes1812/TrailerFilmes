import fresh_tomatoes
import media
import yaml
import tmdbsimple as tmdb

# variavel de identifica o caminho a ser consumido
BASE_URL_POSTER = "https://image.tmdb.org/t/p/w500"

# variavel que identifica o caminho de acesso a visualização no YOUTUBE
BASE_URL_YOUTUBE = "https://www.youtube.com/watch?v="

# função que faz a leitura de um determinado arquivo  (movies_list.yaml)


def get_movies_from_file():
    """Recupera um conj de filmes no formato media.Movie"""
    """a partir de um arquivo yam """

    # Obtem a lista de filmes a partir de arquivo no formato yaml
    movies_list_doc = open("filmes_lista.yaml")
                              
    # Le os dados do arquivo e instancia objetos da classe Movie
    parsed_movies = yaml.load(movies_list_doc)
    movies_list_doc.close()
    return parsed_movies


def get_id_youtube_trailer(movie_id):
    """ Recupera o identificador do trailer no youtube a partir da API do TMDB
        com base no identificador do filme informado.

    Args:
        movie_id: Id do filme no tmdb.
    """
    return tmdb.Movies(movie_id).videos()['results'][0]['key']


def create_movie_from(r_dict):
    """Cria / Devolve uma instancia de media.Movie.

    Instancia um objeto Movie a partir de um objeto dict contendo
    as propriedades do filme.

    Args:
        result: Dicionario chave-valor contendo os dados do filme.
    """

    movie_id = r_dict['id']
    title = r_dict['title']
    storyline = r_dict['overview']
    poster_path = BASE_URL_POSTER + r_dict['poster_path']
    youtube_trailer = BASE_URL_YOUTUBE + get_id_youtube_trailer(movie_id)

    return media.Movie(title, storyline, poster_path, youtube_trailer)

# Função que dispara para fazer o consumo da API ( https://www.themoviedb.org )


def get_movies_from_tmdb():
    """Retorna uma lista de filmes.

    Utiliza a API do https://www.themoviedb.org para recuperar um conjunto
    de filmes.
    """

    # Substituir o <MY_API_KEY> pela chave utilizada para acesso a API do tmdb.
    tmdb.API_KEY = 'ec53f41c9cbf429b4c65e684e93838c2'
    client = tmdb.Movies()

    # A function upcoming() devolve os filmes mais recentes.
    movies_upcoming_dict = client.upcoming()

    movies = []
    for r_dict in movies_upcoming_dict['results']:
        movies.append(create_movie_from(r_dict))

    return movies


# Criação de um array de filmes
filmes = []

""" a função get_movies_from_tmdb() faz uma requisição para """
""" API https://www.themoviedb.org, """
""" caso não seja possivel consumir as informações,  """
""" será lancada uma execeção (funcao) que devera """
""" será lido o arquivo que se encontra em /movies_list.yaml. """
try:
    filmes = get_movies_from_tmdb()
    print("com internet")
except:
    filmes = get_movies_from_file()
    print("sem internet")

# Função que abre o browse e gera os filmes conforme modelo definido.
fresh_tomatoes.open_movies_page(filmes)
