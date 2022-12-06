from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/reklam'
db = SQLAlchemy(app)

class Annons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kundid = db.Column(db.Integer, nullable=False)
    del1 = db.Column(db.String(30), unique=False, nullable=False)
    del2 = db.Column(db.String(30), unique=False, nullable=False)
    del3 = db.Column(db.String(30), unique=False, nullable=False)

class Kund(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    namn = db.Column(db.String(50),unique=False,nullable=False)
    betalt = db.Column(db.Integer,unique=False,nullable=False)

if __name__  == "__main__":
    with app.app_context():
        db.create_all()
        db.session.commit()

        kund = Kund()
        kund.namn = "Hederlige Harrys Bilar"
        kund.betalt = 1500
        db.session.add(kund)

        kund = Kund()
        kund.namn = "Farmor Ankas Pajer AB"
        kund.betalt = 3000
        db.session.add(kund)


        kund = Kund()
        kund.namn = "Svarte Petters Svartbyggen"
        kund.betalt = 1500
        db.session.add(kund)


        kund = Kund()
        kund.namn = "Långbens detektivbyrår"
        kund.betalt = 4000
        db.session.add(kund)
    
        kund = Kund()
        kund.namn = "Yrrol AB"
        kund.betalt = 6000
        db.session.add(kund)


        db.session.commit()

        annons =Annons()
        annons.kundid = 1
        annons.del1 = "Köp bil"
        annons.del2 = "hos "
        annons.del3 = "Harry"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 1
        annons.del1 = "En god"
        annons.del2 = "bilaffär  "
        annons.del3 = "(för Harry!)"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 1
        annons.del1 = "Hederlige "
        annons.del2 = "Harrys   "
        annons.del3 = "Bilar"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 2
        annons.del1 = "Köp paj"
        annons.del2 = "hos   "
        annons.del3 = "Farmor Anka"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 2
        annons.del1 = "Skynda innan  "
        annons.del2 = "Mårten     "
        annons.del3 = "ätit alla pajer"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 3
        annons.del1 = "Låt Petter"
        annons.del2 = "bygga    "
        annons.del3 = "åt dig"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 3
        annons.del1 = "Bygga svart?  "
        annons.del2 = "Ring      "
        annons.del3 = "Petter"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 4
        annons.del1 = "Mysterier?"
        annons.del2 = "Ring     "
        annons.del3 = "Långben"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 4
        annons.del1 = "Långben   "
        annons.del2 = "fixar       "
        annons.del3 = "biffen"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 5
        annons.del1 = "T-Röd - "
        annons.del2 = "för dig som "
        annons.del3 = "tänkt klart"
        db.session.add(annons)

        annons =Annons()
        annons.kundid = 5
        annons.del1 = "Claes Månsson -"
        annons.del2 = "om flickan själv"
        annons.del3 = " får välja"
        db.session.add(annons)


        db.session.commit()



