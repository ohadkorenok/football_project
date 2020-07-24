__author__ = 'ohad koren'

from pymongo import MongoClient, DESCENDING
from consts import *

mongo_client = MongoClient(MONGO_URI)
football_db = mongo_client.get_default_database()
team_collection = football_db['teamCollection']
team_collection.create_index([('team_name', DESCENDING), ('goals', DESCENDING), ('wins', DESCENDING)])
league_collection = football_db['leagueCollection']
match_collection = football_db['matchCollection']
