__author__ = 'ohad koren'

from dbUtils.commonDbUtils import get_item, get_items
from pymongo.errors import InvalidId
from dbUtils.db import team_collection, league_collection
from bson.objectid import ObjectId
from bson.json_util import dumps
from consts import *


def create_team(league_id: str, team_name: str, team_city: str):
    """
    This function Inserts a team to the db.
    :param league_id:  - String that has 24 Letters .
    :param team_name: string
    :param team_city: string
    :return: JSON Return codes or team_collection document that represents the inserted team
    """
    try:
        league = league_collection.find_one({
            "_id": ObjectId(league_id)
        })

        if league is None:
            return {"return_code": LEAGUE_DOES_NOT_EXIST,
                    "Message": 'There is no such league! cannot add a team without a league'}

        team_from_db = team_collection.find_one({'team_name': team_name})
        if team_from_db is not None:
            return {"return_code": TEAM_ALREADY_EXIST, "Message": "There is already a team in this name in the"
                                                                  " system Cannot enter to DB"}
        team = {
            'league_id': league_id,
            'team_name': team_name,
            'city': team_city,
            'goals': 0,
            'wins': 0,
        }
        team_collection.insert(team)
        return dumps(team)
    except InvalidId as e:
        return {"return_code": INVALID_FIELDS,
                "Message": 'Exception while creating a team, league_id is not valid ObjectID', 'Error': str(e)}
    except Exception as e:
        return {"return_code": UNKNOWN_EXCEPTION,
                "Message": 'Unknown exception while creating a team', 'Error': str(e)}


def sort_and_prepare(key, least):
    """
    This method handles the sort of the `key` key in the object and represents the maximal / minimal depend on the least
    variable
    :param key:
    :param least:
    :return:
    """
    cursor = team_collection.find().sort(key, least).limit(1)
    try:
        object_to_return = cursor.next()
        return dumps(object_to_return)
    except StopIteration as e:
        return {"return_code": NO_DATA, "Message": "No results"}


def get_team(team_id):
    """
    this function converts the team_id from string to BSON, and then returns the team Object from team_collection
    :param team_id:str.
    :return:team Object
    """
    return get_item(team_collection, team_id, TEAM_DOES_NOT_EXIST)


def get_teams(offset, limit):
    return get_items(team_collection, offset, limit)