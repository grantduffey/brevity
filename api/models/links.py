from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column

from pydantic import BaseModel
from models.base import Base

class Links(Base):
    __tablename__ = "links"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    o_url = Column(String)
    s_url = Column(String)
    uid = mapped_column(ForeignKey("users.id"))
    
class LinksSchema(BaseModel):
    title: str
    o_url: str
    s_url: str
    uid: int
    
    class Config:
        populate_by_name = True