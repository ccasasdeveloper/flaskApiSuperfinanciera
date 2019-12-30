import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import csv
from models import *
from sqlalchemy import create_engine
from flask import Flask, render_template, jsonify, request

engine = create_engine('postgresql://postgres:123456@localhost:5433/apisuperfinanciera')
dbc =  scoped_session(sessionmaker(bind=engine))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:123456@localhost:5433/apisuperfinanciera'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    creditodeconsumo = CreditodeConsumo.query.all()
    
    if creditodeconsumo is None:    
        f = open("creditodeconsumo.csv")
        reader = csv.reader(f)
        for entidadfinanciera, entre31y365dias, entre366y1095dias, entre1096y1825dias, masde1825dias in reader:
            entre31y365dias = float(entre31y365dias)
            entre366y1095dias = float(entre366y1095dias)
            entre1096y1825dias = float(entre1096y1825dias)
            masde1825dias = float(masde1825dias)
            creditodeconsumo = CreditodeConsumo(entidadfinanciera=entidadfinanciera, 
            entre31y365dias= entre31y365dias, entre366y1095dias=entre366y1095dias,
            entre1096y1825dias=entre1096y1825dias, masde1825dias=masde1825dias
            )
            dbc.add(creditodeconsumo)
            print(f"added creditodeconsumo {entidadfinanciera} {entre31y365dias}{entre1096y1825dias}{masde1825dias}{masde1825dias}")
        dbc.commit()
    tarjetasdecreditoconsumo = TarjetadeCreditodeConsumo.query.all()
    print(tarjetasdecreditoconsumo)
    if tarjetasdecreditoconsumo == []:
        print('hello')
        f = open("tarjetadecreditodeconsumo.csv")
        reader = csv.reader(f)
        for entidad, avancesenefectivo, consumoaunmes, consumoentre2y6meses, consumoentre7y12meses, consumoentre13y18meses, consumomasde18meses in reader:
            avancesenefectivo = float(avancesenefectivo)
            consumoaunmes = float(consumoaunmes)
            consumosentre2y6meses = float(consumoentre2y6meses)
            consumoentre7y12meses = float(consumoentre7y12meses)
            consumoentre13y18meses = float(consumoentre13y18meses)
            consumomasde18meses = float(consumomasde18meses)
            tarjetasdecreditoconsumo = TarjetadeCreditodeConsumo(entidad=entidad, avancesenefectivo=avancesenefectivo, consumoaunmes=consumoaunmes,
            consumoentre2y6meses=consumoentre2y6meses,consumoentre7y12meses=consumoentre7y12meses,
            consumoentre13y18meses=consumoentre13y18meses,consumomasde18meses=consumomasde18meses)
            dbc.add(tarjetasdecreditoconsumo)
            print(f"added creditodeconsumo {entidad} {avancesenefectivo} {consumoentre2y6meses} {consumoentre7y12meses} {consumoentre13y18meses}")
        dbc.commit()

    creditosviviendaconstruccionuvr = CreditoViviendaConstruccionUvr.query.all()
    if creditosviviendaconstruccionuvr == []:
        f = open("creditoviviendaconstruccionuvr.csv")
        reader = csv.reader(f)
        for entidad, viviendadeinteressocial, noviviendadeinteressocial in reader:
            viviendadeinteressocial = float(viviendadeinteressocial)
            noviviendadeinteressocial = float(noviviendadeinteressocial)
            creditosviviendaconstruccionuvr = CreditoViviendaConstruccionUvr(entidad=entidad,
            viviendadeinteressocial=viviendadeinteressocial,noviviendadeinteressocial=noviviendadeinteressocial)
            dbc.add(creditosviviendaconstruccionuvr)
        dbc.commit()   
    print('hellotwo')

    creditosviviendaconstruccionpesos = CreditoViviendaConstruccionPesos.query.all()
    if creditosviviendaconstruccionpesos == []:
        f = open("creditoviviendaconstruccionpesos.csv")
        reader = csv.reader(f)
        for entidad, viviendadeinteressocial, noviviendadeinteressocial in reader:
            viviendadeinteressocial = float(viviendadeinteressocial)
            noviviendadeinteressocial = float(noviviendadeinteressocial)
            creditosviviendaconstruccionpesos = CreditoViviendaConstruccionPesos(entidad=entidad,
            viviendadeinteressocial=viviendadeinteressocial,noviviendadeinteressocial=noviviendadeinteressocial)
            dbc.add(creditosviviendaconstruccionpesos)
        dbc.commit()

    #creditosviviendaadquisicionuvr = CreditoViviendaAdquisicionUvr.query.all()
    #if creditosviviendaadquisicionuvr == []:
        #f = open("creditoviviendaadquisicionuvr.csv")
        #reader = csv.reader(f)
        #for entidad, viviendadeinteressocial, noviviendadeinteressocial in reader:
            #viviendadeinteressocial = float(viviendadeinteressocial)
            #noviviendadeinteressocial = float(noviviendadeinteressocial)
            #creditoviviendaadquisicionuvr = CreditoViviendaConstruccionUvr(entidad=entidad,
            #viviendadeinteressocial=viviendadeinteressocial,noviviendadeinteressocial=noviviendadeinteressocial)
            #dbc.add(creditoviviendaadquisicionuvr)
        #dbc.commit()
    
    creditosviviendaadquisicionpesos = CreditoViviendaAdquisicionPesos.query.all()
    if creditosviviendaadquisicionpesos == []:
        f = open("creditoviviendaadquisicionpesos.csv")
        reader = csv.reader(f)
        for entidad, viviendadeinteressocial, noviviendadeinteressocial in reader:
            viviendadeinteressocial = float(viviendadeinteressocial)
            noviviendadeinteressocial = float(noviviendadeinteressocial)
            creditoviviendaadquisicionpesos = CreditoViviendaAdquisicionPesos(entidad=entidad,
            viviendadeinteressocial=viviendadeinteressocial,noviviendadeinteressocial=noviviendadeinteressocial)
            dbc.add(creditoviviendaadquisicionpesos)
        dbc.commit()

    return render_template("index.html")

@app.route("/creditoconsumo")
def creditoConsumo():
    creditosdeconsumo = CreditodeConsumo.query.all()
    if not creditosdeconsumo is None:
        creditodeconsumolist = []
        creditosdeconsumolist = []
        ids = []
        entidadfinancieras = []
        entre31y365diass = []
        entre366y1095diass = []
        entre1096y1825diass = []
        masde1825diass = []
        for i in creditosdeconsumo:
            creditodeconsumolist = []
            ids.append(i.creditodeconsumo_id)
            entidadfinancieras.append(i.entidadfinanciera)
            entre31y365diass.append(i.entre31y365dias)
            entre366y1095diass.append(i.entre366y1095dias)
            entre1096y1825diass.append(i.entre1096y1825dias)
            masde1825diass.append(i.masde1825dias)
            creditodeconsumolist.append(i.entidadfinanciera)
            creditodeconsumolist.append(i.entre31y365dias)
            creditodeconsumolist.append(i.entre366y1095dias)
            creditodeconsumolist.append(i.entre1096y1825dias)
            creditodeconsumolist.append(i.masde1825dias)
            creditosdeconsumolist.append(creditodeconsumolist)


    return jsonify({
            
            "creditosdeconsumolist":creditosdeconsumolist
          })


@app.route("/tarjetadecreditoconsumo")
def tarjetadeCreditoConsumo():
    tarjetasdecreditoconsumo = TarjetadeCreditodeConsumo.query.all()
    
    if not TarjetadeCreditodeConsumo is None:
        tarjetasdecreditolist = []
        ids = []
        entidades = []
        avancesenefectivos = []
        consumosaunmess = []
        consumosente2y6mesess = []
        consumoentre7y12mesess = []
        consumoentre13y18mesess = []
        consumomasde18mesess = []
        for i in tarjetasdecreditoconsumo:
            tarjetadecreditolist = []
            
            entidades.append(i.entidad)
            avancesenefectivos.append(i.avancesenefectivo)
            consumosaunmess.append(i.consumoaunmes)
            consumosente2y6mesess.append(i.consumoentre2y6meses)
            consumoentre7y12mesess.append(i.consumoentre7y12meses)
            consumoentre13y18mesess.append(i.consumoentre13y18meses)
            consumomasde18mesess.append(i.consumomasde18meses)
            tarjetadecreditolist.append(i.entidad)
            tarjetadecreditolist.append(i.avancesenefectivo)
            tarjetadecreditolist.append(i.consumoaunmes)
            tarjetadecreditolist.append(i.consumoentre2y6meses)
            tarjetadecreditolist.append(i.consumoentre7y12meses)
            tarjetadecreditolist.append(i.consumoentre13y18meses)
            tarjetadecreditolist.append(i.consumomasde18meses)
            tarjetasdecreditolist.append(tarjetadecreditolist)         

    return jsonify({

            "tarjetasdecreditolist":tarjetasdecreditolist
          })

@app.route("/creditodeviviendaconstruccionuvr")
def creditosViviendaConstruccionUvr():
    creditosviviendaconstruccionuvr = CreditoViviendaConstruccionUvr.query.all()
    if not creditosviviendaconstruccionuvr is None:
        ids = []
        entidades = []
        viviendadeinteressocials = []
        noviviendadeinteressocials = []
        creditosviviendaconstruccionuvrlist = []
        for i in creditosviviendaconstruccionuvr:
            creditoviviendaconstruccionuvrlist = []
            ids.append(i.creditoviviendaconstuccionuvr_id)
            entidades.append(i.entidad)
            viviendadeinteressocials.append(i.viviendadeinteressocial)
            noviviendadeinteressocials.append(i.noviviendadeinteressocial)
            creditoviviendaconstruccionuvrlist.append(i.creditoviviendaconstuccionuvr_id)
            creditoviviendaconstruccionuvrlist.append(i.entidad)
            creditoviviendaconstruccionuvrlist.append(i.viviendadeinteressocial)
            creditoviviendaconstruccionuvrlist.append(i.noviviendadeinteressocial)
            creditosviviendaconstruccionuvrlist.append(creditoviviendaconstruccionuvrlist)

    return jsonify({
            
            "creditosviviendaconstruccionuvrlist":creditosviviendaconstruccionuvrlist
            
          })    
@app.route("/creditodeviviendaconstruccionpesos")
def creditosViviendaConstruccionPesos():
    creditosviviendaconstruccionpesos = CreditoViviendaConstruccionPesos.query.all()
    if not creditosviviendaconstruccionpesos is None:
        creditosviviendaconstruccionpesoslist = []
        for i in creditosviviendaconstruccionpesos:
            creditoviviendaconstruccionpesoslist = []
            creditoviviendaconstruccionpesoslist.append(i.creditoviviendaconstuccionpesos_id)
            creditoviviendaconstruccionpesoslist.append(i.entidad)
            creditoviviendaconstruccionpesoslist.append(i.viviendadeinteressocial)
            creditoviviendaconstruccionpesoslist.append(i.noviviendadeinteressocial)
            creditosviviendaconstruccionpesoslist.append(creditoviviendaconstruccionpesoslist)
    return jsonify({
            
            "creditosviviendaconstruccionpesoslist":creditosviviendaconstruccionpesoslist
            
          })  

@app.route("/creditodeviviendaadquisicionpesos")
def creditosViviendaAdquisicionPesos():
    creditosviviendaadquisicionpesos = CreditoViviendaAdquisicionPesos.query.all()
    if not creditosviviendaadquisicionpesos is None:
        creditosviviendaadquisicionpesoslist = []
        for i in creditosviviendaadquisicionpesos:
            creditoviviendaadquisicionpesoslist = []
            creditoviviendaadquisicionpesoslist.append(i.creditoviviendaadquisicionpesos_id)
            creditoviviendaadquisicionpesoslist.append(i.entidad)
            creditoviviendaadquisicionpesoslist.append(i.viviendadeinteressocial)
            creditoviviendaadquisicionpesoslist.append(i.noviviendadeinteressocial)
            creditosviviendaadquisicionpesoslist.append(creditoviviendaadquisicionpesoslist)
    return jsonify({
            
            "creditosviviendaadquisicionpesoslist":creditosviviendaadquisicionpesoslist
            
          })  

if __name__== "__main__":
    main()

