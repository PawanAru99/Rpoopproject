from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Payslip(db.Model):
    __tablename__ = "payslip"
    Shalarth_ID = db.Column(db.String(100), primary_key=True)
    Panchayat_samiti = db.Column(db.String(100))
    School_Udise_Code = db.Column(db.String(100))
    School_Name = db.Column(db.String(100))
    SSDC = db.Column(db.String(100))
    sr_no_of_employee = db.Column(db.String(100))
    Teacher_name = db.Column(db.String(100))
    Gender = db.Column(db.String(100))
    Position = db.Column(db.String(100))
    GPF_NO = db.Column(db.String(100))
    DCPS_NO = db.Column(db.String(100))
    PRAN_NO = db.Column(db.String(100))
    PAN_NO = db.Column(db.String(100))
    ADHAR_NO = db.Column(db.String(100))
    MOB_NO = db.Column(db.String(100))
    EMAIL_ID = db.Column(db.String(100))
    DDO_BANK_NAME = db.Column(db.String(100))
    DDO_BANK_ACCOUNT_NUMBER = db.Column(db.String(100))
    DDO_BANK_IFSC_CODE = db.Column(db.String(100))
    BANK_NAME = db.Column(db.String(100))
    BANK_ACCOUNT_NUMBER = db.Column(db.String(100))
    BANK_IFSC_CODE = db.Column(db.String(100))
    BRANCH_NAME = db.Column(db.String(100))
    Pay_matrix = db.Column(db.String(100))
    mul_vetan = db.Column(db.String(100))
    mahagai_batta = db.Column(db.String(100))
    gharbhade = db.Column(db.String(100))
    vahan_batta = db.Column(db.String(100))
    Washing_Allowance = db.Column(db.String(100))


db.create_all()


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    Shalarth_ID = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    adhar = db.Column(db.String(1000))


# Line below only required once, when creating DB.
db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(Shalarth_ID=request.form.get('Shalarth_ID')).first():
            return redirect(url_for('login'))
        new_user = User(
            Shalarth_ID=request.form.get('Shalarth_ID'),
            password=request.form.get('password'),
            adhar=request.form.get('adhar')
        )
        db.session.add(new_user)
        db.session.commit()
        redirect(url_for('login'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        Shalarth_ID = request.form.get('Shalarth_ID')
        password = request.form.get('password')

        user = User.query.filter_by(Shalarth_ID=Shalarth_ID).first()
        print(user)
        if not user:
            flash("That mis does not exist, please try again.")
            return redirect(url_for('login'))
        elif (user.password!=password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            #login_user(user)
            datas = Payslip.query.filter_by(Shalarth_ID=Shalarth_ID).first()
            print(datas)
            return render_template('secrets.html', datas=datas)

    return render_template("login.html")


@app.route('/secrets')
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
def logout():
    return render_template("login.html")


@app.route('/download')
def download():
    pass


if __name__ == "__main__":
    app.run(debug=True)



