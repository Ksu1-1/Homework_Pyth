from sqlalchemy import create_engine

CONNECTION_STRING = (
    "postgresql+psycopg2://"
    "postgres:rctybz@"
    "localhost:5432/"
    "postgres"
)

db = create_engine(CONNECTION_STRING)
