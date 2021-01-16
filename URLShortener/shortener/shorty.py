from .models import URL
from django.conf import settings
import secrets, string

def generate_short_url():   # function for generating short URL
    characters = list(string.ascii_letters + string.digits) # get all possible characters for generation (small and big letters and digits)
    while True:
        short_url = ''.join(secrets.choice(characters) for i in range(7))   # generate link of length 7
        if not URL.objects.filter(short_url=short_url).exists():    # check DB for duplicate entries
            break
    return short_url