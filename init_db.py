from src.db.database import Base, engine
import src.db.models  # Ensure all models are imported

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)
    print("Database and tables created.")

if __name__ == "__main__":
    create_db_and_tables()