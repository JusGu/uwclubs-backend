from django.http import HttpRequest, HttpResponse, JsonResponse
from uwclubs_backend.database.methods import select_events
from django.views.decorators.http import require_http_methods
from ics import Calendar, Event
from datetime import datetime

@require_http_methods(["GET"])
def get_calendar(request: HttpRequest):
    guild_id = request.GET.get('guild_id')
    if not guild_id:
        return JsonResponse({"error": "Guild ID cannot be empty"}, status=400)
    events_data = select_events(guild_id)
    events = events_data.data

    c = Calendar()

    for event in events:
        start_time = datetime.fromisoformat(event["start_time"])
        end_time = datetime.fromisoformat(event["end_time"]) if event.get("end_time") else None

        if end_time and end_time <= start_time:
            continue

        e = Event()
        e.name = event["title"]
        e.begin = start_time
        e.end = end_time if end_time else start_time
        e.description = event["description"]
        e.location = event["location"]
        c.events.add(e)

    calendar_str = c.serialize()

    response = HttpResponse(calendar_str, content_type='text/calendar')
    response['Content-Disposition'] = 'attachment; filename="events.ics"'

    return response