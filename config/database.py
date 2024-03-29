"""Database Settings."""

import logging

from masonite import env
from masonite.environment import LoadEnvironment
from masoniteorm.connections import ConnectionResolver

"""Load Environment Variables
Loads in the environment variables when this page is imported.
"""

LoadEnvironment()

"""Database Settings
Set connection database settings here as a dictionary. Follow the
format below to create additional connection settings.

Each key is a connection, not a driver. You may have as many
connections as you need.

Supported Drivers: 'sqlite', 'mysql', 'postgres'
"""

DATABASES = {
    'default': env('DB_CONNECTION'),
    'sqlite': {
        'driver': 'sqlite',
        'database': env('DB_DATABASE'),
        'log_queries': env('DB_LOG'),
    },
    'mysql': {
        'driver': 'mysql',
        'host': env('DB_HOST'),
        'database': env('DB_DATABASE'),
        'port': env('DB_PORT'),
        'user': env('DB_USERNAME'),
        'password': env('DB_PASSWORD'),
        'log_queries': env('DB_LOG'),
    },
    'postgres': {
        'driver': 'postgres',
        'host': env('DB_HOST'),
        'database': env('DB_DATABASE'),
        'port': env('DB_PORT'),
        'user': env('DB_USERNAME'),
        'password': env('DB_PASSWORD'),
        'log_queries': env('DB_LOG'),
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)


logger = logging.getLogger('orator.connection.queries')
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    'It took %(elapsed_time)sms to execute the query %(query)s'
)

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger.addHandler(handler)
