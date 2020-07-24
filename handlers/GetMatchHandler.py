import tornado.web
from dbUtils import matchDbUtils
from tornado import escape
from consts import *


class GetMatchHandler(tornado.web.RequestHandler):
    def get(self, match_id):
        """
        Get request in this format : match/match_id
        :param match_id: str ObjectID
        :return: JSON with the desired team.
        """
        try:
            if match_id:
                self.write(matchDbUtils.get_match(match_id))
            else:
                self.write(
                    escape.json_encode({"return_code": MATCH_DOES_NOT_EXIST, "Message": 'Match does not exist'}))
        except Exception as e:
            self.write(
                escape.json_encode({'return_code': UNKNOWN_EXCEPTION, 'Error': str(e), 'Message': 'Unknown Exception'}))