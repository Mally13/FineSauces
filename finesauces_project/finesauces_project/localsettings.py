# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-m290d!q6b265rpy0+^k$&n1objl0#n^%@@==@=42@isybx==3'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'finesauces',
        'USER': 'finesaucesadmin',
        'PASSWORD': '********',
        'HOST': 'localhost'
    }
}
