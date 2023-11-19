from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:12345678@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Phone(db.Model):
    __tablename__ = 'Phone_tb'
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    person = db.relationship('Person', backref='phone', lazy='dynamic')

    def __repr__(self):
        return 'Phone_name: {}'.format(self.name)


class Person(db.Model):
    __tablename__ = 'Person_tb'
    mid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    age = db.Column(db.Integer)
    phone_id = db.Column(db.Integer, db.ForeignKey('Phone_tb.pid'))

    def __repr__(self):
        return 'Person_name: {}'.format(self.name)


db.drop_all()
db.create_all()
# phone_one = Phone(name='IPhone')
# phone_two = Phone(name='Mi')
# phone_three = Phone(name='NOKIA')
# phone_four = Phone(name='HUAWEI')
# phone_five = Phone(name='OPPO')
# phone_six = Phone(name='VIVO')
# db.session.add_all([phone_one, phone_two, phone_three, phone_four, phone_five, phone_six])
# db.session.commit()

# per_one = Person(name='You', age=18, phone_id=1)
# per_two = Person(name='Me', age=81, phone_id=3)
# per_three = Person(name='JackMa', age=60, phone_id=2)
# per_four = Person(name='Panshiyi', age=50, phone_id=4)
# per_five = Person(name='DingLei', age=40, phone_id=1)
# db.session.add_all([per_one, per_two, per_three, per_four, per_five])
# db.session.commit()
# first = Person.query.first()
# print(first)

if __name__ == '__main__':
    app.run(debug=True)
    
