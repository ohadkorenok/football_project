import tornado.web
from dbUtils import teamDbUtils
from consts import *


class MostWinsHandler(tornado.web.RequestHandler):
    def get(self):
        """
        Get request in this format : team/team_id
        :param least - will have 1 if we look for least wins and -1 if we look for most. At default, most is
        chosen which means value -1.
        :return: JSON with the desired team.
        """
        least = int(self.get_argument("least", DEFAULT_LEAST, True))
        self.write(teamDbUtils.sort_and_prepare('wins', least))
