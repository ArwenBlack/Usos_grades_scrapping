from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from Grades import Grades
import pandas as pd
engine = create_engine('sqlite:///usos_database.db', echo=True)
Base = declarative_base()


class GradesData(Base):
    __tablename__ = 'class_semester'
    class_name = Column(String, primary_key=True)
    semester = Column(String)
    wyk = Column(String)
    cw = Column(String)
    lab = Column(String)
    pp = Column(String)


Base.metadata.create_all(engine)


def insert_class(class_names, semesters):
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(GradesData.class_name).filter(GradesData.class_name == class_names)
    if not session.query(q.exists()).scalar():
        classes = GradesData(class_name=class_names, semester=semesters)
        session.add(classes)
        session.commit()


def insert_grades(grades: Grades):
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = update(GradesData).where(GradesData.class_name == grades.name).values(wyk=grades.WYK, cw=grades.CW,
                                                                                lab=grades.LAB, pp=grades.PP)
    session.execute(ins)
    session.commit()


def get_table():
    df = pd.read_sql_table('class_semester', engine)
    return df