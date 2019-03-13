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

<<<<<<< HEAD
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    # http://django-storages.readthedocs.org/en/latest/index.html
   # INSTALLED_APPS += ('storages',)
    #DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    #STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    #AWS_ACCESS_KEY_ID = os.getenv('DJANGO_AWS_ACCESS_KEY_ID')
    #AWS_SECRET_ACCESS_KEY = os.getenv('DJANGO_AWS_SECRET_ACCESS_KEY')
    #AWS_STORAGE_BUCKET_NAME = os.getenv('DJANGO_AWS_STORAGE_BUCKET_NAME')
    #AWS_DEFAULT_ACL = 'public-read'
    #AWS_AUTO_CREATE_BUCKET = True
    #AWS_QUERYSTRING_AUTH = False
    #MEDIA_URL = f'https://s3.amazonaws.com/{AWS_STORAGE_BUCKET_NAME}/'
=======
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
>>>>>>> d861476afbf8b259a06147c6e2493aae8b3dbc3b

    DEBUG = True
    
    AWS_HEADERS = {
        'Cache-Control': 'max-age=86400, s-maxage=86400, must-revalidate',
    }
