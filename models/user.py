from models.base_model import BaseModel
from werkzeug.security import generate_password_hash
from playhouse.hybrid import hybrid_property
import peewee as pw
import re


class User(BaseModel):
    username = pw.CharField(unique=True, null=False)
    email = pw.CharField(unique=True, null=False)
    password = None
    hash_password = pw.CharField(unique=True, null=False)
    profile_image = pw.CharField(unique=False, default="https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png")
    is_private = pw.BooleanField(default=False)

    def validate(self):
        duplicate_username = User.get_or_none(User.username == self.username)

        if duplicate_username == None:
            print("Username is NoneType")
        elif duplicate_username:
            self.errors.append('Username is not unique')

        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_email == None:
            print("Email is NoneType") 
        elif duplicate_email.id != self.id:
            self.errors.append('Email is not unique')
        
        if self.password == None:
            print("Password is Nonetype")
        elif len(self.password) <= 7:
            self.errors.append("Password must contain at least 8 characters.")
        elif len(self.password) > 7:
            has_lower = re.search(r"[a-z]", self.password)
            has_upper = re.search(r"[A-Z]", self.password)
            has_special = re.search(r"[\W]", self.password)

            if has_lower and has_upper and has_special:
                self.hash_password = generate_password_hash(self.password)
            else:
                self.errors.append("Password must contain atleast one lower, upper, and special character.")

        if self.profile_image == None:
            print("Profile Image is None")