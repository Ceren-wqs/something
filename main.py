from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary_yeni.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Veri tabanı oluşturma
db = SQLAlchemy(app)

class card(db.Model):
    # Sütunlar oluşturuluyor
    #id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # Giriş
    can = db.Column(db.String(20), nullable=False)
    # Şifre
    cannot = db.Column(db.String(20), nullable=False)
    cannot2 = db.Column(db.String(20), nullable=False)
    cannot3 = db.Column(db.String(20), nullable=False)
    cannot4 = db.Column(db.String(20), nullable=False)

@app.route("/")
def home():
    return render_template("home.html")

skor = 0
sorulan = []  
@app.route("/game",methods=["GET","POST"])
def game():
    global skor, sorulan
    if request.method=="GET":
        skor = 0
        sorulan = []    
    data = card.query.all()
    soru = random.randint(1,len(data))
    while soru in sorulan:
        soru = random.randint(1,len(data))
    mleh = card.query.get(soru)   
    xyz = [mleh.can,mleh.cannot,mleh.cannot2,mleh.cannot3] 
    xyz = random.shuffle(xyz)
    print(type(xyz))
    return render_template("game.html",skor=skor,mleh=mleh,xyz=xyz)
    





@app.route("/ayarlar",methods=["GET","POST"])
def ayarlar():
    if request.method=="POST":
        metin=request.form.get("title")
        yasak1=request.form.get("kilim")
        yasak2=request.form.get("kelim")
        yasak3=request.form.get("kulim")
        yasak4=request.form.get("kalim")

        yeni=card(can=metin,cannot=yasak1,cannot2=yasak2,cannot3=yasak3,cannot4=yasak4)
        db.session.add(yeni)
        db.session.commit()

    return render_template("index.html")

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

