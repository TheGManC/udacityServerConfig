from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///itemcatalogwithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# start fresh
session.query(Category).delete()
session.query(User).delete()
session.query(Item).delete()

# Create dummy user
User1 = User(name="George Lucas", email="gl@lucasxx.com", picture="")
session.add(User1)
session.commit()

# create initial categories
categoryOne = Category(user_id=1, name="Characters")
categoryTwo = Category(user_id=1, name="Weapons")
categoryThree = Category(user_id=1, name="Vehicles")

dummyData = [categoryOne, categoryTwo, categoryThree]

for item in dummyData:
    session.add(categoryOne)
    session.commit()

# create initial items
itemOne = Item(user_id=1, name="Luke Skywalker", description="Dummy Data For Luke Skywalker", category=categoryOne)
itemTwo = Item(user_id=1, name="Kylo Ren", description="Dummy Data for Kylo Ren", category=categoryOne)
itemThree = Item(user_id=1, name="Luke's Lightsaber", description="Dummy Data for Lukes Lightsaber", category=categoryTwo)
itemFour = Item(user_id=1, name="Sand Speeder", description="Dummy Data for Sand Speeder", category=categoryThree)

dummyItems = [itemOne, itemTwo, itemThree, itemFour]

for item in dummyItems:
    session.add(item)
    session.commit()
