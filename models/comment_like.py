from models.base_model import BaseModel
from models.user import User
from models.comment import Comment
from playhouse.hybrid import hybrid_property
import peewee as pw

class CommentLike(BaseModel):
    user = pw.ForeignKeyField(User, backref='likes', on_delete='CASCADE')
    comment = pw.ForeignKeyField(Comment, backref='likes', on_delete='CASCADE')
    is_like = pw.BooleanField(default=False)