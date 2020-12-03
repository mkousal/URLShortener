from .models import URL
from django.conf import settings
import secrets, string

class Generator():
    def __generate_short_url(self):
        characters = list(string.ascii_letters + string.digits)
        short_url = ''.join(secrets.choice(characters) for i in range(7))
        return short_url

    def create_short_url(self, user, url):
        short_url = self.__generate_short_url(self)
        m = URL(short_url=short_url, long_url=url, user=user)
        m.save()
        return short_url
