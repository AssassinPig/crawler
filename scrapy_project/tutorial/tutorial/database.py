from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://assassinpig:123456@localhost/tutorial')
Base = declarative_base()
Base.metadata.bind = engine
class Database:
    def saveData(self, item):
        global engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        for i,t in enumerate(item['title']):
            entity = DomzEntity(title = t,
                                link = item['link'][i],
                                desc = item['desc'][i])
            session.add(entity)
        session.commit()

class DomzEntity(Base):
    __tablename__ = 'dmozentity'
    id = Column(Integer, primary_key=True)
    title = Column(String(512), nullable=False) 
    link = Column(String(512), nullable=False)
    desc = Column(String(10240))

database = Database()

def create_table():
    global Base
    Base.metadata.create_all(engine)

def drop_table():
    global Base
    Base.metadata.drop_all(engine)
