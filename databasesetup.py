#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys
import datetime
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey
from sqlalchemy import Boolean, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func



Base = declarative_base()


class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	items = relationship("Item", back_populates = 'category')

	@property
	def serialize(self):
		# Return object data in easily serializeable format
		return {
			'id': self.id,
			'name': self.name,
		}

	@property
	def itemsInCategory(self):
		# Return item count per category
		return len(self.items)


class Item(Base):
	__tablename__ = 'category_item'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	description = Column(String(250))
	created = Column(DateTime, default = datetime.datetime.now())
	cat_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category, cascade = 'save-update, merge, delete')


	@property
	def serialize(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'cat_id': self.cat_id,
			'created': self.created
		}


engine = create_engine('sqlite:///ItemCatalog.db')
Base.metadata.create_all(engine)