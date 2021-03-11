from dataclasses import dataclass

import sqlalchemy
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, query

engine = create_engine('sqlite:///usos_database.db', echo=True)
Base = declarative_base()

class Grades_data(Base):
    __tablename__  = 'class_semester'
    class_name = Column(String, primary_key=True)
    semester = Column(String)
    wyk = Column(Float)
    cw = Column(Float)
    lab = Column(Float)
    pp = Column(Float)


Base.metadata.create_all(engine)

def insert_class (class_names, semesters):
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(Grades_data.class_name).filter(Grades_data.class_name==class_names)
    if (not session.query(q.exists()).scalar()):
        classes = Grades_data(class_name=class_names, semester=semesters)
        session.add(classes)
        session.commit()


def insert_grades(class_name, c_name, grade):
    Session = sessionmaker(bind=engine)
    session = Session()

