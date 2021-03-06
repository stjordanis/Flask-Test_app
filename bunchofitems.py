from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from databasesetup import Category, Base, Item

engine = create_engine('sqlite:///ItemCatalog.db')
Base.metadata.bind = engine
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance

DBSession = sessionmaker(bind=engine)
session = DBSession()
"""
A DBSession() instance establishes all conversations with the database
and represents a "staging zone" for all the objects loaded into the
database session object. Any change made against the objects in the
session won't be persisted into the database until you call
session.commit(). If you're not happy about the changes, you can
revert all of them back to the last commit by calling
session.rollback()
"""
categories = ["Soccer", "Basketball", "Baseball", "Frisbee", "Snowboarding", "Rock Climbing", "Foosball", "Skating", "Hockey"]

# Soccer
category = Category(name = categories[0])
item = Item(name = "Shorts", description = "Shorts for running around", category = category)
session.add(item)
session.commit()
item = Item(name = "Soccer-ball", description = "The ball you kick", category = category)
session.add(item)
session.commit()
item = Item(name = "Jersey", description = "Soccer jersey that identifies your team", category = category)
session.add(item)
session.commit()
item = Item(name = "Shoes", description = "The shoes for kicking the ball", category = category)
session.add(item)
session.commit()


# Basketball
category = Category(name = categories[1])
item = Item(name = "Basketball-ball", description = "The ball you shoot hoops with", category = category)
session.add(item)
session.commit()
item = Item(name = "Basketball-jersey", description = "Basketball jersey that identifies your team", category = category)
session.add(item)
session.commit()


# Baseball
category = Category(name = categories[2])
item = Item(name = "Baseball-ball", description = "The ball you hit with the bat", category = category)
session.add(item)
session.commit()
item = Item(name = "Baseball-bat", description = "The bat you hit the ball with", category = category)
session.add(item)
session.commit()
item = Item(name = "Baseball-helmet", description = "Protects your head from the baseball", category = category)
session.add(item)
session.commit()


# Frisbee
category = Category(name = categories[3])
item = Item(name = "Frisbee-disc", description = "The disk you throw when you play frisbee", category = category)
session.add(item)
session.commit()


# Snowboarding
category = Category(name = categories[4])
item = Item(name = "Snowboard", description = "The board you ride on", category = category)
session.add(item)
session.commit()
item = Item(name = "Goggles", description = "The goggles that protect your eyes", category = category)
session.add(item)
session.commit()
item = Item(name = "Coat", description = "The snow is very cold", category = category)
session.add(item)
session.commit()


# Rock Climbing
category = Category(name = categories[5])
item = Item(name = "Rope", description = "Need to attach the hook to this", category = category)
session.add(item)
session.commit()
item = Item(name = "Harness", description = "holds you up when you climb", category = category)
session.add(item)
session.commit()
item = Item(name = "Climbing-Helmet", description = "protect your head from rocks", category = category)
session.add(item)
session.commit()


# Foosball
category = Category(name = categories[6])
item = Item(name = "Foosball-table", description = "The table for foosball", category = category)
session.add(item)
session.commit()
item = Item(name = "Foosball-ball", description = "The ball the little pegs hit", category = category)
session.add(item)
session.commit()


# Skating
category = Category(name = categories[7])
item = Item(name = "Ice-skates", description = "The skates that you skate with", category = category)
session.add(item)
session.commit()


# Hockey
category = Category(name = categories[8])
item = Item(name = "Helmet", description = "Protects you from pucks", category = category)
session.add(item)
session.commit()
item = Item(name = "Hockey-puck", description = "Hit this with the stick", category = category)
session.add(item)
session.commit()
item = Item(name = "Hockey-stick", description = "Hit the puck with this", category = category)
session.add(item)
session.commit()

print "added all items to the catalog."
