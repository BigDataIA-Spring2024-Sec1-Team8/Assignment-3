from pydantic import BaseModel, Field, validator, ValidationError
from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, constr
from typing import Optional, Any
from pydantic.functional_validators import field_validator
from typing_extensions import Annotated
from pydantic import BaseModel, Field, validator, ValidationError

class MetaData(BaseModel):
    title: str = Field(alias='Title', default="Unknown")  
    publisher: str = Field(default="Unknown")
    availability_status: str = Field(default="", alias='availability_status')
    analytic: str = Field(default="Not Available", alias='analytic', min_length=2)
    imprinted_date: str = Field(..., alias='imprinted_date')  
    abstract: str = Field(default="", min_length=2)

    @validator('title', 'publisher', 'availability_status', 'analytic', 'imprinted_date', 'abstract', pre=True, each_item=False)
    def check_empty_string(cls, v,values):
        if v == "":
            raise ValueError(f'empty string not allowed')

        return v
class LearningOutcomes(BaseModel):
    topic: str = Field(..., alias='topic', min_length=2)  
    outcomes: str = Field(default="Not defined", min_length=2)

    @validator('topic', 'outcomes', pre=True, each_item=False)
    def strip_whitespace(cls, v):
        if isinstance(v, str):
            ValueError('empty not allowed')
        return v