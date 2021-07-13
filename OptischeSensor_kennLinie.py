from typing import List
from matplotlib import colors
import matplotlib.pyplot as plt
import matplotlib as mpl 
import numpy as np

#optische Abstandssensor Kennlinie
def optischeSensor(x:List[float], y:List[float]):
    #background
    plt.style.use('Solarize_Light2')
    #graph title
    plt.title("Optische Abstandssensor", loc='center')
    plt.xlabel('Ausgangsstrom [mA]')
    plt.ylabel('Anzeige Laser [mm]')
    #line style
    mpl.rc('lines', linewidth=2, linestyle='-')
    plt.plot(x,y,'c')
    plt.show()

#Ansprechkurve von Lichttaste
def Ansprechkurve(x:List[int], y:List[int], z1:List[int], z2:List[int]):
    #background
    plt.style.use('Solarize_Light2')
    #graph title
    plt.title("Ansprechkurve", loc='center')
    plt.xlabel('a [mm]')
    plt.ylabel('Tastweite [mm]')
    #line style
    mpl.rc('lines', linewidth=2, linestyle='--')
    plt.plot(x,z1,'r', label='Warnbereich')
    #x,y axis scale
    plt.xlim(0,400)
    plt.ylim(0,400)
    mpl.rc('lines', linewidth=2, linestyle='-')
    plt.plot(y,z2,'c', label='Schaltpunkt')
    plt.legend()
    plt.show()

if __name__=="__main__":
    #Ansprechkurve
    #Warnbereich von Lichtaste
    x1 = [4.85,14.95,22.52,32.54,39.72,46.01,49.52,56.67,62.23,60.54,60.3,
        61.12,70.12,71.39,71.26,49.13,47.12,38.25]
    #Schaltpunk von lichttaste
    y1 = [4.61,14.49,22.09,31.05,37.48,42.77,49.08,52.16,53.2,54.3,54.73,
        42.6,39.42,24.09,-0.228]
    z1 = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340]
    z2 = [0,20,40,60,80,100,120,140,160,180,200,220,240,260,280]
    #optische Abstandssensor
    #Ausgangsstrom [mA]
    x2 = [3.96,4.09,4.13,4.39,4.57,4.56,4.76,4.78,4.94,5.00,5.22]
    #Anzeige Laser [mm]
    y2 = [235,245,255,265,275,285,295,305,315,325,335]
    # Ansprechkurve(x1,y1,z1,z2)
    optischeSensor(x2,y2)


   