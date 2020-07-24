__author__ = 'ohad koren'

import os

TEMPLATES_DIRECTORY = os.path.join(os.path.dirname(__file__), "templates")
STATIC_DIRECTORY = os.path.join(os.path.dirname(__file__), "static")

DEFAULT_LIMIT = 50
DEFAULT_STARTING_ROW = 0
DEFAULT_LEAST = 1
############ RETURN CODES ###############

LEAGUE_ALREADY_EXIST = -1
LEAGUE_DOES_NOT_EXIST = -2
TEAM_ALREADY_EXIST = -3
TEAM_DOES_NOT_EXIST = -4
MATCH_ALREADY_EXIST = -5
MATCH_DOES_NOT_EXIST = -6
INVALID_FIELDS = -7
USER_ALREADY_FOLLOWING = -8
UNKNOWN_EXCEPTION = -9
BAD_PARAMETERS_ERROR = -10
NO_DATA = -11

#########################################


########## For Local Development############s
MONGO_USER = "root"
MONGO_PASSWORD = "example"
MONGO_URI = r"mongodb://root:example@mongo:27017/db1?authSource=admin"
MONGO_URI_local = r"mongodb://root:example@localhost:27017/db1?authSource=admin"

MONGO_DB_URL = "0.0.0.0"
MONGO_DB_PORT = 27017
SERVER_PORT = "8888"
