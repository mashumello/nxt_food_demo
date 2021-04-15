from models.base_model import BaseModel
from models.user import User
from models.image import Image
from playhouse.hybrid import hybrid_property
import peewee as pw

class Like_Comment(BaseModel):
    image = pw.ForeignKeyField(Image, on_delete='CASCADE')
    
     