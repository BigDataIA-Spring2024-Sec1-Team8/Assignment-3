from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import ValidationError
from sqlalchemy import Sequence
from models import MetaData, LearningOutcomes
import sys
print(sys.path)
Base = declarative_base()
import logging
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class MetaDataOrm(Base):
    __tablename__ = 'pdf_metadata'

    id = Column(Integer, Sequence('metadata_table2_id_seq'), primary_key=True, autoincrement=True)
    title = Column(String)
    publisher = Column(String, default=2023)
    availability_status = Column(String, default="")
    analytic = Column(String, default="Not Available")
    imprinted_date = Column(String)
    abstract = Column(String, default="")

def orm_instance_to_meta_pydantic(orm_instance):
    print(orm_instance)
    return MetaData(**orm_instance.__dict__)

class LearningOutcomesOrm(Base):
    __tablename__ = 'pdf_content'

    id = Column(Integer, Sequence('learning_outcomes_table_id_seq'), primary_key=True, autoincrement=True)
    topic = Column(String)
    outcomes = Column(String, default=2023)

def orm_instance_to_outcome_pydantic(orm_instance):
    return LearningOutcomes(**orm_instance.__dict__)
