from app import db, Base


class Scout(Base):

    __tablename__ = "scouts"
    user = db.Column(db.Integer, db.ForeignKey('users.id'))
    full_registration = db.Column(db.Boolean, default=False)
    fio = db.Column(db.Text)
    inn = db.Column(db.Integer)
    snils = db.Column(db.Text)
    birth_date = db.Column(db.DateTime)
    birth_place = db.Column(db.Text)
    passport_series = db.Column(db.Text)
    passport_number = db.Column(db.Text)
    passport_date_of_issue = db.Column(db.DateTime)
    passport_division_code = db.Column(db.Text)
    passport_division_name = db.Column(db.Text)
    registration_address = db.Column(db.Text)
    living_address = db.Column(db.Text)
    pass_scan = db.Column(db.Text)
    pass_registration_scan = db.Column(db.Text)

