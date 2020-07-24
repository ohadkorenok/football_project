__author__ = 'ohad koren'

from consts import *
from tornado import escape
import json


def request_validation_decorator(func):
    """
    This function gets a post function and checks if the self.body is empty.
    If so, it returns a JSON error. if not, it returns a new function - "wrapper" that actually runs the function.
    :param func: POST function.
    :return: JSON error/decorated function
    """

    def wrapper(*arg):
        request = arg[0]
        if request.request.body == '':
            request.write(escape.json_encode({"return_code": BAD_PARAMETERS_ERROR, "Message": 'EmptyBody'}))
        else:
            func(*arg)

    return wrapper


def create_league_validation_decorator(func):
    '''
    Verify that the HTTP Request has league_country, league_name, league_level  keys
    :param func: POST function
    :return: JSON error/decorated function
    '''

    def wrapper(*arg):
        request = arg[0]
        data = json.loads(request.request.body)
        if "league_country" in data and "league_name" in data and "league_level" in data:
            func(*arg)
        else:
            request.write(escape.json_encode({"return_code": BAD_PARAMETERS_ERROR,
                                              "Message": 'Bad Parameters : league_country ,league_name, league_level'}))

    return wrapper


def create_team_validation_decorator(func):
    '''
    Verify that the HTTP Request has league_id, team_name, team_city  keys
    :param func: POST function
    :return: JSON error/decorated function
    '''

    def wrapper(*arg):
        request = arg[0]
        data = json.loads(request.request.body)
        if "league_id" in data and "team_name" in data and "team_city" in data:
            func(*arg)
        else:
            request.write(escape.json_encode({"return_code": BAD_PARAMETERS_ERROR,
                                              "Message": 'Bad Parameters : league_id ,team_name, team_city'}))

    return wrapper


def create_match_validation_decorator(func):
    '''
    Verify that the HTTP Request has league_id, home_team,away_team home_goals, away_goals  keys
    :param func: POST function
    :return: JSON error/decorated function
    '''

    def wrapper(*arg):
        request = arg[0]
        data = json.loads(request.request.body)
        if "league_id" in data and "home_team" in data and "away_team" in data and "home_goals" in data and \
                "away_goals" in data:
            func(*arg)
        else:
            request.write(escape.json_encode({"return_code": BAD_PARAMETERS_ERROR,
                                              "Message": 'Bad Parameters : league_id ,team_name, team_city'}))

    return wrapper
