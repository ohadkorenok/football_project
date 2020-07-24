import tornado.web
from dbUtils import leagueDbUtils
from tornado import escape
from consts import *


class GetLeagueHandler(tornado.web.RequestHandler):
    def get(self, league_id):
        """
        Get request in this format : league/league_id
        :param league_id: str ObjectID
        :return: JSON with the desired league.
        """
        try:
            if league_id:
                self.write(leagueDbUtils.get_league(league_id))
            else:
                self.write(
                    escape.json_encode({"return_code": LEAGUE_DOES_NOT_EXIST, "Message": 'League does not exist'}))
        except Exception as e:
            self.write(
                escape.json_encode({'return_code': UNKNOWN_EXCEPTION, 'Error': str(e), 'Message': 'Unknown Exception'}))
