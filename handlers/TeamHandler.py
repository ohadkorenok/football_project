from decorators.decorators import *
import tornado.ioloop
import tornado.web
from dbUtils import teamDbUtils


class TeamHandler(tornado.web.RequestHandler):
    @request_validation_decorator
    @create_team_validation_decorator
    def post(self):
        """
        The Request should Have ObjectId and msg.
        :param league_id: ObjectId String. 24 Letters in a specific format.
        :param team_name: string
        :param team_city: string
        :return: JSON
        """
        data = json.loads(self.request.body)
        self.write(teamDbUtils.create_team(**data))

    def get(self):
        """
        Get request in this format : team/?limit=xx&offset=xx
        return teams in this offset and in this capacity. default values as the constants.
        :return:
        """

        limit = int(self.get_argument("limit", DEFAULT_LIMIT, True))
        offset = int(self.get_argument("offset", DEFAULT_STARTING_ROW, True))
        self.write(teamDbUtils.get_teams(offset, limit))
