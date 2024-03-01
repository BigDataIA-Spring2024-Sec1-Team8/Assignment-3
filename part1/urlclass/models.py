from pydantic import BaseModel, constr, Field, validator
from typing import Optional, Any
from typing_extensions import Annotated

class URLClass(BaseModel):
    id: int
    name_of_the_topic: Annotated[str, Field(alias='name_of_the_topic')]
    year: int = Field(..., ge=1900, le=2024)
    level: Annotated[str, Field(alias='level')]
    topics: constr(strict=True, min_length=1)
    learning_outcomes: Annotated[str, Field(alias='learning_outcomes')]
    introduction: Annotated[Optional[str], Field(alias='introduction', default="Not Available")]
    summary: Annotated[Optional[str], Field(alias='summary', default="Not Available")]
    link_to_the_pdf_file: Annotated[Optional[str], Field(alias='link_to_the_pdf_file',default="/")]
    link_to_the_summary_page: Annotated[Optional[str], Field(alias='link_to_the_summary_page', default="/")]


    @validator('year')
    def validate_curriculum_year(cls, value):
        if value < 1900 or value > 2024:
            raise ValueError('Curriculum year must be between 1900 and 2024')
        return value

    @validator('level')
    def validate_level(cls, value):
        if not value.startswith('Level'):
            raise ValueError('Level must start with the keyword "Level"')
        return value

    @validator('learning_outcomes', 'introduction', 'summary', pre=True)
    def default_not_available_if_empty(cls, value):
        return value if value else "Not Available"

    @validator('link_to_the_pdf_file')
    def validate_pdf_link(cls, value):
        if not value.endswith('.pdf'):
            raise ValueError('PDF link must end with .pdf')
        return value

    @validator('link_to_the_summary_page')
    def validate_pdf_link(cls, value):
        if not value.startswith('https://'):
            raise ValueError('Link to summary page must start with https://')
        return value
    class Config:
        anystr_strip_whitespace = True
