# -*- coding: utf-8 -*-
# Django settings for Roboconf.
import os
import datetime

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('SITCON Administrators', 'sitcon-admin@googlegroups.com'),
)

MANAGERS = ADMINS

PROJECT_PATH = '/'.join(os.path.dirname(os.path.abspath(__file__)).split('/')[0:-2])

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_PATH, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

LOGIN_URL = 'users:login'
ALLOWED_HOSTS = ['*']

TIME_ZONE = 'Asia/Taipei'
LANGUAGE_CODE = 'zh-tw'

SITE_ID = 1
USE_I18N = True    # TODO: Implement internationalization
USE_L10N = True
USE_TZ = True

SECRET_KEY = 'roboconf'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = ()

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'
WSGI_APPLICATION = 'core.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'core',
    'users',
    'docs',
    'issues',
    'agenda',
    'notifications',
    'submission',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'filename': '/var/log/roboconf.log',
            'class': 'logging.FileHandler'
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

EMAIL_HOST = ''
EMAIL_PORT = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'Roboconf <roboconf@example.org>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DEFAULT_NOTIFICATION_SENDER = 'Roboconf:roboconf@example.org'
DEFAULT_ACCOUNTS_SENDER = DEFAULT_NOTIFICATION_SENDER
DEFAULT_ISSUE_SENDER = DEFAULT_NOTIFICATION_SENDER

SUBMITTER_ACCOUNTS_SENDER = DEFAULT_ACCOUNTS_SENDER
USER_ISSUE_SENDER = DEFAULT_ISSUE_SENDER

SMS_API_KEY = ''
SMS_API_SECRET = ''
DEFAULT_SMS_SENDER = 'ROBOCONF'
DEFAULT_SMS_COUNTRY_CODE = '886'    # Taiwan

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SUBMISSION_START = datetime.datetime.min
SUBMISSION_END = datetime.datetime.max
SUBMISSION_RULE_DOCID = ''

ISSUE_EXPIRE_TIMEDELTA = datetime.timedelta(hours=12)