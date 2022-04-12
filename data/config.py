from environs import Env

env = Env()
env.read_env()

TOKEN = env.str("TOKEN") # get token-bot from .env file
ADMINS = env.list("ADMINS") # get id administrator (programmer) from .env file