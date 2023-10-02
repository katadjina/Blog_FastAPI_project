from pydantic import BaseModel
from datetime import datetime

#contains data that is transmitted to the API and that is received from API

class PostBase(BaseModel):
    image_url: str
    title: str
    content_type: str
    creator: str
    #no id is needed here bc it is automatically generatedted
    
    
    
class PostDisplay(BaseModel):
    id: int #we just use the id that was generated
    image_url: str
    title: str
    content_type: str
    creator: str
    timestamp: datetime
    class Config():
        orm_mode = True
    
    