__author__ = 'ohad koren'

import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")