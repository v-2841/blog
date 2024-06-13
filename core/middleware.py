import os

import IP2Location
from django.conf import settings
from django.shortcuts import redirect

from core.utils import get_client_ip, TZ_OFFSET_TO_NAME


class CookieTimeZoneCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not (request.COOKIES.get('timezone')
                and request.COOKIES.get('ip') == get_client_ip(request)):
            response = redirect(request.get_full_path())
            return self.process_response(request, response)
        response = self.get_response(request)
        return response

    def process_response(self, request, response):
        database = IP2Location.IP2Location(os.path.join(
            settings.BASE_DIR, "ip_db", "IP2LOCATION-LITE-DB11.IPV6.BIN"))
        try:
            ip = get_client_ip(request)
            offset = database.get_timezone(ip)
        except Exception:
            ip = '127.0.0.1'
            offset = '+00:00'
        try:
            timezone = TZ_OFFSET_TO_NAME[offset]
        except Exception:
            timezone = 'Etc/GMT'
        max_age = 60 * 60 * 24 * 30  # 30 days
        response.set_cookie('timezone', timezone, max_age)
        response.set_cookie('ip', ip, max_age)
        return response
