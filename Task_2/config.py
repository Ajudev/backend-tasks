class Config(object):
    DEBUG = True
    SECRET_KEY = '$iSWeT_!fR!dIs4a#1FEvojADUc?I7'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Test#123@db:3306/orders'
    SQLALCHEMY_TRACK_MODIFICATIONS = False