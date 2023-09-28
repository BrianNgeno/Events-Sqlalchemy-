from faker import Faker
from main import User
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

Base =  declarative_base()
engine = create_engine('sqlite:///my_database.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

print("seeding user data")

fake = Faker()
users = [
    User(
        name=fake.name()
    )
    for i in range(10)
]


session.bulk_save_objects(users)
session.commit()