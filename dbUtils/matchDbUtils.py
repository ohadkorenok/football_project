from dbUtils.db import match_collection, team_collection, league_collection
from dbUtils.commonDbUtils import get_item, get_items
from bson.objectid import ObjectId
from bson.json_util import dumps
from consts import *


def create_match(league_id: str, home_team: str, away_team: str, home_goals: int,
                 away_goals: int):
    """
    This function Inserts a match to the match collection.
    :param league_id:  - String that has 24 Letters .
    :param home_team: string
    :param away_team: string
    :param home_goals : int
    :param away_goals: int
    :return: JSON Return codes or match_collection document that represents the inserted match
    """
    try:
        league = league_collection.find_one({
            "_id": ObjectId(league_id)
        })

        if league is None:
            return {"return_code": LEAGUE_DOES_NOT_EXIST,
                    "Message": 'There is no such league! cannot add a team without a league'}
        team_dict = {}
        teams_from_db = team_collection.find({'team_name': {"$in": [home_team, away_team]}}, limit=2)

        if teams_from_db is None:
            return {"return_code": TEAM_ALREADY_EXIST, "Message": "There is already a team in this name in the"
                                                                  "system Cannot enter to DB"}

        for team in teams_from_db:
            if home_team == team['team_name']:
                team_dict['home_team'] = team
                team['goals'] = home_goals
                team['winner'] = 1 if home_goals > away_goals else 0  # in case of draw both 0
            elif away_team == team['team_name']:
                team_dict['away_team'] = team
                team['goals'] = away_goals
                team['winner'] = 1 if away_goals > home_goals else 0  # in case of draw both 0

        if len(team_dict.keys()) < 2:
            return {"return_code": TEAM_DOES_NOT_EXIST,
                    "Message": "Could not find all of the teams in the game. Check if you have spelled correctly."}
        match = {
            'league_id': league_id,
            'home_team': home_team,
            'away_team': away_team,
            'home_goals': home_goals,
            'away_goals': away_goals,
        }
        match_collection.insert(match)
        for key in team_dict.keys():
            team_collection.update_one({"_id": team_dict[key]['_id']},
                                       {'$inc': {'wins': team_dict[key]['winner'], 'goals': team_dict[key]['goals']}})
        return dumps(match)
    except Exception as e:
        return {"return_code": UNKNOWN_EXCEPTION, "Message": 'Exception while creating a match', 'Error': str(e)}


def get_match(match_id):
    """
    this function converts the match_id from string to BSON, and then returns the match Object from match_collection
    :param match_id :str.
    :return:match Object
    """
    return get_item(match_collection, match_id, MATCH_DOES_NOT_EXIST)


def get_matches(offset, limit):
    return get_items(match_collection, offset, limit)
