CSRF_ENABLED = True
SECRET_KEY = "ahDaeb5a rohGair3 emohCh7j Phie8mop aceic3AF Meixu8iv Si4eiMie cei2Eoyu"
SQLALCHEMY_DATABASE_URI = 'sqlite:///howmush.db'

try:
    from config_dev import *
except:
    pass