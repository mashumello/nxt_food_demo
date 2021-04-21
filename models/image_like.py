from models.base_model import BaseModel
from models.user import User
from models.image import Image
from playhouse.hybrid import hybrid_property
import peewee as pw

class ImageLike(BaseModel):
    user = pw.ForeignKeyField(User, backref='likes', on_delete='CASCADE')
    image = pw.ForeignKeyField(Image, backref='likes', on_delete='CASCADE')
    is_like = pw.BooleanField(default=False)