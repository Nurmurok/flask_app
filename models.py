from peewee import *
from datetime import datetime

db = PostgresqlDatabase(
    'flask_db2',
    host = 'localhost',
    port = '5432',
    user = 'flask_user2',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Register(BaseModel):
    user_name = CharField(max_length=255, null = False)
    password = CharField(max_length=255, null = False)
    post = CharField(max_length=255, null = False)
    date = DateField(default = datetime.now)
    email = CharField(max_length=255, null = False)
    
    

    def repr(self):
        return self.name 

# db.create_tables([Register])
# Register.create(name='ALihan', second_name='ruslanov', email='rusla@gmila.com')

db.close()