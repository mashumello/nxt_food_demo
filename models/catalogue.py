from enum import unique
from models.base_model import BaseModel
from models.user import User
from playhouse.hybrid import hybrid_property
import peewee as pw

class Catalogue(BaseModel):
    user = pw.ForeignKeyField(User, backref="catalogues", on_delete='CASCADE')
    ingredient = pw.CharField(unique=True, null=False)