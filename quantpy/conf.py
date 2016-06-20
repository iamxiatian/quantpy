import configparser

cfg = configparser.ConfigParser()

cfg.read('settings.cfg')

MONGODB_DB_NAME = cfg['db']['dbname']
MONGODB_USER_NAME = cfg['db']['user']
MONGODB_PASSWORD = cfg['db']['password']
MONGODB_HOST = cfg['db']['host']
MONGODB_PORT = int(cfg['db']['port'])
