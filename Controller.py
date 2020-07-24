__author__ = 'Ohad Koren'

import tornado.ioloop
import tornado.web
import tornado.httpserver
import sys
from handlers.GetTeamHandler import GetTeamHandler
from handlers.TeamHandler import TeamHandler
from handlers.LeagueHandler import LeagueHandler
from handlers.GetLeagueHandler import GetLeagueHandler
from handlers.GetMatchHandler import GetMatchHandler
from handlers.MatchHandler import MatchHandler
from handlers.MostGoalsHandler import MostGoalsHandler
from handlers.MostWinsHandler import MostWinsHandler
from consts import *

settings = dict(
    template_path=TEMPLATES_DIRECTORY,
    static_path=STATIC_DIRECTORY,
    debug=True
)

application = tornado.web.Application([
    (r"/league/(\w+)", GetLeagueHandler),
    (r"/league/", LeagueHandler),
    (r"/team/(\w+)", GetTeamHandler),
    (r"/team/", TeamHandler),
    (r"/match/(\w+)", GetMatchHandler),
    (r"/match/", MatchHandler),
    (r"/most_goals/", MostGoalsHandler),
    (r"/most_wins/", MostWinsHandler)

], **settings)

if __name__ == "__main__":
    try:
        print("the server has started on port {}".format(SERVER_PORT))
        http_server = tornado.httpserver.HTTPServer(application)
        port = int(os.environ.get("PORT", SERVER_PORT))
        http_server.listen(port)
        tornado.ioloop.IOLoop.instance().start()
    except:
        sys.exc_info()
