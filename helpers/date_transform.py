import datetime

DEFAULT_FORMAT = "%Y-%m-%d %H:%M:%S"


def datetimeSerializer(o, format=DEFAULT_FORMAT):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.strftime(format)
