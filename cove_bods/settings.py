from cove import settings

PIWIK = settings.PIWIK
GOOGLE_ANALYTICS_ID = settings.GOOGLE_ANALYTICS_ID
MEDIA_ROOT = settings.MEDIA_ROOT
MEDIA_URL = settings.MEDIA_URL
DEALER_TYPE = settings.DEALER_TYPE
SECRET_KEY = settings.SECRET_KEY
DEBUG = settings.DEBUG
ALLOWED_HOSTS = settings.ALLOWED_HOSTS
MIDDLEWARE_CLASSES = settings.MIDDLEWARE_CLASSES
ROOT_URLCONF = settings.ROOT_URLCONF
TEMPLATES = settings.TEMPLATES
WSGI_APPLICATION = settings.WSGI_APPLICATION
DATABASES = settings.DATABASES
LANGUAGE_CODE = settings.LANGUAGE_CODE
TIME_ZONE = settings.TIME_ZONE
USE_I18N = settings.USE_I18N
USE_L10N = settings.USE_L10N
USE_TZ = settings.USE_TZ
STATIC_URL = settings.STATIC_URL
STATIC_ROOT = settings.STATIC_ROOT
LANGUAGES = settings.LANGUAGES
LOCALE_PATHS = settings.LOCALE_PATHS
LOGGING = settings.LOGGING

if getattr(settings, 'RAVEN_CONFIG', None):
    RAVEN_CONFIG = settings.RAVEN_CONFIG

INSTALLED_APPS = settings.INSTALLED_APPS + ('cove_bods', )
WSGI_APPLICATION = 'cove_bods.wsgi.application'
ROOT_URLCONF = 'cove_bods.urls'
COVE_CONFIG = {
    'app_name': 'cove_bods',
    'app_base_template': 'cove_bods/base.html',
    'app_verbose_name': 'Beneficial Ownership Data Quality Tool',
    'app_strapline': 'Convert, Validate, Explore Beneficial Ownership Data',
    'schema_item_name': 'bods-package.json',
    'schema_name': {'entity': 'entity-statement.json', 'person': 'person-statement.json', 'ownership': 'ownership-or-control-statement.json', 'components': 'components.json'},
    'schema_codelists': 'codelists/',
    'schema_host': 'https://raw.githubusercontent.com/openownership/data-standard/schema-beta-2/schema/',
    'schema_version': 0.2,
    'schema_version_choices': None,
    'root_list_path': '/',
    'root_id': '',
    'convert_titles': True,
    'input_methods': ['upload', 'url', 'text'],
    'support_email': 'xxx@openownership.org'
}
