import eventful

from django.conf import settings

def get_events():
    api = eventful.API(settings.EVENTFUL_API_KEY)
    return api.call('/events/search', l='Dover, NH').get('events').get('event')