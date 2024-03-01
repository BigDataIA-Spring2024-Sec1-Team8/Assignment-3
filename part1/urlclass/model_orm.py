from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class URLOrm(Base):
    __tablename__ = 'readings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name_of_the_topic = Column(String)
    year = Column(String)
    level = Column(String)
    topics = Column(String)
    learning_outcomes = Column(String, default="Not Available")
    introduction = Column(String, default="Not Available")
    summary = Column(String, default="Not Available")
    link_to_the_pdf_file = Column(String, default="/")
    link_to_the_summary_page = Column(String, default="https://")


