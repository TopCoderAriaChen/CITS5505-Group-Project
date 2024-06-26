from datetime import timedelta
import os

class BaseConfig:
  SECRET_KEY = "your secret key"
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  PERMANENT_SESSION_LIFETIME = timedelta(days=7)

  UPLOAD_IMAGE_PATH = os.path.join(os.path.dirname(__file__),"static/images")

  PER_PAGE_COUNT = 10


class DevelopmentConfig(BaseConfig):

  SQLALCHEMY_DATABASE_URI0 = "mysql+pymysql://root:yxccc@@127.0.0.1:3306/CITS5505-Group-Project?charset=utf8mb4"

  SQLALCHEMY_DATABASE_URI0 = "sqlite:////Users/cyxxx/Desktop/CITS5505-Group-Project/db.sqlite"
  SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite"

  MAIL_SERVER = "smtp.163.com"
  MAIL_USE_SSL = True
  MAIL_PORT = 465
  MAIL_USERNAME = "hynever@163.com"
  MAIL_PASSWORD = "1111111111111"
  MAIL_DEFAULT_SENDER = "hynever@163.com"

  # redis
  CACHE_TYPE = "RedisCache"
  CACHE_REDIS_HOST = "127.0.0.1"
  CACHE_REDIS_PORT = 6379

  # Celery
  # redis://:password@hostname:port/db_number
  CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
  CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"

  AVATARS_SAVE_PATH = os.path.join(BaseConfig.UPLOAD_IMAGE_PATH,"avatars")



class TestingConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI0 = "mysql+pymysql://[user]:[pass]@[IP]:[port]/CITS5505-Group-Project?charset=utf8mb4"


class ProductionConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI0 = "mysql+pymysql://bbs:Bbs#hwygl123@127.0.0.1:3306/CITS5505-Group-Project?charset=utf8mb4"
