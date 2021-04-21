from enum import unique
from models.base_model import BaseModel
from models.user import User
from playhouse.hybrid import hybrid_property
import peewee as pw

class GroceryList(BaseModel):
    user = pw.ForeignKeyField(User, backref="grocerylists", on_delete='CASCADE')
    ingredient = pw.CharField(unique=False, null=False)

    def validate(self):
        duplicate_ingredient = GroceryList.get(GroceryList.ingredient == self.ingredient)
        if duplicate_ingredient == None:
            print("Ingredient is NoneType")
        elif duplicate_ingredient.user == self.user:
            self.errors.append('Ingredient is already in the List')
