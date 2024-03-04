from django.contrib import admin
from django.http import JsonResponse, HttpRequest
from django.urls import path
from django.views.decorators.http import require_http_methods
import json

from uwclubs_backend.calendar.endpoint import get_calendar
from .consts.env import is_dev, is_prod
from django.middleware.csrf import get_token
from uwclubs_backend.database.methods import select_events


def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

# Health Check Endpoint
@require_http_methods(["GET"])
def health(request):
    env = "local"
    if is_prod():
        env = "prod"
    if is_dev():
        env = "dev"
    return JsonResponse({"data": "ok", "env": env})

# Search Endpoint
@require_http_methods(["POST"])
def search(request: HttpRequest):
    try:
        query = json.loads(request.body).get("query")
        if not query:
            return JsonResponse({"error": "Query cannot be empty"}, status=400)
        return JsonResponse({"query": query})
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", health, name="health"),
    path("search/", search, name="search"),
    path("calendar/", get_calendar, name="calendar"),
    path('csrf/', csrf, name='csrf'),
]