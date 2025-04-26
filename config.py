import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "29557383"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "c712dbb98445b40fa2745b439a43c06a")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", ""))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://comadyt:7qRP0rRvmZBdqJ9P@cluster0.iu2ko1l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
