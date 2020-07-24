from decorators.decorators import *
import tornado.web
from dbUtils import leagueDbUtils


class LeagueHandler(tornado.web.RequestHandler):
    @request_validation_decorator
    @create_league_validation_decorator
    def post(self):
        """
        This method creates a league in the DB. params will be organized in data dict with the following keys:
        :param league_country: str
        :param league_name: str
        :param league_level: int
        :return: JSON of the league.
        """
        data = json.loads(self.request.body)
        self.write(leagueDbUtils.create_league(**data))

    def get(self):
        """
        Get request in this format : league/?limit=xx&offset=xx
        return leagues in this offset and in this capacity. default values as the constants.
        :return:
        """
        limit = int(self.get_argument("limit", DEFAULT_LIMIT, True))
        offset = int(self.get_argument("offset", DEFAULT_STARTING_ROW, True))
        self.write(leagueDbUtils.get_leagues(offset, limit))
