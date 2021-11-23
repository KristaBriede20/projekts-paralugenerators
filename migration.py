import sqlite3
import configparser
from sqlite3.dbapi2 import Cursor
import logger
import logging
import yaml
import logging.config

from sqlite3 import Error
from configparser import ConfigParser

with open(r"./conf_migration.yaml") as stream:  
    config = yaml.safe_load(stream)

logging.config.dictConfig(config)
logger = logging.getLogger('root')

logger.info('Migration started')

try:
    logger.info('Getting migrations...')
    config = configparser.ConfigParser()
    config.read('config.ini')

    migration =config.get('database', 'create_query')
except:
    logger.error('Error')
logger.info('Done')

connection = sqlite3.connect(r'database/database.db')
logger.info('Connected to database')
cursor = connection.cursor()

cursor.execute(migration)
connection.commit()
logger.info('Migrations successful')
