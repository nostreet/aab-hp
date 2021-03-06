from event.models import Event
import datetime
from django.utils.timezone import utc
#includes all events from the db to the event_list.html as sidebar for main.html

def globs(request):
    events = Event.objects.all().order_by('event_date')
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    return {'event_li': events, 'time_now':now}
