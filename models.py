from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CreditodeConsumo(db.Model):
    
    __tablename__ = "creditodeconsumo"
    creditodeconsumo_id = db.Column(db.Integer, primary_key=True)
    entidadfinanciera = db.Column(db.String, nullable=False)
    entre31y365dias = db.Column(db.Float, nullable=False)
    entre366y1095dias = db.Column(db.Float, nullable=False)
    entre1096y1825dias = db.Column(db.Float, nullable=False)
    masde1825dias = db.Column(db.Float, nullable=False)


class TarjetadeCreditodeConsumo(db.Model):

    __tablename__ = "tarjetacreditodeconsumo"
    tarjetadecreditoconsumo_id = db.Column(db.Integer, primary_key=True)
    entidad = db.Column(db.String, nullable=False)
    avancesenefectivo = db.Column(db.Float, nullable=False)
    consumoaunmes = db.Column(db.Float, nullable=False)
    consumoentre2y6meses = db.Column(db.Float, nullable=False)
    consumoentre7y12meses = db.Column(db.Float, nullable=False)
    consumoentre13y18meses = db.Column(db.Float, nullable=False)
    consumomasde18meses = db.Column(db.Float, nullable=False)

class CreditoViviendaConstruccionUvr(db.Model):

    __tablename__ = "creditoviviendaconstuccionuvr"
    creditoviviendaconstuccionuvr_id = db.Column(db.Integer, primary_key=True)
    entidad = db.Column(db.String, nullable=False)
    viviendadeinteressocial = db.Column(db.Float, nullable=False)
    noviviendadeinteressocial = db.Column(db.Float, nullable=False)

class CreditoViviendaConstruccionPesos(db.Model):

    __tablename__ = "creditoviviendaconstuccionpesos"
    creditoviviendaconstuccionpesos_id = db.Column(db.Integer, primary_key=True)
    entidad = db.Column(db.String, nullable=False)
    viviendadeinteressocial = db.Column(db.Float, nullable=False)
    noviviendadeinteressocial = db.Column(db.Float, nullable=False)

class CreditoViviendaAdquisicionUvr(db.Model):

    __tablename__ = "creditoviviendaadquisicionuvr" 
    creditoviviendaadquisicionuvr_id = db.Column(db.Integer, primary_key=True) 
    entidad = db.Column(db.String, nullable=False)
    viviendadeinteressocial = db.Column(db.Float, nullable=False)
    noviviendadeinteressocial = db.Column(db.Float, nullable=False)

class CreditoViviendaAdquisicionPesos(db.Model):

    __tablename__ = "creditoviviendaadquisicionpesos" 
    creditoviviendaadquisicionpesos_id = db.Column(db.Integer, primary_key=True) 
    entidad = db.Column(db.String, nullable=False)
    viviendadeinteressocial = db.Column(db.Float, nullable=False)
    noviviendadeinteressocial = db.Column(db.Float, nullable=False)







