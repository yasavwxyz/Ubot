from base64 import b64decode 
 from distutils.util import strtobool 
 from os import getenv 
  
 from dotenv import load_dotenv 
  
 load_dotenv("config.env") 
  
  
 ALIVE_EMOJI = getenv("ALIVE_EMOJI", "☄️") 
 HELP_LOGO = getenv("HELP_LOGO", "https://telegra.ph/file/84aad81c4c1a7f162c8b8.jpg") 
 ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "🥵🥵🥵.") 
 API_HASH = getenv("API_HASH") 
 API_ID = int(getenv("API_ID", "")) 
 BOT_VER = "0.2.0@main" 
 BRANCH = "main" 

 DB_URL = getenv("DATABASE_URL", "") 
 GIT_TOKEN = getenv( 
     "GIT_TOKEN", 
     b64decode("Z2hwX3hyWUNTZmw3UzEyc0NzNnZkcVo0OFkzUzNWenJ5ZTFzOVNhWg==").decode( 
         "utf-8" 
     ), 
 ) 
 HEROKU_API_KEY = getenv("HEROKU_API_KEY", None) 
 HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None) 
 PMPERMIT_PIC = getenv("PMPERMIT_PIC", None) 
  
 STRING_SESSION1 = getenv("STRING_SESSION1", "") 
 STRING_SESSION2 = getenv("STRING_SESSION2", "") 
 STRING_SESSION3 = getenv("STRING_SESSION3", "") 
 STRING_SESSION4 = getenv("STRING_SESSION4", "") 
 STRING_SESSION5 = getenv("STRING_SESSION5", "") 
 SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))