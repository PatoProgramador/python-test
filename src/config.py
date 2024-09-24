from decouple import config


class Config:
    SECRET_KEY = config('SEC_SECRET')


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


appConfig = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
