from couchpotato.core.logger import CPLog
from couchpotato.core.providers.automation.base import Automation
import datetime

log = CPLog(__name__)


class PopularMovies(Automation):

    interval = 1800
    url = 'https://s3.amazonaws.com/popular-movies/movies.json'

    def getIMDBids(self):

        movies = []
        retrieved_movies = self.getJsonData(self.url)

        for movie in retrieved_movies.get('movies'):
            imdb_id = movie.get('imdb_id')
            movies.append(imdb_id)

        return movies