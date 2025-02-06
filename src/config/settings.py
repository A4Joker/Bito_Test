from decouple import config

class Config:
    DATABASE_URL = config('DATABASE_URL', default='postgresql://localhost/db')
    API_KEY = config('API_KEY')
    CACHE_TTL = config('CACHE_TTL', default=3600, cast=int)

    @classmethod
    def get_database_url(cls) -> str:
        return cls.DATABASE_URL

    @classmethod
    def get_api_key(cls) -> str:
        return cls.API_KEY

    @classmethod
    def get_cache_ttl(cls) -> int:
        return cls.CACHE_TTL