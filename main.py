#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, Table

Base = declarative_base()

user_event = Table(
    'user_event',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('event_id', ForeignKey('events.id'), primary_key=True),
)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    events = relationship("Event", secondary=user_event, back_populates='users')
    reviews = relationship("Review", back_populates='user')

    def __repr__(self):
        return f"User {self.name}, is having an id of {self.id}"

class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer(), primary_key=True)
    name = Column(String())
    location = Column(String())
    users = relationship("User", secondary=user_event, back_populates='events')
    reviews = relationship("Review", back_populates='event')

    def __repr__(self):
        return f"Event is {self.name}, it will be held at {self.location}"

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer(), primary_key=True)
    score = Column(Integer())
    user_id = Column(Integer(), ForeignKey("users.id"))
    event_id = Column(Integer(), ForeignKey("events.id"))

    user = relationship("User", back_populates='reviews')
    event = relationship("Event", back_populates='reviews')

    def __repr__(self):
        return f"Your review {self.score}"

if __name__ == "__main__":
    engine = create_engine('sqlite:///my_database.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # eventA = Event(
    #     name="Music",
    #     location="Nairobi garage"
    # )
    # eventB = Event(
    #     name="Movie Awards",
    #     location="Galleria"
    # )

    # session.bulk_save_objects([eventA, eventB])
    # session.commit()



