from .helpers import env

class Config(object):
    DEBUG = env("DEBUG", cast=bool)

    # SQLALCHEMY_POOL_SIZE = env("SQLALCHEMY_POOL_SIZE", cast=int)
    # SQLALCHEMY_MAX_OVERFLOW = env("SQLALCHEMY_MAX_OVERFLOW", cast=int)

    # database
    SQLALCHEMY_DATABASE_URI = env("SQLALCHEMY_DATABASE_URI", cast=str)