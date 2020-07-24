
import tornado.web
from dbUtils import teamDbUtils
from tornado import escape
from consts import *


class GetTeamHandler(tornado.web.RequestHandler):
    def get(self, team_id):
        """
        Get request in this format : team/team_id
        :param team_id: str ObjectID
        :return: JSON with the desired team.
        """
        try:
            if team_id:
                self.write(teamDbUtils.get_team(team_id))
            else:
                self.write(
                    escape.json_encode({"return_code": TEAM_DOES_NOT_EXIST, "Message": 'Team does not exist'}))
        except Exception as e:
            self.write(
                escape.json_encode({'return_code': UNKNOWN_EXCEPTION, 'Error': str(e), 'Message': 'Unknown Exception'}))
