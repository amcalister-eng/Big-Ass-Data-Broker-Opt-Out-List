from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    anthropic_api_key: str = ""
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "governance123"
    upload_dir: str = "/app/uploads"
    max_upload_mb: int = 50
    claude_model: str = "claude-sonnet-4-6"

    class Config:
        env_file = ".env"


settings = Settings()
