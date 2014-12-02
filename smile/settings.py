# Django settings for alwefaq project.
import os

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__).decode('utf-8')).replace('\\', '/')

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
# ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add '', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'smile', # os.path.join(CURRENT_PATH, 'wefaqdb'), # Or path to database file if using sqlite3.
    }
}
# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Riyadh'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ar'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = False

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(CURRENT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'


# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
# STATIC_ROOT = os.path.join(CURRENT_PATH, 'static')
# print STATIC_ROOT
# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(CURRENT_PATH, 'static'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'd^3tdy11@k5(lv1mo*aok1fokov@52r&2moteo9e0a!wjd=-a+'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'common.middleware.ForceLangMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'smile.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'alwefaq.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(CURRENT_PATH, 'templates')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'raven.contrib.django.raven_compat',
    'import_export',
    'common',
    'news',
    'vehicles',
    'offers',
    'booking',
    'locations',
    'amyali',
    'tinymce',
    'marketing',
    'tastypie',
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# AUTH_USER_MODEL = 'common.User'
# ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.


from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.i18n',
    'django.core.context_processors.request'
)

LOCALE_PATHS = (
    os.path.join(CURRENT_PATH, 'locale'),
    os.path.join(CURRENT_PATH, '../amyali/locale'),
    os.path.join(CURRENT_PATH, '../booking/locale'),
    os.path.join(CURRENT_PATH, '../common/locale'),
    os.path.join(CURRENT_PATH, '../locations/locale'),
    os.path.join(CURRENT_PATH, '../news/locale'),
    os.path.join(CURRENT_PATH, '../offers/locale'),
    os.path.join(CURRENT_PATH, '../vehicles/locale'),
)

ugettext = lambda s: s

LANGUAGES = (
    ('ar', ugettext('Arabic')),
    ('en', ugettext('English')),

)

LANGUAGE_CODE = 'ar'

# Mandrill login username and password (only lower case)
# Username = abdallah_n@hotmail.com
# Password = swapalwefaqmandrill123

#Mandrill SMTP & API Credentials
# Host = smtp.mandrillapp.com
# Port = 587
# SMTP Username = abdallah_n@hotmail.com
# SMTP Password = B1JDr56hhPBprctLXa7iQw
# ** SMTP password is any API key for this account ** #

AUTH_USER_MODEL = 'common.Guest'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.mailgun.org'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'postmaster@alwefaq.com'
# EMAIL_HOST_PASSWORD = '3zneu50tkk10'
# EMAIL_USE_TLS = True
EMAIL_USE_TLS = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'yazan.alhorani@gmail.com'
DEFAULT_FROM_EMAIL = 'yazan.alhorani@gmail.com'
SERVER_EMAIL = 'yazan.alhorani@gmail.com'

EMAIL_HOST_PASSWORD = 'P@ssword_'

EMAIL_PORT = 587

EMAIL_BASE_URL = 'http://localhost:9001'

LOGIN_URL = '/login'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# EJAR_SERVER_URL = "http://212.102.29.218/eJarIntegration/api/"
EJAR_SERVER_URL = "http://212.102.29.222/eJarIntegration/api/" #Production

# RAVEN_CONFIG = {
#     'dsn': 'http://73c7d1e58eec44eeafb23f07a0b926ca:07f1d0e9fb774513ad9cdaf2e29fc266@sitdev-sentry.cloudapp.net/3',
# }