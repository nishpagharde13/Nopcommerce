# import configparser
# config=configparser.RawConfigParser()
# config.read("..\\Configurations\\config.ini")
#
#
# class ReadConfig:
#     @staticmethod
#     def getApplicationURL():
#         url=config.get('common info','baseURL')
#         return url
#
#     @staticmethod
#     def getUserEmail():
#         username=config.get('common info','username')
#         return  username
#
#     @staticmethod
#     def getPassword():
#         password=config.get('common info','password')
#         return password

import configparser
import os

config = configparser.RawConfigParser()

config_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "Configurations",
    "config.ini"
)

config.read(config_path)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get('common info', 'baseURL')

    @staticmethod
    def getUserEmail():
        return config.get('common info', 'username')

    @staticmethod
    def getPassword():
        return config.get('common info', 'password')
