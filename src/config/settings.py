from decouple import config

class Config:
    def __init__(self):
        self.DATABASE_URL = config('DATABASE_URL', 
                                 default='postgresql://localhost/db')
        self.API_KEY = config('API_KEY', 
                             default='development-key')
        self.CACHE_TTL = config('CACHE_TTL', 
                               default=3600, cast=int)