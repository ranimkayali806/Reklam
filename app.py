from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade

app = Flask("__name__")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Mercedes600@localhost/employee'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(80),unique=False,nullable=False)
    age = db.Column(db.Integer,unique=False,nullable=False)
    birthdate = db.Column(db.DateTime,unique=False,nullable=False)
    city = db.Column(db.String(20),unique=False,nullable=True)
    shoesize = db.Column(db.Integer,unique=False,nullable=False)

   
def CreateNew():
    b = Employee()
    b.namn = input("Ange namn: ")
    b.age = input("Ange ålder: ")
    b.birthdate = input("Ange födelseår: ")
    b.city = input("Ange stad ")
    b.shoesize = input("Ange skostorlek ")
    db.session.add(b)
    db.session.commit()

def Search():
    text = input("Ange text att söka på: ")
    resultat = Employee.query.filter(Employee.namn.contains(text)).all()
    for emp in resultat :
        print(f"{emp.id}, {emp.namn}")
    Id = int(input("Ange id på den som du vill uppdatera elle 0"))

    if id == 0:
        return
    
    employee = Employee.query.filter_by(id = Id).first()
    print(f"{employee.id}, {employee.namn}, {employee.age}")
    employee.namn = input("Ange nytt namn ")
    employee.age = input("Ange ny ålder ")
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        #db.create_all()
        #db.session.commit()
        upgrade()

        while True:
            print("1  Sök")
            print("2. Skapa ny")
            print("7. Avsluta")
            action = input("Ange val: ")

            if action == "1":
                Search()

            if action == "2":
                CreateNew()

            if action == "7":
                break




