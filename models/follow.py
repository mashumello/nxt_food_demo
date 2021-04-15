from models.base_model import BaseModel
from models.user import User
from playhouse.hybrid import hybrid_property
import peewee as pw

class Follow(BaseModel):
    fan = pw.ForeignKeyField(User, on_delete='CASCADE')
    idol = pw.ForeignKeyField(User, on_delete='CASCADE')
    is_approve = pw.BooleanField(null=True)