from dbUtils.db import *
from consts import *
from bson.json_util import dumps
from dbUtils.commonDbUtils import get_item, get_items


def create_league(league_country: str, league_name: str, league_level: int):
    """
    This function gets league_country, league_name and league_level in JSON format, checks if there exists a league in
    the DB and if not creates a new league
    :param league_country: string
    :param league_name: string
    :param league_level:string
    :return: JSON that includes the league if created or an Error message
    """
    if not isinstance(league_country, str) or not isinstance(league_name, str) or not isinstance(league_level, int):
        return {"return_code": INVALID_FIELDS,
                "Message": 'League country, league name and league level has to be string and league level'
                           'has to be int(from 0 as top and 1 for each level, (example : third league - 2)'}

    league = {"league_country": league_country,
              "league_name": league_name,
              "league_level": league_level,
              }
    if league_collection.find_one({"league_name": league_name}) is None:
        try:
            league_collection.insert_one(league)
            return dumps(league)
        except Exception as e:
            return {"return_code": UNKNOWN_EXCEPTION, "Message": 'Exception while inserting league', 'Error': str(e)}
    else:
        return {"return_code": LEAGUE_ALREADY_EXIST, "Message": 'League Already exist!'}


def get_league(league_id):
    """
        this function converts the team_id from string to BSON, and then returns the team Object from team_collection
    :param league_id :str.
    :return:league Object
    """
    return get_item(league_collection, league_id, LEAGUE_DOES_NOT_EXIST)


def get_leagues(offset, limit):
    return get_items(league_collection, offset, limit)
