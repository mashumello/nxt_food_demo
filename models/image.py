from models.base_model import BaseModel
from models.user import User
from playhouse.hybrid import hybrid_property
import peewee as pw


class Image(BaseModel):
    user = pw.ForeignKeyField(User, backref='images', on_delete='CASCADE')
    image_url = pw.TextField(null=True, on_delete='CASCADE')