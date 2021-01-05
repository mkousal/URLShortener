from .models import URL
from django.conf import settings
import secrets, string

def generate_short_url():
    characters = list(string.ascii_letters + string.digits)
    while True:
        short_url = ''.join(secrets.choice(characters) for i in range(7))
        if not URL.objects.filter(short_url=short_url).exists():
            break
    return short_url