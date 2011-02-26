
ADMINS = (
    ('Your Name', 'Your E-mail'),
)

MANAGERS = ADMINS

SECRET_KEY = 'abcdefg_this_is_a_secret_key'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'twit',
        'USER': 'twituser',
        'PASSWORD': 'twitpass',
        'HOST': '127.0.0.1',
    }
}

# Twitter oAuth Keys
CONSUMER_KEY = 'Get Consumer Key from Twitter App Registration'
CONSUMER_SECRET = 'Get Consumer Secret from Twitter App Registration Too!'
