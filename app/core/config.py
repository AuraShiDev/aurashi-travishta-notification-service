from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    APP_ENV: str = "dev"
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    REDIS_URL: str = "redis://localhost:6379/0"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    ANONYMOUS_TOKEN_EXPIRE_MINUTES: int = 60
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


Config = Settings()


broker_url = Config.REDIS_URL
broker_connection_retry_on_startup = True