from bson.objectid import ObjectId
from bson.json_util import dumps
from tornado import escape

from consts import *


def get_items(item_collection, offset=DEFAULT_STARTING_ROW, limit=DEFAULT_LIMIT):
    """
    This method returns a list of items. Supports paging.
    :param item_collection - collection object
    :param offset - int offset value
    :param limit - int limit value
    """
    item_cursor = item_collection.find().sort("_id", -1).skip(offset).limit(limit)
    item_list = [i for i in item_cursor]
    return escape.json_encode({
        "item_list": escape.json_decode(dumps(item_list)),
        "limit": limit,
        "offset": offset})


def get_item(item_collection, item_id, does_not_exist_error):
    """
    this function casts the item_id from string to BSON, and then returns the team Object from its desirable collection
    :param item_collection - collection Object.
    :param item_id :str of BSON
    :param does_not_exist_error is an error constant,
    :return:item Object or following error.
    """
    item_id = ObjectId(item_id)  # cast from string to BSON
    item = item_collection.find_one({'_id': item_id})
    if item:
        return dumps(item)
    else:
        return {"return_code": does_not_exist_error, "Message": 'Item does not exist!'}
