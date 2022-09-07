from base64 import b64decode 
 from distutils.util import strtobool 
 from os import getenv 
  
 from dotenv import load_dotenv 
  
 load_dotenv("config.env") 
  
  
 ALIVE_EMOJI = getenv("ALIVE_EMOJI", "☄️") 
 ALIVE_TEKS_CUSTOM = getenv("ALIVE_TEKS_CUSTOM", "🥵🥵🥵.") 
 API_HASH = getenv("333f70291772d39d8bd4c246e4feb3fc") 
 API_ID = int(getenv("12557329", "")) 
 BOT_VER = "0.2.0@main" 
 BRANCH = "main" 

 DB_URL = getenv("DATABASE_URL", "mongodb+srv://nekomaru:nekomaru24@cluster0.uv6mq1k.mongodb.net/?retryWrites=true&w=majority") 
 GIT_TOKEN = getenv( 
     "GIT_TOKEN", 
     b64decode("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==").decode( 
         "utf-8" 
     ), 
 ) 
 HEROKU_API_KEY = getenv("9e517a08-f592-4779-ae45-55cdf212be72") 
 HEROKU_APP_NAME = getenv("MarryCrush") 
 PMPERMIT_PIC = getenv("PMPERMIT_PIC", None) 
  
 STRING_SESSION1 = getenv("STRING_SESSION1", "BQAhIHQAR1Y-nRd5h-aSTa-IzMTee0KECsUNMjWj5MgOczgOxVB9hl9GYMHaioPw9qB5zgkHAUlmitRui7l1E-hObISC1db1sapF1JdbRdV_cEzsqGZsI95FmTY7ot3s51VmVevu-h-VA8WJt001O-sg1lM2ZW_o3bfR3JiwvZgRLEg13Rbv_1u97Kzc_MjjuSsYgtk0qd7o3T7f4qy8CWejfcylFhn_i-WK6tXGcYTaBwUWILjEnQGrv_D_qOMulW5e77oZkvV_EWGa5HmUgYFiyexet0S7fP_kv4NU7TdwkjTlpZjAlX4EqE3pVvECVVW84VTZn-L1FWSVDqWYuBjBjLm2PQAAAAEzZyIlAA") 
 STRING_SESSION2 = getenv("STRING_SESSION2", "") 
 STRING_SESSION3 = getenv("STRING_SESSION3", "") 
 STRING_SESSION4 = getenv("STRING_SESSION4", "") 
 STRING_SESSION5 = getenv("STRING_SESSION5", "") 
 SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
