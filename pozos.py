from __future__ import division
import pandas
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

data = pandas.read_csv("pozos.csv",encoding="utf-8",delimiter=",");

## Renombrar columnas.
data.columns = ["periodo","asignacion","region_fiscal","campo_oficial","pozo","ronda_licitacion","compania","produccion_petroleo(mbd)","produccion_gas_asociado(mmpcd)","produccion_gas_no_asociado(mmpcd)","produccion_total_de_gas(mmpcd)","tipo_de_aceite","pozo_productor"];

a = data[[0,4,7]];

## Pozos (sin repetir valores) 
pozos = np.unique(data.pozo.values);

## Convertir fechas al formato adecuado
periodos = data.periodo.values;

for i in range(len(periodos)):
    periodos[i] = periodos[i].encode("utf-8");
    periodos[i] = datetime.strptime(periodos[i],"%b-%y");

periodos = pandas.DataFrame({ "periodos":periodos[:] })
data.periodos = periodos;

# Ordenar por fecha
data = data.sort_values(by="periodo")

# Periodos
# periodos = np.unique(data.periodo.values);
# [pozos[i],(len(data[data['pozo'] == pozos[i]][[7]]))]

def NuevaTabla():
    nuevaTabla = [];
    print "Calculando...";
    for i in range(len(pozos)):
        #a = Reg(pozos[i],7);
        #a.Parametros();
        nuevaTabla.append( [pozos[i], len( data[data['pozo'] == pozos[i]][[7]] )] );

    nuevaTabla = np.array(nuevaTabla);
    nuevaTabla = pandas.DataFrame({ 'pozos':nuevaTabla[:,0], 'observaciones':nuevaTabla[:,1] })#, "pendientes":nuevaTabla[:,2], 'R_2':nuevaTabla[:,3] });
#    nuevaTabla = nuevaTabla[nuevaTabla['observaciones'] >= limite]
    print "Se ha obtenido la nueva tabla..";
    return nuevaTabla;


class Reg(object):
    def __init__(self,pozo,variable):
        self.pozo = pozo
        self.variable = variable
        self.x = 0
        self.y = 0
        self.slope = 0
        self.intercept = 0
        self.R_2 = 0
        self.y_yat = 0

    def Parametros(self):
        self.y = data[data['pozo'] == self.pozo][[self.variable]].values;
        self.y = self.y.reshape(1,self.y.shape[0])[0].tolist();
        self.x = [];
        for i in range(len(self.y)):
            self.x.append(i);


        self.x = np.array(self.x);
        self.y = np.array(self.y);
        self.slope,self.intercept,self.R_2,p_value,std_err = stats.linregress(self.x,self.y);
	self.R_2 = self.R_2**2

    def Graficar(self):
	self.y_hat = self.intercept + self.slope * self.x
        plt.plot(self.x,self.y)
        plt.plot(self.x,self.y_hat)
        plt.show()
