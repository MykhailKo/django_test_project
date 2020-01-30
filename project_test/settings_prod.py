DEBUG = False
ALLOWED_HOSTS = ['*']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db1',
        'USER': 'django_psg',
        'PASSWORD': 'django_psg1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')