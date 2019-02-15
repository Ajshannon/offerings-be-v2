import os
from .common import Common
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Production(Common):
    INSTALLED_APPS = Common.INSTALLED_APPS
    SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
    # Site
    # https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["52.14.135.120"]
    INSTALLED_APPS += ("gunicorn", )
    STATIC_ROOT = "/home/ec2-user/offerings-be-v2/static"
    STATICFILES_DIRS = (os.path.join(BASE_DIR, "static/"),)

        # Postgres
    DATABASES = {
	    'default': {
    		'ENGINE': 'django.db.backends.postgresql',
    		'NAME': 'offerings',
    		'USER': 'offerings',
    		'PASSWORD': 'LetsDoThis2018',
    		'HOST': 'offerings.ccdjwdmacumw.us-east-2.rds.amazonaws.com',
    		'PORT': '5432',
        }
    }

    DEBUG = True
    
    AWS_HEADERS = {
        'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
    }
