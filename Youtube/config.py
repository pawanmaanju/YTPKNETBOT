import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7505434122:AAF6BfyngeU-yyiRuBgI7GEJvf22ihQooQo")
    API_ID = int(os.environ.get("API_ID",21174134 ))
    API_HASH = os.environ.get("API_HASH", "3d7f8c4ee4978228f411bbd04f2eea73")
    #Add your channel id. For force Subscribe.
    CHANNEL = os.environ.get("CHANNEL", "")
    #Skip or add your proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = ''
