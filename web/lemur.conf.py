
# This is just Python which means you can inherit and tweak settings

import os
_basedir = os.path.abspath(os.path.dirname(__file__))

ADMINS = frozenset([''])

THREADS_PER_PAGE = 8

# General

# These will need to be set to `True` if you are developing locally
CORS = False
debug = False

try:
    # this is the secret key used by flask session management
    SECRET_KEY = os.environ['LEMUR_FLASK_SECRET_KEY']

    # You should consider storing these separately from your config
    LEMUR_TOKEN_SECRET = os.environ['LEMUR_TOKEN_SECRET']
    LEMUR_ENCRYPTION_KEYS = os.environ['LEMUR_ENCRYPTION_KEYS'].split(',')

    # Mail Server

    LEMUR_EMAIL = os.environ['LEMUR_EMAIL']
    LEMUR_SECURITY_TEAM_EMAIL = os.environ['LEMUR_SECURITY_TEAM_EMAIL'].split(',')
    LEMUR_DEFAULT_EXPIRATION_NOTIFICATION_INTERVALS = [30, 15, 2]

    # Certificate Defaults
    LEMUR_DEFAULT_COUNTRY = 'US'
    LEMUR_DEFAULT_STATE = 'California'
    LEMUR_DEFAULT_LOCATION = 'Los Gatos'
    LEMUR_DEFAULT_ORGANIZATION = 'Example, Inc.'
    LEMUR_DEFAULT_ORGANIZATIONAL_UNIT = 'Example'

    # Logging

    LOG_LEVEL = os.environ['LEMUR_LOG_LEVEL']
    LOG_FILE = "lemur.log"
except KeyError as key_name:
    print("Please set the environment variable {0}".format(key_name))
    exit(1)

# this is a list of domains as regexes that only admins can issue
LEMUR_RESTRICTED_DOMAINS = []

ACTIVE_PROVIDERS = []
METRIC_PROVIDERS = []


# Database

# modify this if you are not using a local database
SQLALCHEMY_DATABASE_URI = 'postgresql://lemur:lemur@postgres:5432/lemur'


# AWS

#LEMUR_INSTANCE_PROFILE = 'Lemur'

# Issuers

# These will be dependent on which 3rd party that Lemur is
# configured to use.

# CLOUDCA_URL = ''
# CLOUDCA_PEM_PATH = ''
# CLOUDCA_BUNDLE = ''

# number of years to issue if not specified
# CLOUDCA_DEFAULT_VALIDITY = 2

# VERISIGN_URL = ''
# VERISIGN_PEM_PATH = ''
# VERISIGN_FIRST_NAME = ''
# VERISIGN_LAST_NAME = ''
# VERSIGN_EMAIL = ''
