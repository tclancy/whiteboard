import eventful

from django.conf import settings

def get_events():
    """
    Docs: https://api.eventful.com/docs/events/search
    Need to sort by date and then show some actual details
    """
    api = eventful.API(settings.EVENTFUL_API_KEY)
    return api.call('/events/search', l='Dover, NH').get('events').get('event')