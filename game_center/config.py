from .helpers import env


class Config(object):
    DEBUG = env("DEBUG", cast=bool)

    # SQLALCHEMY_POOL_SIZE = env("SQLALCHEMY_POOL_SIZE", cast=int)
    # SQLALCHEMY_MAX_OVERFLOW = env("SQLALCHEMY_MAX_OVERFLOW", cast=int)

    # database
    DEBUG = True
    # env("SQLALCHEMY_DATABASE_URI", cast=str)
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:ruc@10.77.70.167:3316/theglovesdev?charset=utf8"
