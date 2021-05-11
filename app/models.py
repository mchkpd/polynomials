from app import db


class Polynomial(db.Model):
    __tablename__ = 'polynomials'

    id = db.Column(db.Integer(), primary_key=True)
    expression = db.Column(db.String(255), nullable=False)

    def __init__(self, expression=None):
        self.expression = expression
