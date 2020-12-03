from .models import URL
from django.conf import settings
import secrets, string

def __generate_short_url():
    characters = list(string.ascii_letters + string.digits)
    short_url = ''.join(secrets.choice(characters) for i in range(7))
    return short_url

def create_short_url(url):
    short_url = __generate_short_url()
    m = URL(short_url=short_url, long_url=url)
    m.save()
    return short_url