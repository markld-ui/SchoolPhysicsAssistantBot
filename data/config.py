from opcode import hasconst
from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN") # get token-bot from .env file
ADMINS = env.list("ADMINS") # get id administrator (programmer) from .env file
HOST =  env.str("HOST")
DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")