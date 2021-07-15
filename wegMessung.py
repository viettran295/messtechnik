from typing import List
from matplotlib import colors, lines
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.style.core import load_base_library
from numpy.core.fromnumeric import size 


#Umformer messvalue volt->mm
def Umformer(Messbereich: float, volt:float)->float:
    return (Messbereich//10)*volt

#kennlinie zeichen
def Zeichen(x1:List[float], x2:List[float], x3:List[float], x4:List[float], y:List[float]):
    #background
    plt.style.use('Solarize_Light2')
    #graph title
    plt.title("Kennlinie von Sensoren", loc='center')
    plt.xlabel('Istwert [mm]')
    plt.ylabel('Masterwert [mm]')
    #line style
    mpl.rc('lines', linewidth=2, linestyle='-')
    plt.plot(x1,y,'c', label='MRU')
    plt.plot(x2,y,'r', label='TLI')
    plt.plot(x3,y,'b', label='TLC')
    plt.plot(x4,y,'y', label='WS1.2')
    plt.legend(loc='upper left')
    plt.show()

def Regression(x:List[float], y:List[int], y1:List[float]):
    plt.style.use('Solarize_Light2')
    #graph title
    plt.title("Regression", loc='center')
    plt.xlabel('Prozent %')
    plt.ylabel('[mm]')
    #line style
    plt.scatter(x,y, label='WS12', color='r')
    plt.plot(x,y1, label='Regression', linewidth=1)
    plt.legend(loc='upper left')
    plt.show()

def Abweichung(x:List[float], y1:List[float]):
    #background
    plt.style.use('Solarize_Light2')
    #graph title
    abw = 0.05/100*750
    plt.title("Abweichung", loc='center')
    plt.xlabel('Prozent %')
    plt.ylabel('[mm]')
    #line style
    plt.axhline(y=0, color='r', linewidth=0.5)
    plt.axhline(y=abw, color='b', linewidth=0.5)
    plt.axhline(y=-abw, color='b', linewidth=0.5)
    plt.plot(x,y1, label='WS12', marker='^', color='y')
    plt.legend(loc='lower left')
    plt.show()

def Hysterese(x:List[float], y1:List[float], y2:List[float], y3:List[float], y4:List[float]):
    plt.style.use('Solarize_Light2')
    #graph title
    plt.title("Hysterese", loc='center')
    plt.xlabel('Prozent %')
    plt.ylabel('Master [mm]')
    #line style
    plt.scatter(x,y1, label='MRU')
    plt.scatter(x,y2, label='TLI')
    plt.scatter(x,y3, label='TLC')
    plt.scatter(x,y4, label='WS12')
    plt.legend(loc='upper left')
    plt.show()

if __name__=="__main__":
    Master = [0.0005, 37.519, 74.9765, 112.4825, 150.003, 187.467, 224.983, 262.4615, 299.955, 337.4855, 374.9695]
    Prozent = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # messvalue in voltage
    MRU_V = [0.207, 1.442, 2.678, 3.903, 5.139, 6.374, 7.61, 8.845, 10.081, 10.632, 10.632]
    TLI_V = [0.305, 1.214, 2.143, 3.061, 3.98, 4.909, 5.828, 6.747, 7.676, 8.604, 9.523] 
    TLC_V = [0.33, 1.156, 1.982, 2.797, 3.623, 4.439, 5.264, 6.080, 6.895, 7.721, 8.547]
    WS12_V = [0.127, 0.607, 1.108, 1.608, 2.099, 2.610, 3.11, 3.601, 4.102, 4.613, 5.103]
    
    #Hystrese 10%, 20%, 30% - 90%, 80%, 70%
    MRU_Hys_V = [6.384, 6.384, 6.374, 6.374, 6.384, 6.374]
    TLI_Hys_V = [4.909, 4.909, 4.909, 4.899, 4.899, 4.899]
    TLC_Hys_V = [4.439, 4.449, 4.449, 4.439, 4.439, 4.439]
    WS12_Hys_V = [2.610, 2.61, 2.61, 2.61, 2.62, 2.62]

    #messvalue in mm 
    #MRU 1 inch = 25.4 mm 
    MRU_mm = []
    TLI_mm = []
    TLC_mm = []
    WS12_mm = []

    #Hysterese
    MRU_Hys_mm = []
    TLI_Hys_mm = []
    TLC_Hys_mm = []
    WS12_Hys_mm = []
    Prozent_Hys = [50, 50]
    MRU_Hys_mittel_mm = [191.42, 191.32]
    TLI_Hys_mittel_mm = [196.36, 196.96]
    TLC_Hys_mittel_mm = [200.05, 199.755]
    WS12_Hys_mittel_mm = [195.75, 196.25]
    
    #Regression 
    #MRU
    MRU_Regress = [] 
    for i in Prozent:
        MRU_Regress.append(i*3.42065+16.1224)
    #TLI
    TLI_Regress = []
    for i in Prozent:
        TLI_Regress.append(i*3.69+11.948)
    #TLC
    TLC_Regress = []
    for i in Prozent:
        TLC_Regress.append(i*3.693+15.089)
    #WS12
    WS12_Regress = []
    for i in Prozent:
        WS12_Regress.append(i*3.734+8.6875)

    #Abweichung
    MRU_abw = [] 
    TLI_abw = []
    TLC_abw = []
    WS12_abw = []
    #Abw in mm 
    for i in range(len(Master)):
        MRU_mm.append(Umformer(304.8, MRU_V[i]))
        MRU_abw.append(MRU_mm[i] - MRU_Regress[i])
        TLI_mm.append(Umformer(400,TLI_V[i]))
        TLI_abw.append(TLI_mm[i] - TLI_Regress[i])
        TLC_mm.append(Umformer(450,TLC_V[i]))
        TLC_abw.append(TLC_mm[i] - TLC_Regress[i])
        WS12_mm.append(Umformer(750,WS12_V[i]))
        WS12_abw.append(WS12_mm[i] - WS12_Regress[i])
    
    #Hysterese in mm 
    for i in range(len(MRU_Hys_V)):
        MRU_Hys_mm.append(Umformer(304.8, MRU_Hys_V[i]))
        TLI_Hys_mm.append(Umformer(400,TLI_Hys_V[i]))
        TLC_Hys_mm.append(Umformer(450,TLC_Hys_V[i]))
        WS12_Hys_mm.append(Umformer(750,WS12_Hys_V[i]))
    #Zeichen(MRU_mm, TLI_mm, TLC_mm, WS12_mm, Master)
    Regression(Prozent, WS12_mm, WS12_Regress)
    #Abweichung(Prozent, WS12_abw)
    #Hysterese(Prozent_Hys, MRU_Hys_mittel_mm, TLI_Hys_mittel_mm, TLC_Hys_mittel_mm, WS12_Hys_mittel_mm)