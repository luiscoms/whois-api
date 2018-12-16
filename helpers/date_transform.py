import datetime

DEFAULT_FORMAT = "%a, %d %b %Y %H:%M:%S GMT"


def datetimeSerializer(o, format=DEFAULT_FORMAT):
    if type(o) is datetime.date or type(o) is datetime.datetime:
        return o.strftime(format)
