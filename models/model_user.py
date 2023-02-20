from app import db, Base


class User(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Text, unique=True)
    email = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)
    name = db.Column(db.Text)
    refresh_token = db.Column(db.Text, unique=True)
    refresh_token_timestamp = db.Column(db.Integer)
    refresh_token_ttl = db.Column(db.Integer)
    failed_login_count = db.Column(db.Integer, default=0)
    date_last_failed_login = db.Column(db.DateTime)