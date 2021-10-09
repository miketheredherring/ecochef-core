import environ

# Default configuration for environ
env = environ.Env(
    DEBUG=(bool, False)
)

# Fetch from the environment file
environ.Env.read_env()

# General
DEBUG = env('DEBUG')

# Database
DATABASE_USER = env('DATABASE_USER')
DATABASE_PASSWORD = env('DATABASE_PASSWORD')
DATABASE_HOST = env('DATABASE_HOST')
