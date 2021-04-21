from models.base_model import BaseModel
from models.user import User
from models.image import Image
from playhouse.hybrid import hybrid_property
import peewee as pw

class Comment(BaseModel):
    user = pw.ForeignKeyField(User, backref='comments', on_delete='CASCADE')
    image = pw.ForeignKeyField(Image, backref='comments', on_delete='CASCADE')
    user_comment = pw.TextField(unique=False, null=False)