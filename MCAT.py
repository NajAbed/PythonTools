from sklearn.cluster import MiniBatchKMeans, KMeans
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import matplotlib.pyplot as plt
from Tkinter import *
import ttk
import numpy as np
from math import sqrt
import gc
gc.disable()
from Tkinter import Tk, Button, Frame, Canvas, Scrollbar
root = Tk()
root.title("Multivariate Visualization")
from scipy.stats.stats import pearsonr
from matplotlib.backend_bases import key_press_handler
from scipy.stats.mstats import mquantiles
#import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

  
car_file = open("csuamm.txt")
y=[]; yea=[]; j=[]; jslp=[]; jslp33=[]; jnino=[]; jnino33=[]; fmbu=[];fmbu33=[]; fm=[]; fm33=[]; fslp=[]; fslp33=[]; fsst=[]; fsst33=[]; n=[]; n33=[]; o=[]; o33=[]; sht=[]; sht33=[];jmbu=[]; jmbu33=[];
hu=[]; s=[]; nslp=[]; m=[]; hu33=[]; s33=[]; nslp33=[]; m33=[]; a33=[]; mslp33=[]; a=[]; mslp=[]; h56=[]; ih1=[]; ns=[];
aja=[]; ama=[]; aap=[]; am=[]; amf=[]; aju=[]; ajl=[]; aa=[]; ase=[]; ao=[]; an=[]; ad=[]; j33=[]; aja33=[]; ama33=[]; aap33=[]; am33=[]; amf33=[]; aju33=[]; ajl33=[]; aa33=[]; ase33=[]; ao33=[]; an33=[]; ad33=[]; j33=[]
for each in car_file:
        IH, H, NS, JunJulSST16, JunJulSLP10, JunJulNino1, Feb200MBU3,FebSLP5, FebMar200MBV4,\
        FebSST14, Sep500MBGeoHt7, NovSLP8, Nov500MBGeoHt12, MaySST2, Jul50MBU13, OctNovSLP6,\
        SepNovSLP11, AprMaySST15, MarAprSLP9, AMMJan, AMMFeb, AMMMar, AMMApr, AMMMay, AMMJun,\
        AMMJul, AMMAug, AMMSep, AMMOct, AMMNov, AMMDec, Year = each.split('\t')

        y.append(Year); yea.append(Year); j.append(JunJulSST16); j33.append(JunJulSST16);jslp.append(JunJulSLP10); jnino.append(JunJulNino1); fmbu.append(Feb200MBU3);
        fm.append(FebMar200MBV4); fslp.append(FebSLP5); fsst.append(FebSST14); jslp33.append(JunJulSLP10); jnino33.append(JunJulNino1); fmbu33.append(Feb200MBU3);
        fm33.append(FebMar200MBV4); fslp33.append(FebSLP5); fsst33.append(FebSST14);n.append(Nov500MBGeoHt12); n33.append(Nov500MBGeoHt12);o.append(OctNovSLP6);o33.append(OctNovSLP6);
        sht.append(Sep500MBGeoHt7); jmbu.append(Jul50MBU13); s.append(SepNovSLP11); nslp.append(NovSLP8); m.append(MaySST2); a.append(AprMaySST15);
        mslp.append(MarAprSLP9); sht33.append(Sep500MBGeoHt7); jmbu33.append(Jul50MBU13); s33.append(SepNovSLP11); nslp33.append(NovSLP8); m33.append(MaySST2); a33.append(AprMaySST15);
        mslp33.append(MarAprSLP9);h56.append(H); hu.append(H); ih1.append(IH); ns.append(NS); aja.append(AMMJan);amf.append(AMMFeb); ama.append(AMMMar); aap.append(AMMApr);
        am.append(AMMMay); aju.append(AMMJun); ajl.append(AMMJul); aa.append(AMMAug); ase.append(AMMSep); ao.append(AMMOct); an.append(AMMNov); ad.append(AMMDec);aja33.append(AMMJan);amf33.append(AMMFeb);
        ama33.append(AMMMar); aap33.append(AMMApr);am33.append(AMMMay); aju33.append(AMMJun); ajl33.append(AMMJul); aa33.append(AMMAug); ase33.append(AMMSep); ao33.append(AMMOct); an33.append(AMMNov); ad33.append(AMMDec); 
h=h56
for i in xrange(len(h)):
        h56[i]=float(h56[i])+0 
        j[i]=float(j[i])+0  
        j33[i]=float(j33[i])+0 
        y[i]=float(y[i])+0 
        jslp[i]=float(jslp[i])+0 
        jnino[i]=float(jnino[i])+0 
        fmbu[i]=float(fmbu[i])+0 
        fm[i]=float(fm[i])+0 
        fslp[i]=float(fslp[i])+0 
        fsst[i]=float(fsst[i])+0 
        n[i]=float(n[i])+0
        n33[i]=float(n33[i])+0 
        o[i]=float(o[i])+0
        o33[i]=float(o33[i])+0      
        sht[i]=float(sht[i])+0 
        jmbu[i]=float(jmbu[i])+0 
        s[i]=float(s[i])+0 
        nslp[i]=float(nslp[i])+0 
        m[i]=float(m[i])+0 
        a[i]=float(a[i])+0 
        mslp[i]=float(mslp[i])+0
        h56[i]=float(h56[i])+0 
        jslp33[i]=float(jslp[i])+0 
        jnino33[i]=float(jnino[i])+0 
        fmbu33[i]=float(fmbu[i])+0 
        fm33[i]=float(fm[i])+0 
        fslp33[i]=float(fslp[i])+0 
        fsst33[i]=float(fsst[i])+0 
        sht33[i]=float(sht[i])+0 
        jmbu33[i]=float(jmbu[i])+0 
        s33[i]=float(s[i])+0 
        nslp33[i]=float(nslp[i])+0 
        m33[i]=float(m[i])+0 
        a33[i]=float(a[i])+0 
        mslp33[i]=float(mslp[i])+0 
        h[i]=float(h[i])+0 
        ih1[i]=float(ih1[i])+0 
        ns[i]=float(ns[i])+0
        aja33[i]=float(aja33[i])+0
        amf33[i]=float(amf33[i])+0
        ama33[i]=float(ama33[i])+0
        aap33[i]=float(aap33[i])+0
        am33[i]=float(am33[i])+0
        aju33[i]=float(aju33[i])+0
        ajl33[i]=float(ajl33[i])+0
        aa33[i]=float(aa33[i])+0
        ase33[i]=float(ase33[i])+0
        ao33[i]=float(ao33[i])+0
        an33[i]=float(an33[i])+0
        ad33[i]=float(ad33[i])+0
       
h=ih1
rang=2006-1960+2
y33= [0 for x in range(rang)]
h33= [0 for x in range(rang)]
##print len(ns)
rang1=rang-1
for k in xrange(rang1):
        ff=k+10
        ##print ff
        y33[k]=y[ff]
        h33[k]=h[ff]

y6=y; j6=j; jslp6=jslp; jnino6=jnino; fmbu6=fmbu; fm6=fm; fslp6=fslp; fsst6=fsst; n6=n; o6=o; sht6=sht
jmbu6=jmbu;s6=s; nslp6=nslp; m6=m; a6=a; mslp6=mslp; 

for i in xrange(len(h)):
        #y6[i]=(y6[i]-min(y6))/(max(y6)-min(y6))
        j6[i]=(j6[i]-min(j))/(max(j)-min(j))
        jslp6[i]=(jslp6[i]-min(jslp))/(max(jslp)-min(jslp))
        jnino6[i]=(jnino6[i]-min(jnino))/(max(jnino)-min(jnino))
        fmbu6[i]=(fmbu6[i]-min(fmbu))/(max(fmbu)-min(fmbu))
        fm6[i]=(fm6[i]-min(fm))/(max(fm)-min(fm))
        fslp6[i]=(fslp6[i]-min(fslp))/(max(fslp)-min(fslp))
        fsst6[i]=(fsst6[i]-min(fsst))/(max(fsst)-min(fsst))
        n6[i]=(n6[i]-min(n))/(max(n)-min(n))
        o6[i]=(o6[i]-min(o))/(max(o)-min(o))
        sht6[i]=(sht6[i]-min(sht))/(max(sht)-min(sht))
        jmbu6[i]=(jmbu6[i]-min(jmbu))/(max(jmbu)-min(jmbu))
        s6[i]=(s6[i]-min(s))/(max(s)-min(s))
        nslp6[i]=(nslp6[i]-min(nslp))/(max(nslp)-min(nslp))
        m6[i]=(m6[i]-min(m))/(max(m)-min(m))
        a6[i]=(a6[i]-min(a))/(max(a)-min(a))
        mslp6[i]=(mslp6[i]-min(mslp))/(max(mslp)-min(mslp))


ensdata = [[0 for x in range(rang)] for x in range(16)]

data_input=[j6,jslp6,jnino6,fmbu6,fm6,fslp6,fsst6,n6,o6,sht6,jmbu6,s6,nslp6,m6,a6,mslp6]
for i in xrange(16):
        for j in xrange(rang):
                ensdata[i][j]= data_input[i][j]

h=ih1

mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

f = plt.figure(figsize=(17,5.8))
canvas = FigureCanvasTkAgg(f, master=mainframe)
canvas.get_tk_widget().configure(background='black', highlightbackground='black')
canvas.show()
canvas.get_tk_widget().grid(row=1, column=2, rowspan=6)
 
toolbar = NavigationToolbar2TkAgg(canvas, mainframe)
toolbar.update()
canvas._tkcanvas.grid(row=14, column=0, columnspan=3)

d= [0 for su1 in xrange(rang)]
x99= [0 for su1 in xrange(rang)]
y99= [0 for su1 in xrange(rang)]


import numpy.random as npr
def bootstrap(data1, data2, num_samples, statistic, alpha):
    num_samples=1000
    alpha=0.05
    n = len(data1)
    idx = npr.randint(0, n, (num_samples, n))
    samples1=  [[0 for x in range(idx.shape[1])] for x in range(idx.shape[0])]
    samples2=  [[0 for x in range(idx.shape[1])] for x in range(idx.shape[0])]
    #print(idx.shape)
    stat= [0 for su1 in xrange(idx.shape[0])]
    for i in xrange(idx.shape[0]):
            for j in xrange(idx.shape[1]):
                    samples1[i][j] = data1[idx[i][j]]
                    samples2[i][j] = data2[idx[i][j]]
            stat[i] = pearcor(samples1[i], samples2[i])
    stat= np.sort(stat)
    return (stat[int((alpha/2.0)*num_samples)], stat[int((1-alpha/2.0)*num_samples)])

def pearcor(data1, data2):
	return pearsonr(data1, data2)[0]

def corr(data1, data2):
    corr = pearcor(data1,data2)
    corrl, corrh = bootstrap(data1, data2, 100000, pearcor, 0.05)
    return corr,corrl,corrh

def corr2(data1, data2):
    corr = pearcor(data1,data2)
    return corr

 
ax = f.add_subplot(111,xlim=[1959,2008.8], ylim=[-1.9,8.7])
ax.set_axis_bgcolor('#969696')


import matplotlib.patches as mpatches

def filled_arc1(center, radius, theta1, theta2, ax, color):
    circ = mpatches.Wedge(center, radius, theta1, theta2, fill=True, color=color,zorder=0)
    ax.add_patch(circ)

theta1a=[330 for i in xrange(len(y33))]
theta2a=[360 for i in xrange(len(y33))]


for i in xrange(len(y33)):
        filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
        

def arcdraw(d3l,d3h,co):
                for i in xrange(len(y33)):
                    d3l[i]=float("%.2f" % round(d3l[i],2))
                    if 2.6<d3l[i]<=3:
                        theta1a[i]= d3l[i]-2.6+68
                    elif 2.4<d3l[i]<=2.6:
                        theta1a[i]= d3l[i]-2.4+66
                    elif 2.2<d3l[i]<=2.4:
                        theta1a[i]= d3l[i]-2.2+64
                    elif 2<d3l[i]<=2.2:
                        theta1a[i]= d3l[i]-2+63
                    elif 1.95<d3l[i]<=2:
                        theta1a[i]= d3l[i]-1.95+62
                    elif 1.9<d3l[i]<=1.95:
                        theta1a[i]= d3l[i]-1.9+61.5
                    elif 1.85<d3l[i]<=1.9:
                        theta1a[i]= d3l[i]-1.85+60.8
                    elif 1.80<d3l[i]<=1.85:
                        theta1a[i]= d3l[i]-1.8+60.5
                    elif 1.75<d3l[i]<=1.8:
                        theta1a[i]= d3l[i]-1.75+59.5
                    elif 1.7<d3l[i]<=1.75:
                        theta1a[i]= d3l[i]-1.7+58
                    elif 1.65<d3l[i]<=1.7:
                        theta1a[i]= d3l[i]-1.65+57.5
                    elif 1.6<d3l[i]<=1.65:
                        theta1a[i]= d3l[i]-1.6+57
                    elif 1.55<d3l[i]<=1.6:
                        theta1a[i]= d3l[i]-1.55+56
                    elif 1.5<d3l[i]<=1.55:
                        theta1a[i]= d3l[i]-1.5+55
                    elif 1.45<d3l[i]<=1.5:
                        theta1a[i]= d3l[i]-1.45+54
                    elif 1.4<d3l[i]<=1.45:
                        theta1a[i]= d3l[i]-1.4
                    elif 1.35<d3l[i]<=1.4:
                        theta1a[i]= d3l[i]-1.35+52
                    elif 1.3<d3l[i]<=1.35:
                        theta1a[i]= ((8)*(d3l[i]-1.3))*10+47
                    elif 1.25<d3l[i]<=1.3:
                        theta1a[i]= d3l[i]-1.25+50
                    elif 1.2<d3l[i]<=1.25:
                        theta1a[i]= d3l[i]-1.2+44.5
                    elif 1.15<d3l[i]<=1.2:
                        theta1a[i]= d3l[i]-1.15+48
                    elif 1.1<d3l[i]<=1.15:
                        theta1a[i]= d3l[i]-1.1+46.5
                    elif 1.05<d3l[i]<=1.1:
                        theta1a[i]= d3l[i]-1.05+45
                    elif 1<d3l[i]<=1.05:
                        theta1a[i]= (d3l[i]-1)+42
                    elif 0.9<d3l[i]<=1:
                        theta1a[i]= ((8)*(d3l[i]-0.9))*10+37
                    elif 0.85<d3l[i]<=0.9:
                        theta1a[i]= ((8)*(d3l[i]-0.85))*10+36
                    elif 0.83<d3l[i]<=0.85:
                        theta1a[i]= ((8)*(d3l[i]-0.83))*10+35
                    elif 0.8<d3l[i]<=0.83:
                        theta1a[i]= ((8)*(d3l[i]-0.8))*10+33
                    elif 0.7<d3l[i]<=0.75:
                        theta1a[i]= ((8)*(d3l[i]-0.7))*10+33
                    elif 0.75<d3l[i]<=0.8:
                        theta1a[i]= ((8)*(d3l[i]-0.75))*10+32
                    elif 0.6<d3l[i]<=0.7:
                        theta1a[i]= ((8)*(d3l[i]-0.6))*10+26
                    elif 0.52<d3l[i]<=0.6:
                        theta1a[i]= ((8)*(d3l[i]-0.52))*9+22
                    elif 0.50<d3l[i]<=0.52:
                        theta1a[i]= ((8)*(d3l[i]-0.5))*10+24
                    elif 0.4<d3l[i]<=0.5:
                        theta1a[i]= ((8)*(d3l[i]-0.4))*8+19
                    elif 0.3<d3l[i]<=0.4:
                        theta1a[i]= ((8)*(d3l[i]-0.3))*9+15
                    elif 0.2<d3l[i]<=0.3:
                        theta1a[i]= ((8)*(d3l[i]-0.2))*8+9
                    elif 0.1<d3l[i]<=0.2:
                        theta1a[i]= ((8)*(d3l[i]-0.1))*8+4
                    elif 0<d3l[i]<=0.1:
                        theta1a[i]= d3l[i]-0.1+1
                    elif -0.1<d3l[i]<=0:
                        theta1a[i]= ((360-355)*(d3l[i]+0.1))*10+355
                    elif -0.2<d3l[i]<=-0.1:
                        theta1a[i]= ((355-347)*(d3l[i]+0.2)*10)+348
                    elif -0.3<d3l[i]<=-0.2:
                        theta1a[i]= ((347-343)*(d3l[i]+0.3)*10)+345
                    elif -0.4<d3l[i]<=-0.3:
                        theta1a[i]= ((343-336)*(d3l[i]+0.4)*10)+336
                    elif -0.50<d3l[i]<=-0.4:
                        theta1a[i]= ((336-333)*(d3l[i]+0.50)*10)+335
                    elif -0.60<d3l[i]<=-0.50:
                        theta1a[i]= ((333-328)*(d3l[i]+0.6)*10)+330
                    elif -0.70<d3l[i]<=-0.60:
                        theta1a[i]= ((328-325)*(d3l[i]+0.7)*10)+327
                    elif -0.80<d3l[i]<=-0.70:
                        theta1a[i]= ((325-320)*(d3l[i]+0.8)*10)+324
                    elif -0.90<d3l[i]<=-0.80:
                        theta1a[i]= ((320-316)*(d3l[i]+0.9)*10)+320
                    elif -1<=d3l[i]<=-0.90:
                        theta1a[i]= ((316-310)*(d3l[i]+1)*10)+310                                     
                    elif -1.1<d3l[i]<=-1:
                        theta1a[i]= d3l[i]+1.2+318
                    elif -1.2<d3l[i]<=-1.1:
                        theta1a[i]= d3l[i]+1.2+314
                    elif -1.6<d3l[i]<=-1.2:
                        theta1a[i]= d3l[i]+1.6+307
                    elif -2<d3l[i]<=-1.6:
                        theta1a[i]= d3l[i]+2+304
                    elif -2.5<d3l[i]<=-2:
                        theta1a[i]= d3l[i]+2.5+298
                    elif -2.8<d3l[i]<=-2.5:
                        theta1a[i]= d3l[i]+3+294
                    elif -3<=d3l[i]<=-2.8:
                        theta1a[i]= d3l[i]+2.8+290
                    if 2.6<d3h[i]<=3:
                        theta2a[i]= d3h[i]-2.6+68
                    elif 2.4<d3h[i]<=2.6:
                        theta2a[i]= d3h[i]-2.4+66
                    elif 2.2<d3h[i]<=2.4:
                        theta2a[i]= d3h[i]-2.2+64
                    elif 2<d3h[i]<=2.2:
                        theta2a[i]= d3h[i]-2+63
                    elif 1.95<d3h[i]<=2:
                        theta2a[i]= d3h[i]-1.95+62
                    elif 1.9<d3h[i]<=1.95:
                        theta2a[i]= d3h[i]-1.9+61.5
                    elif 1.85<d3h[i]<=1.9:
                        theta2a[i]= d3h[i]-1.85+60.8
                    elif 1.80<d3h[i]<=1.85:
                        theta2a[i]= d3h[i]-1.8+60.5
                    elif 1.75<d3h[i]<=1.8:
                        theta2a[i]= d3h[i]-1.75+59.5
                    elif 1.7<d3h[i]<=1.75:
                        theta2a[i]= d3h[i]-1.7+58
                    elif 1.65<d3h[i]<=1.7:
                        theta2a[i]= d3h[i]-1.65+57.5
                    elif 1.6<d3h[i]<=1.65:
                        theta2a[i]= d3h[i]-1.6+57
                    elif 1.55<d3h[i]<=1.6:
                        theta2a[i]= d3h[i]-1.55+56
                    elif 1.5<d3h[i]<=1.55:
                        theta2a[i]= d3h[i]-1.5+55
                    elif 1.45<d3h[i]<=1.5:
                        theta2a[i]= d3h[i]-1.45+54
                    elif 1.4<d3h[i]<=1.45:
                        theta2a[i]= d3h[i]-1.4
                    elif 1.35<d3h[i]<=1.4:
                        theta2a[i]= d3h[i]-1.35+52
                    elif 1.3<d3h[i]<=1.35:
                        theta2a[i]= ((8)*(d3h[i]-1.3))*10+47
                    elif 1.25<d3h[i]<=1.3:
                        theta2a[i]= d3h[i]-1.25+50
                    elif 1.2<d3h[i]<=1.25:
                        theta2a[i]= d3h[i]-1.2+44.5
                    elif 1.15<d3h[i]<=1.2:
                        theta2a[i]= d3h[i]-1.15+48
                    elif 1.1<d3h[i]<=1.15:
                        theta2a[i]= d3h[i]-1.1+46.5
                    elif 1.05<d3h[i]<=1.1:
                        theta2a[i]= d3h[i]-1.05+45
                    elif 1<d3h[i]<=1.05:
                        theta2a[i]= (d3h[i]-1)+42
                    elif 0.9<d3h[i]<=1:
                        theta2a[i]= ((8)*(d3h[i]-0.9))*10+37
                    elif 0.85<d3h[i]<=0.9:
                        theta2a[i]= ((8)*(d3h[i]-0.85))*10+37
                    elif 0.83<d3h[i]<=0.85:
                        theta2a[i]= ((8)*(d3h[i]-0.83))*10+35
                    elif 0.8<d3h[i]<=0.83:
                        theta2a[i]= ((8)*(d3h[i]-0.8))*10+33
                    elif 0.7<d3h[i]<=0.75:
                        theta2a[i]= ((8)*(d3h[i]-0.7))*10+33
                    elif 0.75<d3h[i]<=0.8:
                        theta2a[i]= ((8)*(d3h[i]-0.75))*10+33
                    elif 0.6<d3h[i]<=0.7:
                        theta2a[i]= ((8)*(d3h[i]-0.6))*10+26
                    elif 0.52<d3h[i]<=0.6:
                        theta2a[i]= ((8)*(d3h[i]-0.52))*9+22
                    elif 0.50<d3h[i]<=0.52:
                        theta2a[i]= ((8)*(d3h[i]-0.5))*10+24
                    elif 0.4<d3h[i]<=0.5:
                        theta2a[i]= ((8)*(d3h[i]-0.4))*8+19
                    elif 0.3<d3h[i]<=0.4:
                        theta2a[i]= ((8)*(d3h[i]-0.3))*9+15
                    elif 0.2<d3h[i]<=0.3:
                        theta2a[i]= ((8)*(d3h[i]-0.2))*8+9
                    elif 0.1<d3h[i]<=0.2:
                        theta2a[i]= ((8)*(d3h[i]-0.1))*8+4
                    elif 0<d3h[i]<=0.1:
                        theta2a[i]= d3h[i]-0.1+1
                    elif -0.1<d3h[i]<=0:
                        theta2a[i]= ((360-355)*(d3h[i]+0.1))*10+355
                    elif -0.2<d3h[i]<=-0.1:
                        theta2a[i]= ((355-347)*(d3h[i]+0.2)*10)+348
                    elif -0.3<d3h[i]<=-0.2:
                        theta2a[i]= ((347-343)*(d3h[i]+0.3)*10)+345
                    elif -0.4<d3h[i]<=-0.3:
                        theta2a[i]= ((343-336)*(d3h[i]+0.4)*10)+336
                    elif -0.50<d3h[i]<=-0.4:
                        theta2a[i]= ((336-333)*(d3h[i]+0.50)*10)+335
                    elif -0.60<d3h[i]<=-0.50:
                        theta2a[i]= ((333-328)*(d3h[i]+0.6)*10)+330
                    elif -0.70<d3h[i]<=-0.60:
                        theta2a[i]= ((328-325)*(d3h[i]+0.7)*10)+327
                    elif -0.80<d3h[i]<=-0.70:
                        theta2a[i]= ((325-320)*(d3h[i]+0.8)*10)+324
                    elif -0.90<d3h[i]<=-0.80:
                        theta2a[i]= ((320-316)*(d3h[i]+0.9)*10)+320
                    elif -1<=d3h[i]<=-0.90:
                        theta2a[i]= ((316-310)*(d3h[i]+1)*10)+310                                     
                    elif -1.1<d3h[i]<=-1:
                        theta2a[i]= d3h[i]+1.2+318
                    elif -1.2<d3h[i]<=-1.1:
                        theta2a[i]= d3h[i]+1.2+314
                    elif -1.6<d3h[i]<=-1.2:
                        theta2a[i]= d3h[i]+1.6+307
                    elif -2<d3h[i]<=-1.6:
                        theta2a[i]= d3h[i]+2+304
                    elif -2.5<d3h[i]<=-2:
                        theta2a[i]= d3h[i]+2.5+298
                    elif -2.8<d3h[i]<=-2.5:
                        theta2a[i]= d3h[i]+3+294
                    elif -3<=d3h[i]<=-2.8:
                        theta2a[i]= d3h[i]+2.8+290
             
                for i in xrange(len(y33)):
                        filled_arc1((y33[i], h33[i]), 1.7, theta1a[i], theta2a[i], ax, co)


##class AnyObject(object):
##    pass
##class AnyObject1(object):
##    pass
##class AnyObject2(object):
##    pass
##class AnyObject3(object):
##    pass
##class AnyObject4(object):
##    pass
##
##class AnyObjectHandler(object):
##    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
##        x0, y0 = handlebox.xdescent, handlebox.ydescent
##        width, height = 16,16#handlebox.width, handlebox.height
##        patch = mpatches.Rectangle([x0-5, y0], width, height, facecolor='#969696',
##                                   edgecolor='#fff5eb', hatch='/', lw=0,
##                                   transform=handlebox.get_transform())
##        handlebox.add_artist(patch)
##        return patch
##
##class AnyObjectHandler1(object):
##    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
##        x0, y0 = handlebox.xdescent, handlebox.ydescent
##        width, height = 16,16#handlebox.width, handlebox.height
##        patch = mpatches.Rectangle([x0, y0+2], width, height, facecolor='#969696',
##                                   edgecolor='#fff5eb', hatch='-/', lw=0,
##                                   transform=handlebox.get_transform())
##        handlebox.add_artist(patch)
##        return patch
##class AnyObjectHandler2(object):
##    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
##        x0, y0 = handlebox.xdescent, handlebox.ydescent
##        width, height = 16,16#handlebox.width, handlebox.height
##        patch = mpatches.Rectangle([x0+5, y0-2], width, height, facecolor='#969696',
##                                   edgecolor='#fff5eb', hatch='-', lw=0,
##                                   transform=handlebox.get_transform())
##        handlebox.add_artist(patch)
##        return patch
##class AnyObjectHandler3(object):
##    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
##        x0, y0 = handlebox.xdescent, handlebox.ydescent
##        width, height = 16,16#handlebox.width, handlebox.height
##        patch = mpatches.Rectangle([x0+7, y0-6], width, height, facecolor='#969696',
##                                   edgecolor='#fff5eb', hatch='\-', lw=0,
##                                   transform=handlebox.get_transform())
##        handlebox.add_artist(patch)
##        return patch
##class AnyObjectHandler4(object):
##    def legend_artist(self, legend, orig_handle, fontsize, handlebox):
##        x0, y0 = handlebox.xdescent, handlebox.ydescent
##        width, height = 16,16#handlebox.width, handlebox.height
##        patch = mpatches.Rectangle([x0+3, y0-4], width, height, facecolor='#969696',
##                                   edgecolor='#fff5eb', hatch='\\', lw=0,
##                                   transform=handlebox.get_transform())
##        handlebox.add_artist(patch)
##        return patch

"""f.legend([AnyObject(),AnyObject1(),AnyObject2(),AnyObject3(),AnyObject4()], ['+1','(0,+1)','0','(-1,0)','-1'],
           handler_map={AnyObject: AnyObjectHandler(),AnyObject1: AnyObjectHandler1(),AnyObject2: AnyObjectHandler2(),AnyObject3: AnyObjectHandler3(),AnyObject4: AnyObjectHandler4()})
"""

def clearpage():
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()


def setup_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= o33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5

                x, y = event.x, event.y
                #print(x,y)#(172,429)   (172,49)  (1236,429)  (1236,49)
                x2=((x-172)/21.36)+1959#x2=((x-322)/40)+1959
                y2= ((y-49)/35.85)-1.9  #y2= ((y-65)/49.34)-1.9 
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or o1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: OctNovSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0009,linewidth=0,scale=1/0.035,color= '#00441b')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#238b45')
                        canvas.show()
                        

def onclickOctNovSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= o33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3
                
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                font = {'family': 'serif',
                        'color':  'darkred',
                        'weight': 'normal',
                        'size': 16,
                        }
                if event.key=='a':
                    arcdraw(d3l,d3h,'#238b45')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#00441b', label='Model length11111111')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: OctNovSLP average', color='#00441b',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#238b45',size=14)

                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()

def OctNovSLP1():
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= o33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5

                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#00441b')
                canvas.show()

                f.canvas.mpl_connect('key_press_event', onclickOctNovSLP)
                f.canvas.mpl_connect('motion_notify_event', setup_annotation)

                if (o1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: OctNovSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        #arcdraw(d3l,d3h,'#969696')
                        canvas.show()
      

def JunJulSST_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= j33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5

                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or j1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSST average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0009,linewidth=0,scale=1/0.035,color= '#4d004b')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#4d004b')
                        canvas.show()

def onclickJunJulSST(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= j33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3 
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='b':
                    arcdraw(d3l,d3h,'#88419d')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#4d004b')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSST average', color='#4d004b',size=14)#fontdict=font)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#88419d',size=14)#'fontdict=font)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()
                
def JunJulSST161():
                ax.set_visible(True)
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= j33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                #print d3   
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                aa=ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#4d004b')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickJunJulSST)
                f.canvas.mpl_connect('motion_notify_event', JunJulSST_annotation)
                if (j1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSST average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()
                
def Nov500MBGeoHt_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= n33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or n1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Nov500MBGeoHt average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0009,linewidth=0,scale=1/0.035,color= '#084081')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#084081')
                        canvas.show()

def onclickNov500MBGeoHt(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= n33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3 

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='c':
                    ww=arcdraw(d3l,d3h,'#2b8cbe')
                    ee=plt.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#084081',zorder=1)
                    ax.text(y33[rang/2],h33[1]+1, ' -->: Nov500MBGeoHt average', color='#084081',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#2b8cbe',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()                
                
def Nov500MBGeoHt1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= n33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#084081')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickNov500MBGeoHt)
                f.canvas.mpl_connect('motion_notify_event', Nov500MBGeoHt_annotation)
                if (n1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Nov500MBGeoHt average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def SepNovSLP_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= s33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or s1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: SepNovSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0009,linewidth=0,scale=1/0.035,color= '#7f0000')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#7f0000')
                        canvas.show()


def onclickSepNovSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= s33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='d':
                    arcdraw(d3l,d3h,'#d7301f')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#7f0000')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: SepNovSLP average', color='#7f0000',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#d7301f',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()                
                
def SepNovSLP1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= s33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#7f0000')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickSepNovSLP)
                f.canvas.mpl_connect('motion_notify_event', SepNovSLP_annotation)
                if (s1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: SepNovSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def FebMar200MB_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fm33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or fm1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebMar200MB average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0007,linewidth=0,scale=1/0.035,color= '#67001f')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#67001f')
                        canvas.show()
                        
def onclickFebMar200MB(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fm33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='e':
                    arcdraw(d3l,d3h,'#ce1256')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#67001f')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: FebMar200MBV average', color='#67001f',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#ce1256',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()                

def FebMar200MBV41():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fm33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#67001f')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickFebMar200MB)
                f.canvas.mpl_connect('motion_notify_event', FebMar200MB_annotation)
                if (fm1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebMar200MB average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def JunJulSLP_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or jslp1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#2b8cbe')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#2b8cbe')
                        canvas.show()
                        
def onclickJunJulSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jslp33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                  
                mind=min(d3)
                maxd=max(d3)
                mindl=min(d3l)
                maxdl=max(d3l)
                mindh=min(d3h)
                maxdh=max(d3h)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='z':
                    if (jslp1.get()== 1):
                        arcdraw(d3l,d3h,'#7bccc4')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#2b8cbe')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSLP average', color='#2b8cbe',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#7bccc4',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()                
                
def JunJulSLP101():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 

                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#2b8cbe')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickJunJulSLP)
                f.canvas.mpl_connect('motion_notify_event', JunJulSLP_annotation)
                if (jslp1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def JunJulNino_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jnino33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or jnino1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulNino average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#49006a')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#49006a')
                        canvas.show()
                        

def onclickJunJulNino(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jnino33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='g':
                    arcdraw(d3l,d3h,'#ae017e')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#49006a')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulNino average', color='#49006a',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#ae017e',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()                
                
def JunJulNino11():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jnino33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#49006a')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickJunJulNino)
                f.canvas.mpl_connect('motion_notify_event', JunJulNino_annotation)
                if (jnino1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: JunJulNino average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def Feb200MBU_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fmbu33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or fmbu1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Feb200MBU average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#662506')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#662506')
                        canvas.show()
                        
def onclickFeb200MBU(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fmbu33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='h':
                    arcdraw(d3l,d3h,'#cc4c02')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#662506')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: Feb200MBU average', color='#662506',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#cc4c02',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def Feb200MBU31():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fmbu33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#662506')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickFeb200MBU)
                f.canvas.mpl_connect('motion_notify_event', Feb200MBU_annotation)
                if (fmbu1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Feb200MBU average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def FebSLP_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or fslp1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#41ae76')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#bcbddc')
                        canvas.show()

def onclickFebSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fslp33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='i':
                    arcdraw(d3l,d3h,'#99d8c9')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#41ae76')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: FebSLP average', color='#41ae76',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#99d8c9',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def FebSLP51():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#41ae76')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickFebSLP)
                f.canvas.mpl_connect('motion_notify_event', FebSLP_annotation)
                if (fslp1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def FebSST_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fsst33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or fsst1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebSST average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#8c6bb1')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#8c6bb1')
                        canvas.show()
                        

def onclickFebSST(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fsst33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='j':
                    arcdraw(d3l,d3h,'#9ebcda')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#8c6bb1')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: FebSST average', color='#8c6bb1',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#9ebcda',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def FebSST141():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= fsst33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#8c6bb1')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickFebSST)
                f.canvas.mpl_connect('motion_notify_event', FebSST_annotation)
                if (fsst1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: FebSST average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def Sep500MBGeoHt_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= sht33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or sht1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Sep500MBGeoHt average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#4eb3d3')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#d95f0e')
                        canvas.show()

def onclickSep500MBGeoHt(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= sht33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3  
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='k':
                    arcdraw(d3l,d3h,'#a8ddb5')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#4eb3d3')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: Sep500MBGeoHt average', color='#4eb3d3',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#a8ddb5',size=14)
                event.canvas.draw()
                
                
def Sep500MBGeoHt71():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= sht33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#4eb3d3')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickSep500MBGeoHt)
                f.canvas.mpl_connect('motion_notify_event', Sep500MBGeoHt_annotation)
                if (sht1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Sep500MBGeoHt average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def Jul50MBU_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jmbu33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or jmbu1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Jul50MBU average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#ef6548')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#ef6548')
                        canvas.show()
                        
def onclickJul50MBU(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jmbu33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='l':
                    arcdraw(d3l,d3h,'#fdbb84')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#ef6548')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: Jul50MBU average', color='#ef6548',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#fdbb84',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def Jul50MBU131():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= jmbu33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#ef6548')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickJul50MBU)
                f.canvas.mpl_connect('motion_notify_event', Jul50MBU_annotation)
                if (jmbu1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: Jul50MBU average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def NovSLP_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= nslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or nslp1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: NovSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#e7298a')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#e7298a')
                        canvas.show()
                        
def onclickNovSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= nslp33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='m':
                    arcdraw(d3l,d3h,'#c994c7')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#e7298a')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: NovSLP average', color='#e7298a',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#c994c7',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def NovSLP81():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= nslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#e7298a')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickNovSLP)
                f.canvas.mpl_connect('motion_notify_event', NovSLP_annotation)
                if (nslp1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: NovSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def MaySST_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= m33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or m1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: MaySST average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#f768a1')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#f768a1')
                        canvas.show()
                        
def onclickMaySST(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= m33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='n':
                    arcdraw(d3l,d3h,'#fcc5c0')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#f768a1')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: MaySST average', color='#f768a1',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#fcc5c0',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def MaySST21():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= m33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#f768a1')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickMaySST)
                f.canvas.mpl_connect('motion_notify_event', MaySST_annotation)
                if (m1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: MaySST average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()
                                        
def AprMaySST_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= a33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or a1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AprMaySST average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#78c679')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#78c679')
                        canvas.show()

def onclickAprMaySST(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= a33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='o':
                    arcdraw(d3l,d3h,'#d9f0a3')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#78c679')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AprMaySST average', color='#78c679',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#d9f0a3',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AprMaySST151():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= a33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#78c679')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAprMaySST)
                f.canvas.mpl_connect('motion_notify_event', AprMaySST_annotation)
                if (a1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AprMaySST average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def MarAprSLP_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= mslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or mslp1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: MarAprSLP average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#41b6c4')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#41b6c4')
                        canvas.show()
                        
def onclickMarAprSLP(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= mslp33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='p':
                    arcdraw(d3l,d3h,'#c7e9b4')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#41b6c4')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: MarAprSLP average', color='#41b6c4',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#c7e9b4',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def MarAprSLP91():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= mslp33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#41b6c4')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickMarAprSLP)
                f.canvas.mpl_connect('motion_notify_event', MarAprSLP_annotation)
                if (mslp1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: MarAprSLP average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()
                        

def clustering1():

                temp1=ensdata
                batch_size=100  
                mbk = MiniBatchKMeans(init='k-means++', n_clusters=3, batch_size=batch_size,
                      n_init=10, max_no_improvement=10, verbose=0)
                mbk.fit(temp1)
                mbk_means_labels = mbk.labels_ 
                mbk_means_cluster_centers = mbk.cluster_centers_ 
                mbk_meas_labels_unique = np.unique(mbk_means_labels)
                temp4=mbk_means_labels[0:(rang)]
                for i in xrange(len(temp4)):
                        if (temp4[i]==2):
                                temp4[i]=336
                        if (temp4[i]==1):
                                temp4[i]=100
                        if (temp4[i]==0):
                                temp4[i]=25
                ax.scatter(y33,h33,temp4,alpha=1,c='#2b8cbe')
                canvas.show()
                if (cluster1.get()== 0):
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        canvas.show()

def AMMJan_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aja33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or aja1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJan average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#ec7014')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#ec7014')
                        canvas.show()

def onclickAMMJan(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aja33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='q':
                    arcdraw(d3l,d3h,'#fec44f')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#ec7014')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJan average', color='#ec7014',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#fec44f',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
                
def AMMJan1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aja33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#ec7014')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMJan)
                f.canvas.mpl_connect('motion_notify_event', AMMJan_annotation)
                if (aja1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJan average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def AMMFeb_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= amf33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or amf1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMFeb average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#fe9929')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#fe9929')
                        canvas.show()

                        
                
def onclickAMMFeb(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= amf33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='4':
                    arcdraw(d3l,d3h,'#fee391')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#fe9929')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMFeb average', color='#fe9929',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#fee391',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
def AMMFeb1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= amf33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#fe9929')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMFeb)
                f.canvas.mpl_connect('motion_notify_event', AMMFeb_annotation)
                if (amf1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMFeb average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMMar_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ama33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or ama1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMar average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#fc4e2a')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#fc4e2a')
                        canvas.show()

def onclickAMMMar(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ama33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='5':
                    arcdraw(d3l,d3h,'#feb24c')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#fc4e2a')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMar average', color='#fc4e2a',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#feb24c',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()
                        
def AMMMar1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ama33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#fc4e2a')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMMar)
                f.canvas.mpl_connect('motion_notify_event', AMMMar_annotation)
                if (ama1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMar average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMApr_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aap33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or aap1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMApr average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#fed976')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#fed976')
                        canvas.show()

def onclickAMMApr(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aap33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='t':
                    arcdraw(d3l,d3h,'#ffffcc')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#fed976')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMApr average', color='#fed976',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#ffffcc',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMApr1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aap33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#fed976')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMApr)
                f.canvas.mpl_connect('motion_notify_event', AMMApr_annotation)
                if (aap1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMApr average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMMay_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= am33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or am1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMay average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        ##print "it is"
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#006d2c')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#006d2c')
                        canvas.show()

def onclickAMMMay(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= am33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='u':
                    arcdraw(d3l,d3h,'#66c2a4')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#006d2c')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMay average', color='#006d2c',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#66c2a4',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                                
def AMMMay1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= am33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#006d2c')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMMay)
                f.canvas.mpl_connect('motion_notify_event', AMMMay_annotation)
                if (am1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMMay average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def AMMJun_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aju33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or aju1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJun average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#810f7c')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#810f7c')
                        canvas.show()

def onclickAMMJun(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aju33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='v':
                    arcdraw(d3l,d3h,'#8c96c6')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#810f7c')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJun average', color='#810f7c',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#8c96c6',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMJun1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aju33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#810f7c')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMJun)
                f.canvas.mpl_connect('motion_notify_event', AMMJun_annotation)
                if (aju1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJun average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMJul_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ajl33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or ajl1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJul average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#0868ac')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#0868ac')
                        canvas.show()
                        
def onclickAMMJul(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ajl33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3 
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='w':
                    arcdraw(d3l,d3h,'#7bccc4')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#0868ac')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJul average', color='#0868ac',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#7bccc4',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMJul1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ajl33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#0868ac')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMJul)
                f.canvas.mpl_connect('motion_notify_event', AMMJul_annotation)
                if (ajl1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMJul average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMAug_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aa33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or aa1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMAug average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#7f2704')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#7f2704')
                        canvas.show()
                        
                        
def onclickAMMAug(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aa33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     
 
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='x':
                    arcdraw(d3l,d3h,'#d94801')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#7f2704')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMAug average', color='#7f2704',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#d94801',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMAug1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= aa33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#7f2704')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMAug)
                f.canvas.mpl_connect('motion_notify_event', AMMAug_annotation)
                if (aa1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMAug average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def AMMSep_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ase33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or ase1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMSep average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#a63603')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#a63603')
                        canvas.show()
                        
def onclickAMMSep(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ase33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     
     
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='y':
                    arcdraw(d3l,d3h,'#f16913')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#a63603')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMSep average', color='#a63603',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#f16913',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMSep1():
                tt=10
                d3= [0 for x in range(rang)]
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ase33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#a63603')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMSep)
                f.canvas.mpl_connect('motion_notify_event', AMMSep_annotation)
                if (ase1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMSep average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()


def AMMOct_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ao33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or ao1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMOct average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#fd8d3c')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#fd8d3c')
                        canvas.show()
                        
def onclickAMMOct(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ao33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     
 
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='1':
                    arcdraw(d3l,d3h,'#fdd0a2')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#fd8d3c')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMOct average', color='#fd8d3c',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#fdd0a2',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                        
def AMMOct1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ao33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#fd8d3c')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMOct)
                f.canvas.mpl_connect('motion_notify_event', AMMOct_annotation)
                if (ao1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMOct average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMNov_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= an33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or an1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMNov average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#3f007d')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#3f007d')
                        canvas.show()

                        
def onclickAMMNov(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= an33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3                     

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='2':
                    arcdraw(d3l,d3h,'#6a51a3')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#3f007d')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMNov average', color='#3f007d',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#6a51a3',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
                
def AMMNov1():
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= an33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#3f007d')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMNov)
                f.canvas.mpl_connect('motion_notify_event', AMMNov_annotation)
                if (an1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMNov average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()

def AMMDec_annotation(event):
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ad33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                mind=min(d3)
                maxd=max(d3)
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                x, y = event.x, event.y
                x2=((x-172)/21.36)+1959
                y2= ((y-49)/35.85)-1.9               
                for i in xrange(len(y33)):
                    if i==len(y33)-2 or ad1.get()== 0:
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMDec average', color='#969696',size=14)
                        break

                    if (((x2-y33[i])**2+(y2-h33[i])**2)**0.5<0.2):
                        v=i+1
                        ax.quiver([y33[i],y33[v]],[h33[i],h33[v]],[vx3[i],vx3[v]],[vy3[i],vy3[v]],width=0.0015,linewidth=0,scale=1/0.035,color= '#54278f')
                        canvas.show()
                    elif(((x2-y33[i])**2+(y2-h33[i])**2)**0.5<1) and (((x2-y33[i])**2+(y2-h33[i])**2)**0.5>=0.2):
                        j=i+1
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0030,linewidth=0,scale=1/0.035,color= '#bdbdbd')
                        ax.quiver([y33[i],y33[j]],[h33[i],h33[j]],[vx3[i],vx3[j]],[vy3[i],vy3[j]],width=0.0007,linewidth=0,scale=1/0.035,color= '#54278f')
                        canvas.show()
                        
def onclickAMMDec(event):
                tt=10
                d3= [0 for x in range(rang)]
                d3l= [0 for x in range(rang)]
                d3h= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ad33[i]
                    tt=tt+1
                    d3[k], d3l[k], d3h[k]=corr(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    if(0<d3l[i]<=0.1) or (-0.1<d3l[i]<=0):
                        d3l[i]=d3l[i]*1.07
                    elif(0.1<d3l[i]<=0.2) or (-0.2<d3l[i]<=-0.1):
                        d3l[i]=d3l[i]*1.1
                    elif(0.2<d3l[i]<=0.3) or (-0.3<d3l[i]<=-0.2):
                        d3l[i]=d3l[i]*1.2
                    elif(0.3<d3l[i]<=0.4) or (-0.4<d3l[i]<=-0.3):
                        d3l[i]=d3l[i]*1.3
                    elif(0.4<d3l[i]<=0.5) or (-0.5<d3l[i]<=-0.4):
                        d3l[i]=d3l[i]*1.4
                    elif(0.5<d3l[i]<=0.6) or (-0.6<d3l[i]<=-0.5):
                        d3l[i]=d3l[i]*1.5
                    elif(0.6<d3l[i]<=0.7) or (-0.7<d3l[i]<=-0.6):
                        d3l[i]=d3l[i]*1.7
                    elif(0.7<d3l[i]<=0.8) or (-0.8<d3l[i]<=-0.7):
                        d3l[i]=d3l[i]*2.1
                    elif(0.8<d3l[i]<=0.9) or (-0.9<d3l[i]<=-0.8):
                        d3l[i]=d3l[i]*2.5
                    elif(0.9<d3l[i]<=1) or (-1<d3l[i]<=-0.9):
                        d3l[i]=d3l[i]*3
                    if(0<d3h[i]<=0.1) or (-0.1<d3h[i]<=0):
                        d3h[i]=d3h[i]*1.07
                    elif(0.1<d3h[i]<=0.2) or (-0.2<d3h[i]<=-0.1):
                        d3h[i]=d3h[i]*1.1
                    elif(0.2<d3h[i]<=0.3) or (-0.3<d3h[i]<=-0.2):
                        d3h[i]=d3h[i]*1.2
                    elif(0.3<d3h[i]<=0.4) or (-0.4<d3h[i]<=-0.3):
                        d3h[i]=d3h[i]*1.3
                    elif(0.4<d3h[i]<=0.5) or (-0.5<d3h[i]<=-0.4):
                        d3h[i]=d3h[i]*1.4
                    elif(0.5<d3h[i]<=0.6) or (-0.6<d3h[i]<=-0.5):
                        d3h[i]=d3h[i]*1.5
                    elif(0.6<d3h[i]<=0.7) or (-0.7<d3h[i]<=-0.6):
                        d3h[i]=d3h[i]*1.7
                    elif(0.7<d3h[i]<=0.8) or (-0.8<d3h[i]<=-0.7):
                        d3h[i]=d3h[i]*2.1
                    elif(0.8<d3h[i]<=0.9) or (-0.9<d3h[i]<=-0.8):
                        d3h[i]=d3h[i]*2.5
                    elif(0.9<d3h[i]<=1) or (-1<=d3h[i]<=-0.9):
                        d3h[i]=d3h[i]*3 

                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                vx3l=[0 for xv in range(rang)]
                vy3l=[0 for xv in range(rang)]
                vx3h=[0 for xv in range(rang)]
                vy3h=[0 for xv in range(rang)]
                for i in xrange(rang):
                        vx3[i]=1/(1+d3[i]**2)**0.5
                        vy3[i]=d3[i]/(1+d3[i]**2)**0.5
                        vx3l[i]=1/(1+d3l[i]**2)**0.5
                        vy3l[i]=d3l[i]/(1+d3l[i]**2)**0.5
                        vx3h[i]=1/(1+d3h[i]**2)**0.5
                        vy3h[i]=d3h[i]/(1+d3h[i]**2)**0.5 
                key_press_handler(event, canvas, toolbar)
                if event.key=='3':
                    arcdraw(d3l,d3h,'#807dba')
                    ax.quiver(y33,h33,vx3,vy3, width=0.0007,linewidth=0,scale=1/0.035,color= '#54278f')
                    ax.text(y33[rang/2],h33[1]+1, ' -->: AMMDec average', color='#54278f',size=14)
                    ax.text(y33[rang/2],h33[1], ' --: Bootstrap Higher and Lower values', color='#807dba',size=14)
                event.canvas.draw()
                if event.key=='$':
                        plt.cla()
                        plt.xlabel('Year', fontsize=18)
                        plt.ylabel('Number of Intense Hurricanes', fontsize=18)
                        ax.set_xlim([1959,2008.1])
                        ax.set_ylim([-1,9])
                        plt.plot(y,h,color= '#fdae6b')
                        for i in xrange(len(y33)):
                            filled_arc1((y33[i], h33[i]), 1.7, 290, 70, ax, '#bdbdbd')
                        canvas.show()  
def AMMDec1():
                tt=10
                tt=10
                d3= [0 for x in range(rang)]
                for k in xrange(rang):
                    data1= [0 for x in range(tt)]
                    data2= [0 for x in range(tt)]
                    for i in xrange(tt):
                        data1[i]= h[i]
                        data2[i]= ad33[i]
                    tt=tt+1
                    d3[k]=corr2(data1, data2)
                for i in xrange(rang):
                    if(0<d3[i]<=0.1) or (-0.1<d3[i]<=0):
                        d3[i]=d3[i]*1.07
                    elif(0.1<d3[i]<=0.2) or (-0.2<d3[i]<=-0.1):
                        d3[i]=d3[i]*1.1
                    elif(0.2<d3[i]<=0.3) or (-0.3<d3[i]<=-0.2):
                        d3[i]=d3[i]*1.2
                    elif(0.3<d3[i]<=0.4) or (-0.4<d3[i]<=-0.3):
                        d3[i]=d3[i]*1.3
                    elif(0.4<d3[i]<=0.5) or (-0.5<d3[i]<=-0.4):
                        d3[i]=d3[i]*1.4
                    elif(0.5<d3[i]<=0.6) or (-0.6<d3[i]<=-0.5):
                        d3[i]=d3[i]*1.5
                    elif(0.6<d3[i]<=0.7) or (-0.7<d3[i]<=-0.6):
                        d3[i]=d3[i]*1.7
                    elif(0.7<d3[i]<=0.8) or (-0.8<d3[i]<=-0.7):
                        d3[i]=d3[i]*2.1
                    elif(0.8<d3[i]<=0.9) or (-0.9<d3[i]<=-0.8):
                        d3[i]=d3[i]*2.5
                    elif(0.9<d3[i]<=1) or (-1<d3[i]<=-0.9):
                        d3[i]=d3[i]*3 
                    
                vx3=[0 for xv in range(rang)]
                vy3=[0 for xv in range(rang)]
                for i in xrange(rang):
                    vx3[i]=1/(1+d3[i]**2)**0.5
                    vy3[i]=d3[i]/(1+d3[i]**2)**0.5 
                ax.quiver(y33,h33,vx3,vy3,width=0.0007,linewidth=0,scale=1/0.035,color= '#54278f')
                canvas.show()
                cid = f.canvas.mpl_connect('key_press_event', onclickAMMDec)
                f.canvas.mpl_connect('motion_notify_event', AMMDec_annotation)
                if (ad1.get()== 0):
                        ax.text(y33[rang/2],h33[1]+1, ' -->: AMMDec average', color='#969696',size=14)
                        ax.quiver(y33,h33,vx3,vy3,width=0.0040,linewidth=0,scale=1/0.038,color= '#bdbdbd')
                        canvas.show()
                  

#OctNovSLP Entry
o1 = IntVar()
sampleSize = Checkbutton(mainframe, text="OctNovSLP(a)", variable = o1, command=OctNovSLP1,selectcolor="#00441b",borderwidth=0,pady =0,highlightthickness=0)
sampleSize.grid(column = 0, row = 0, sticky = W)
#sampleSize.pack
#JunJulSST16 Entry
j1 = IntVar()
JunJulSST162 = Checkbutton(mainframe, text="JunJulSST(b)", variable=j1, command=JunJulSST161,selectcolor="#4d004b",borderwidth=0,pady =0,highlightthickness=0)
JunJulSST162.grid(column = 0, row = 1, sticky = W)
 
#Nov500MBGeoHt Entry
n1 = IntVar()
binsize = Checkbutton(mainframe, text="Nov500MBGeoHt(c)", variable=n1, command=Nov500MBGeoHt1,selectcolor="#084081",borderwidth=0,pady =0,highlightthickness=0)
binsize.grid(column = 0, row = 2, sticky = W)
 
#SepNovSLP Entry
s1 = IntVar()
Humiditysize = Checkbutton(mainframe, text="SepNovSLP(d)", variable=s1, command=SepNovSLP1,selectcolor="#7f0000",borderwidth=0,pady =0,highlightthickness=0)
Humiditysize.grid(column = 0, row = 3, sticky = W)#(W, E))

#FebMar200MBV4 Entry
fm1 = IntVar()
FebMar200MBV42 = Checkbutton(mainframe, text="FebMar200MBV(e)", variable=fm1, command=FebMar200MBV41,selectcolor="#67001f",borderwidth=0,pady =0,highlightthickness=0)
FebMar200MBV42.grid(column = 0, row = 4, sticky = W)#(W, E))

#JunJulSLP10 Entry
jslp1 = IntVar()
JunJulSLP102 = Checkbutton(mainframe, text="JunJulSLP(z)", variable = jslp1, command=JunJulSLP101,selectcolor="#2b8cbe",borderwidth=0,pady =0,highlightthickness=0)
JunJulSLP102.grid(column = 0, row = 5, sticky = W)
 
#JunJulNino1 Entry
jnino1 = IntVar()
JunJulNino12 = Checkbutton(mainframe, text="JunJulNino(g)", variable = jnino1, command=JunJulNino11,selectcolor="#49006a",borderwidth=0,pady =0,highlightthickness=0)
JunJulNino12.grid(column = 1, row = 5, sticky = W)

#Feb200MBU3 Entry
fmbu1 = IntVar()
Feb200MBU32 = Checkbutton(mainframe, text="Feb200MBU(h)", variable = fmbu1, command=Feb200MBU31,selectcolor="#662506",borderwidth=0,pady =0,highlightthickness=0)
Feb200MBU32.grid(column = 0, row = 6, sticky = W)

#FebSLP5 Entry
fslp1 = IntVar()
FebSLP52 = Checkbutton(mainframe, text="FebSLP(i)", variable = fslp1, command=FebSLP51,selectcolor="#41ae76",borderwidth=0,pady =0,highlightthickness=0)
FebSLP52.grid(column = 0, row =7 , sticky = W)

#FebSST14 Entry
fsst1 = IntVar()
FebSST142 = Checkbutton(mainframe, text="FebSST(j)", variable = fsst1, command=FebSST141,selectcolor="#8c6bb1",borderwidth=0,pady =0,highlightthickness=0)
FebSST142.grid(column = 0, row = 8, sticky = W)

#Sep500MBGeoHt7 Entry
sht1 = IntVar()
Sep500MBGeoHt712 = Checkbutton(mainframe, text="Sep500MBGeoHt(k)", variable = sht1, command=Sep500MBGeoHt71,selectcolor="#4eb3d3",borderwidth=0,pady =0,highlightthickness=0)
Sep500MBGeoHt712.grid(column = 0, row = 9, sticky = W)

#Jul50MBU13 Entry
jmbu1 = IntVar()
Jul50MBU132 = Checkbutton(mainframe, text="Jul50MBU(l)", variable = jmbu1, command=Jul50MBU131,selectcolor="#ef6548",borderwidth=0,pady =0,highlightthickness=0)
Jul50MBU132.grid(column = 0, row =10 , sticky = W)

#NovSLP8 Entry
nslp1 = IntVar()
NovSLP82 = Checkbutton(mainframe, text="NovSLP(m)", variable = nslp1, command=NovSLP81,selectcolor="#e7298a",borderwidth=0,pady =0,highlightthickness=0)
NovSLP82.grid(column = 0, row =11 , sticky = W)

#MaySST2 Entry
m1 = IntVar()
MaySST22 = Checkbutton(mainframe, text="MaySST(n)", variable = m1, command=MaySST21,selectcolor="#f768a1",borderwidth=0,pady =0,highlightthickness=0)
MaySST22.grid(column = 0, row =12 , sticky = W)

#AprMaySST15 Entry
a1 = IntVar()
AprMaySST152 = Checkbutton(mainframe, text="AprMaySST(o)", variable = a1, command=AprMaySST151,selectcolor="#41ab5d",borderwidth=0,pady =0,highlightthickness=0)
AprMaySST152.grid(column = 0, row =13 , sticky = W)
      
#MarAprSLP9 Entry
mslp1 = IntVar()
MarAprSLP92 = Checkbutton(mainframe, text="MarAprSLP(p)", variable = mslp1, command=MarAprSLP91,selectcolor="#41b6c4",borderwidth=0,pady =0,highlightthickness=0)
MarAprSLP92.grid(column = 1, row =0 , sticky = W)

#AMMJan Entry
aja1 = IntVar()
AMMJan2 = Checkbutton(mainframe, text="AMMJan(q)", variable=aja1, command=AMMJan1,selectcolor='#ec7014',borderwidth=0,pady =0,highlightthickness=0)
AMMJan2.grid(column = 1, row = 1, sticky = W)#(W, E))

#AMMFeb Entry
amf1 = IntVar()
AMMFeb2 = Checkbutton(mainframe, text="AMMFeb(4)", variable = amf1, command=AMMFeb1,selectcolor='#fe9929',borderwidth=0,pady =0,highlightthickness=0)
AMMFeb2.grid(column = 1, row = 2, sticky = W)
 
#AMMMar Entry
ama1 = IntVar()
AMMMar2 = Checkbutton(mainframe, text="AMMMar(5)", variable = ama1, command=AMMMar1,selectcolor='#fc4e2a',borderwidth=0,pady =0,highlightthickness=0)
AMMMar2.grid(column = 1, row = 3, sticky = W)

#AMMApr Entry
aap1 = IntVar()
AMMApr2 = Checkbutton(mainframe, text="AMMApr(t)", variable = aap1, command=AMMApr1,selectcolor='#fed976',borderwidth=0,pady =0,highlightthickness=0)
AMMApr2.grid(column = 1, row = 4, sticky = W)

#AMMMay Entry
am1 = IntVar()
AMMMay2 = Checkbutton(mainframe, text="AMMMay(u)", variable = am1, command=AMMMay1,selectcolor='#006d2c',borderwidth=0,pady =0,highlightthickness=0)
AMMMay2.grid(column = 1, row =5 , sticky = W)

#AMMJun Entry
aju1 = IntVar()
AMMJun2 = Checkbutton(mainframe, text="AMMJun(v)", variable = aju1, command=AMMJun1,selectcolor='#810f7c',borderwidth=0,pady =0,highlightthickness=0)
AMMJun2.grid(column = 1, row = 6, sticky = W)

#AMMJul Entry
ajl1 = IntVar()
AMMJul2 = Checkbutton(mainframe, text="AMMJul(w)", variable = ajl1, command=AMMJul1,selectcolor='#0868ac',borderwidth=0,pady =0,highlightthickness=0)
AMMJul2.grid(column = 1, row = 7, sticky = W)

#AMMAug Entry
aa1 = IntVar()
AMMAug2 = Checkbutton(mainframe, text="AMMAug(x)", variable = aa1, command=AMMAug1,selectcolor='#7f2704',borderwidth=0,pady =0,highlightthickness=0)
AMMAug2.grid(column = 1, row =8 , sticky = W)

#AMMSep Entry
ase1 = IntVar()
AMMSep2 = Checkbutton(mainframe, text="AMMSep(y)", variable = ase1, command=AMMSep1,selectcolor='#a63603',borderwidth=0,pady =0,highlightthickness=0)
AMMSep2.grid(column = 1, row =9 , sticky = W)

#AMMOct Entry
ao1 = IntVar()
AMMOct2 = Checkbutton(mainframe, text="AMMOct(1)", variable = ao1, command=AMMOct1,selectcolor='#fd8d3c',borderwidth=0,pady =0,highlightthickness=0)
AMMOct2.grid(column = 1, row =10 , sticky = W)

#AMMNov Entry
an1 = IntVar()
AMMNov2 = Checkbutton(mainframe, text="AMMNov(2)", variable = an1, command=AMMNov1,selectcolor='#3f007d',borderwidth=0,pady =0,highlightthickness=0)
AMMNov2.grid(column = 1, row =11 , sticky = W)
      
#AMMDec Entry
ad1 = IntVar()
AMMDec2 = Checkbutton(mainframe, text="AMMDec(3)", variable = ad1, command=AMMDec1,selectcolor='#54278f',borderwidth=0,pady =0,highlightthickness=0)
AMMDec2.grid(column = 1, row =12 , sticky = W)

#clear Entry
cp1 = IntVar()
clearp2 = Checkbutton(mainframe, text="Clear Page", variable = cp1, command=clearpage,selectcolor='#969696',borderwidth=0,pady =0,highlightthickness=0)
clearp2.grid(column = 2, row =0 , sticky = W)

#clustering Entry
cluster1 = IntVar()
cluster2 = Checkbutton(mainframe, text="Clustering", variable = cluster1, command=clustering1,selectcolor="#2b8cbe",borderwidth=0,pady =0,highlightthickness=0)
cluster2.grid(column = 2, row =1 , sticky = W)

plt.plot(y,h,color= '#fdae6b')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Number of Intense Hurricanes', fontsize=18)

for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1)
root.mainloop()
