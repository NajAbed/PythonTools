import random
import matplotlib, sys
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from Tkinter import *
#from Tkinter import ttk
import ttk
import matplotlib as mpl 
import numpy as np
from netCDF4 import Dataset
import matplotlib.colors as mcolors
nz = mcolors.Normalize()
import matplotlib.cm as cm
import matplotlib.colorbar as mcolorbar
#fig = plt.figure(figsize=(18,8))
from mpl_toolkits.basemap import Basemap
from math import sqrt
from random import randint
from sklearn.cluster import MiniBatchKMeans, KMeans
from scipy.stats.stats import pearsonr
import matplotlib.patches as mpatches
import gc
gc.disable()
from Tkinter import Tk, Button, Frame, Canvas, Scrollbar
import Tkconstants
root = Tk()
root.title("Multivariate Visualization")

url='C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_18_00_00.nc'
l=[]
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_18_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_19_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_20_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_21_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_22_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-01_23_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_00_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_01_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_02_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_03_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_04_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_05_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_06_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_07_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_08_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_09_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_10_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_11_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_12_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_13_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_14_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_15_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_16_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_17_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_18_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_19_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_20_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_21_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_22_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-02_23_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_00_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_01_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_02_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_03_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_04_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_05_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_06_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_07_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_08_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_09_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_10_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_11_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_12_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_13_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_14_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_15_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_16_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_17_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_18_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_19_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_20_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_21_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_22_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-03_23_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_00_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_01_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_02_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_03_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_04_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_05_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_06_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_07_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_08_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_09_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_10_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_11_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_12_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_13_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_14_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_15_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_16_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_17_00_00.nc")
l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/ens_01/wrfprs_1999-03-04_18_00_00.nc")
dset = Dataset(url)
lats = dset.variables['g3_lat_0'][:]
lons = dset.variables['g3_lon_1'][:]
lons=lons[:,:]
lats=lats[:,:]
pres = dset.variables['PRMSL_GDS3_MSL'][:]
height = dset.variables['HGT_GDS3_ISBL'][:]
length=len(lons)
length2=71
interval=72
a=42
b=48
lstl=5
devision=b-a+1
d = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
d1 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
d3 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
d31 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
d32 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
d33 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]

u1=[[0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
u2=[[0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
u3=[[0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
u4=[[0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
u5=[[0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]

 
#mainframe
mainframe = ttk.Frame(root, padding = "3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


  
#histogram embed
f = plt.figure(figsize=(14,6))
#f = Figure(figsize=(8,4), dpi=100)
canvas = FigureCanvasTkAgg(f, master=mainframe)
#canvas.show()
canvas.get_tk_widget().grid(row=1, column=2, rowspan=6)
 
toolbar = NavigationToolbar2TkAgg(canvas, mainframe)
toolbar.update()
canvas._tkcanvas.grid(row=14, column=0, columnspan=3)

dset = Dataset(url)
lats = dset.variables['g3_lat_0'][:]
lons = dset.variables['g3_lon_1'][:]



class new():
	def __init__(self):
		master = Tk()

		e = Entry(master)
		e.pack()

		e.focus_set()
		b = Button(master, text="get", width=10, command=callback(self))
		b.pack()
		return e.get()
	
	def callback(self):
		print(e.get())
		return e.get()
		    


def tilevathree():
	master = Tk()
	master.title("Time")
	w1 = Label(master, text="Time")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Predictor1")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()
	w4 = Label(master, text="Predictor2")
	e4 = Entry(master)
	e4.pack()
	w4.pack()
	e4.focus_set()
	w8 = Label(master, text="Predictand")
	e8 = Entry(master)
	e8.pack()
	w8.pack()
	e8.focus_set()	
	w5 = Label(master, text="Color")
	e5 = Entry(master)
	e5.pack()
	w5.pack()
	e5.focus_set()
	w6 = Label(master, text="Radius")
	e6 = Entry(master)
	e6.pack()
	w6.pack()
	e6.focus_set()
	w7 = Label(master, text="Time Range")
	e7 = Entry(master)
	e7.pack()
	w7.pack()
	e7.focus_set()

	def callback():
		master.quit()
		return (e1.get(),e2.get(),e3.get(), e4.get(),e8.get(),e5.get(),e6.get(),e7.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return (e1.get(),e2.get(),e3.get(),e4.get(),e8.get(),e5.get(),e6.get(),e7.get())


def tilevatwo():
	master = Tk()
	master.title("Time")
	w1 = Label(master, text="Time")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable1")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()
	w4 = Label(master, text="Variable2")
	e4 = Entry(master)
	e4.pack()
	w4.pack()
	e4.focus_set()
	w5 = Label(master, text="Color")
	e5 = Entry(master)
	e5.pack()
	w5.pack()
	e5.focus_set()
	w6 = Label(master, text="Radius")
	e6 = Entry(master)
	e6.pack()
	w6.pack()
	e6.focus_set()
	w7 = Label(master, text="Time Range")
	e7 = Entry(master)
	e7.pack()
	w7.pack()
	e7.focus_set()	

	def callback():
		master.quit()
		return (e1.get(),e2.get(),e3.get(), e4.get(),e5.get(),e6.get(),e7.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return (e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get())





def tileva():
	master = Tk()
	master.title("Time")
	w1 = Label(master, text="Time")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()

	def callback():
		master.quit()
		return (e1.get(),e2.get(),e3.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return (e1.get(),e2.get(),e3.get())



def onetime():
	master = Tk()
	master.title("Time")
	w1 = Label(master, text="Timestep")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()

	def callback():
		master.quit()
		return (e1.get(),e2.get(),e3.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return(e1.get(),e2.get(),e3.get())


def twotime():
	master = Tk()
	master.title("Time")
	w1 = Label(master, text="Start Time")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w4 = Label(master, text="End Time")
	e4 = Entry(master)
	e4.pack()
	w4.pack()
	e4.focus_set()	
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()
	w5 = Label(master, text="Color")
	e5 = Entry(master)
	e5.pack()
	w5.pack()
	e5.focus_set()
	
	def callback():
		master.quit()
		return (e1.get(),e4.get(),e2.get(),e3.get(),e5.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return(e1.get(),e4.get(),e2.get(),e3.get(),e5.get())	

def timer():
	master = Tk()
	master.title("Time")
	w = Label(master, text="Time")
	e = Entry(master)
	e.pack()
	w.pack()
	e.focus_set()

	def callback():
		master.quit()
		return (e.get())

	b = Button(master, text="Process", width=10, command=callback)
	b.pack()
	
	mainloop()
	return(e.get())


def locationr():
	master = Tk()
	master.title("Time and Radius")
	w = Label(master, text="Time")
	e = Entry(master)
	e.pack()
	w.pack()
	e.focus_set()

	w1 = Label(master, text="Radius")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable1")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()
	w4 = Label(master, text="Variable2")
	e4 = Entry(master)
	e4.pack()
	w4.pack()
	e4.focus_set()	
	def callback():
		master.quit()
		return (e.get(),e1.get(),e2.get(),e3.get(),e4.get())

	b = Button(master, text="Process", width=10, command=callback)
##	print(e.get())        
	b.pack()
	
	mainloop()
	return(e.get(),e1.get(),e2.get(),e3.get(),e4.get())


def val():
	master = Tk()
	#master.title("Time Starting and Ending")
	w = Label(master, text="Start Time")
	e = Entry(master)
	e.pack()
	w.pack()
	e.focus_set()

	w1 = Label(master, text="End Time")
	e1 = Entry(master)
	e1.pack()
	w1.pack()
	e1.focus_set()
	w2 = Label(master, text="Level")
	e2 = Entry(master)
	e2.pack()
	w2.pack()
	e2.focus_set()
	w3 = Label(master, text="Variable1")
	e3 = Entry(master)
	e3.pack()
	w3.pack()
	e3.focus_set()
	w4 = Label(master, text="Variable2")
	e4 = Entry(master)
	e4.pack()
	w4.pack()
	e4.focus_set()	

	def callback():
		master.quit()
		return (e.get(),e1.get(),e2.get(),e3.get(),e4.get())

	b = Button(master, text="Process", width=10, command=callback)
##	print(e.get())        
	b.pack()
	
	mainloop()
	return(e.get(),e1.get(),e2.get(),e3.get(),e4.get())

	

def pearcor(data1, data2):
	return pearsonr(data1, data2)[0]


def fvariable(url):
		dset = Dataset(url)
		pres = dset.variables['PRMSL_GDS3_MSL'][:]
		height = dset.variables['HGT_GDS3_ISBL'][:]
		temp = dset.variables['TMP_GDS3_ISBL'][:]
		windu = dset.variables['U_GRD_GDS3_ISBL'][:]
		windv = dset.variables['V_GRD_GDS3_ISBL'][:]
		humid = dset.variables['SPF_H_GDS3_ISBL'][:]
		temp=np.matrix(temp[19,:,:])
		pres=np.matrix(pres[:,:])
		height=np.matrix(height[19,:,:])
		humid=np.matrix(humid[19,:,:])
		windu=np.array(windu[19,:,:])
		windv=np.array(windv[19,:,:])
		return temp, pres, height, humid, windu, windv

ax1 = f.add_subplot(111)
#m = Basemap(width=9000000,height=7000000,projection='lcc',  resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-97., ax=ax1)
m = Basemap(llcrnrlon=-145.5,llcrnrlat=1.,urcrnrlon=-2.566,urcrnrlat=46.352,\
			rsphere=(6378137.00,6356752.3142),\
			resolution='l',area_thresh=1000.,projection='lcc',\
			lat_1=23.5,lon_0=-80)
ny = lons.shape[0]; nx = lons.shape[1]
lons1, lats1 = m(lons, lats)
mint=lons.min();maxt=lons.max();bground=(lons-mint)/(maxt-mint)*5
#1 + (x-A)*(10-1)/(B-A)
#bground = lons/10
#bground = lons/5
#bground = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
im=ax1.pcolor(lons1,lats1,bground, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
ax1.cla()
cbar = f.colorbar(im)



xScrollbar = Scrollbar(mainframe, orient=Tkconstants.HORIZONTAL)
yScrollbar = Scrollbar(mainframe)

xScrollbar.grid(row=22, column=0, sticky=Tkconstants.EW)
yScrollbar.grid(row=21, column=0, sticky=Tkconstants.NS)

canvas1 = Canvas(mainframe)
canvas1.config(xscrollcommand=xScrollbar.set)
xScrollbar.config(command=canvas1.xview)
canvas1.config(yscrollcommand=yScrollbar.set)
yScrollbar.config(command=canvas1.yview)


##mplCanvas = canvas.get_tk_widget()
##factor =2
##cwid = canvas1.create_window(0, 0, window=mplCanvas, anchor=Tkconstants.NW)
##oldSize = f.get_size_inches()
##f.set_size_inches([factor * s for s in oldSize])
##wi,hi = [i*f.dpi for i in f.get_size_inches()]
##mplCanvas.config(width=wi, height=hi)
##canvas1.itemconfigure(cwid, width=wi, height=hi)
##canvas1.config(scrollregion=canvas1.bbox(Tkconstants.ALL),width=200,height=200)
##tz.set_fontsize(tz.get_fontsize()*factor)
##for item in ([ax1.title, ax1.xaxis.label, ax1.yaxis.label] + ax1.get_xticklabels() + ax1.get_yticklabels()):
##        item.set_fontsize(item.get_fontsize()*factor)
##ax.xaxis.labelpad = ax.xaxis.labelpad*factor
##ax.yaxis.labelpad = ax.yaxis.labelpad*factor
##f.subplots_adjust(left=0.2, bottom=0.15, top=0.86)
##f.canvas1.draw() 

  
def prestemphumid1():
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']

				b, level, varn1, varn2, varn3, co ,r ,timedis= tilevathree()
				b= int(b); level= int(level); timedis= int(timedis); r= int(r)
				timestep=b
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep+1]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]

				if varn1== 'PRMSL_GDS3_MSL':
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp3=(windu**2+windv**2)**0.5
				else:
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[level,:,:])
				if varn2== 'PRMSL_GDS3_MSL':
					pres = dset.variables[varn2][:]
					pres3=np.array(pres[:,:])
				elif varn2== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					pres3=(windu**2+windv**2)**0.5
				else:
					pres = dset.variables[varn2][:]
					pres3=np.array(pres[level,:,:])
				if varn3== 'PRMSL_GDS3_MSL':
					height = dset.variables[varn3][:]
					height3=np.array(height[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					height3=(windu**2+windv**2)**0.5
				else:
					height = dset.variables[varn3][:]
					height3=np.array(height[level,:,:])					
				minh=height3.min();maxh=height3.max();height3=(height3-minh)/(maxh-minh)
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				height3=height3.ravel()
				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3 = height3.reshape(len(height3), 1)
				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				for j in xrange(timedis):
					timestep=timestep+1
					for i in xrange(29):
							enrand=ensembles[i]
							url=ensrand(enrand)[timestep]
							dset = Dataset(url)
							if varn1== 'PRMSL_GDS3_MSL':
								temp = dset.variables[varn1][:]
								temp=np.array(temp[:,:])
							elif varn1== 'UV_GRD_GDS3_ISBL':
								windu = dset.variables['U_GRD_GDS3_ISBL'][:]
								windv = dset.variables['V_GRD_GDS3_ISBL'][:]
								windu=np.array(windu[level,:,:])
								windv=np.array(windv[level,:,:])
								temp=(windu**2+windv**2)**0.5
							else:
								temp = dset.variables[varn1][:]
								temp=np.array(temp[level,:,:])
							if varn2== 'PRMSL_GDS3_MSL':
								pres = dset.variables[varn2][:]
								pres=np.array(pres[:,:])
							elif varn2== 'UV_GRD_GDS3_ISBL':
								windu = dset.variables['U_GRD_GDS3_ISBL'][:]
								windv = dset.variables['V_GRD_GDS3_ISBL'][:]
								windu=np.array(windu[level,:,:])
								windv=np.array(windv[level,:,:])
								pres=(windu**2+windv**2)**0.5
							else:
								pres = dset.variables[varn2][:]
								pres=np.array(pres[level,:,:])
							if varn3== 'PRMSL_GDS3_MSL':
								height = dset.variables[varn3][:]
								height=np.array(height[:,:])
							elif varn3== 'UV_GRD_GDS3_ISBL':
								windu = dset.variables['U_GRD_GDS3_ISBL'][:]
								windv = dset.variables['V_GRD_GDS3_ISBL'][:]
								windu=np.array(windu[level,:,:])
								windv=np.array(windv[level,:,:])
								height=(windu**2+windv**2)**0.5
							else:
								height = dset.variables[varn3][:]
								height=np.array(height[level,:,:])

							minh=height.min();maxh=height.max();height=(height-minh)/(maxh-minh)
							mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
							minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
							height=height.ravel()
							temp=temp.ravel()
							pres=pres.ravel()
							height3 = np.insert(height3, 0, height, axis=1)
							temp3 = np.insert(temp3, 0, temp, axis=1)
							pres3 = np.insert(pres3, 0, pres, axis=1)

				dtp = [0 for x in range(temp3.shape[0])]
				dth = [0 for x in range(temp3.shape[0])]
				dph = [0 for x in range(temp3.shape[0])]
				d = [0 for x in range(temp3.shape[0])]
				#d=np.array(d);dtp=np.array(dtp);dth=np.array(dth);dph=np.array(dph)
				leng=175
				for i in xrange(temp3.shape[0]):
					xx=temp3[i,:]
					yy=pres3[i,:]
					zz=height3[i,:]
					if (i-1>=0):
						xx=np.append(xx,temp3[i-1,:])
						yy=np.append(yy,pres3[i-1,:])
						zz=np.append(zz,height3[i-1,:])
					else:
						pass
					if (i-2>=0):
						xx=np.append(xx,temp3[i-2,:])
						yy=np.append(yy,pres3[i-2,:])
						zz=np.append(zz,height3[i-2,:])
					else:
						pass
					if (i+1<temp3.shape[0]):
						xx=np.append(xx,temp3[i+1,:])
						yy=np.append(yy,pres3[i+1,:])
						zz=np.append(zz,height3[i+1,:])
					else:
						pass
					if (i+2<temp3.shape[0]):
						xx=np.append(xx,temp3[i+2,:])
						yy=np.append(yy,pres3[i+2,:])
						zz=np.append(zz,height3[i+2,:])
					else:
						pass
					if (i-157>=0):
						xx=np.append(xx,temp3[i-157,:])
						yy=np.append(yy,pres3[i-157,:])
						zz=np.append(zz,height3[i-157,:])
					else:
						pass
					if (i-(157*2)>=0):
						xx=np.append(xx,temp3[i-(157*2),:])
						yy=np.append(yy,pres3[i-(157*2),:])
						zz=np.append(zz,height3[i-(157*2),:])
					if (i+157<temp3.shape[0]):    
						xx=np.append(xx,temp3[i+157,:])
						yy=np.append(yy,pres3[i+157,:])
						zz=np.append(zz,height3[i+157,:])
					else:
						pass
					if (i+(157*2)<temp3.shape[0]):
						xx=np.append(xx,temp3[i+(157*2),:])
						yy=np.append(yy,pres3[i+(157*2),:])
						zz=np.append(zz,height3[i+(157*2),:])
					else:
						pass          
					t1 = pearcor(xx, yy)
					#dtp[i] = t1
					#print dtp[i],pearcor(xx, yy),temporary
					#dth[i]=pearcor(xx, zz)
					t2 = pearcor(xx, zz)
					#dph[i]=pearcor(yy, zz)
					t3=pearcor(yy, zz)

##					if t1==1:
##							t1=0.999
##					if t2==1:
##							t2=0.999
##					if t3==1:
##							t3=0.999
					vv=t2*t2#t1*t1
					
					xx=t3*t3#t2*t2*0.16
					zz=2*t2*t3*t1#2*(t1*t1*t2*0.064)
					gg=1-(t1*t1)#1-(t3*t3*0.4)
					d[i]= ((vv+xx-zz)/gg)**0.5
					#print d[i]
				
				d1=np.array(d)
				maxp = d1.max()
				minp = d1.min()
				#d1=-1*(1-((d1-minp)/(maxp-minp)))+((d1-minp)/(maxp-minp))
				#print d1
				vx1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vy1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vx1=np.array(vx1)
				vy1=np.array(vy1)
				d5=np.array(d1)
				#print d5.shape
				#print lons.shape[0]
				d6=d5.reshape(lons.shape[0],lons.shape[1])
				for i in xrange(length):
						vx1[i]=1/(1+d6[i]**2)**0.5
						vy1[i]=d6[i]/(1+d6[i]**2)**0.5                 
				for i in xrange(0,lons.shape[0],lstl):
						for j in xrange(0,lons.shape[1],lstl):
							ax1.quiver(lons1[i][j],lats1[i][j],vx1[i][j],vy1[i][j],width=0.001,linewidth=0.1,scale=1/0.015,color= co)
				canvas.show()
				if vprestemphumid.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()

				
						
def presinc1():
				a , b, level, varn1, co = twotime();
				a= int(a); b= int(b); level=int(level)
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']

				enrand=ensembles[29]
				url=ensrand(enrand)[a]
				dset = Dataset(url)
				if varn1== 'PRMSL_GDS3_MSL':
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp3=(windu**2+windv**2)**0.5
				else:
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[level,:,:])


				enrand=ensembles[29]
				url=ensrand(enrand)[b]
				dset2 = Dataset(url)
				if varn1== 'PRMSL_GDS3_MSL':
					temp = dset2.variables[varn1][:]
					temp31=np.array(temp[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset2.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset2.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp31=(windu**2+windv**2)**0.5
				else:
					temp = dset2.variables[varn1][:]
					temp31=np.array(temp[level,:,:])
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				temp3=temp3.ravel()
				temp3 = temp3.reshape(len(temp3), 1)
				mint=temp31.min();maxt=temp31.max();temp31=(temp31-mint)/(maxt-mint)
				temp31=temp31.ravel()
				temp31 = temp31.reshape(len(temp31), 1)

				for i in xrange(29):
					enrand=ensembles[i]
					url=ensrand(enrand)[a]
					dset = Dataset(url)
					url1=ensrand(enrand)[b]
					dset1 = Dataset(url1)

					if varn1== 'PRMSL_GDS3_MSL':
						temp = dset.variables[varn1][:]
						temp=np.array(temp[:,:])
						temp1 = dset1.variables[varn1][:]
						temp1=np.array(temp1[:,:])
					elif varn1== 'UV_GRD_GDS3_ISBL':
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						windu=np.array(windu[level,:,:])
						windv=np.array(windv[level,:,:])
						temp=(windu**2+windv**2)**0.5
						windu1 = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv1 = dset.variables['V_GRD_GDS3_ISBL'][:]
						windu1=np.array(windu1[level,:,:])
						windv1=np.array(windv1[level,:,:])
						temp1=(windu1**2+windv1**2)**0.5
					else:
						temp = dset.variables[varn1][:]
						temp=np.array(temp[level,:,:])
						temp1 = dset1.variables[varn1][:]
						temp1=np.array(temp1[level,:,:])
					mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
					temp=temp.ravel()
					temp3 = np.insert(temp3, 0, temp, axis=1)
					mint=temp1.min();maxt=temp1.max();temp1=(temp1-mint)/(maxt-mint)
					temp1=temp1.ravel()
					temp31 = np.insert(temp31, 0, temp1, axis=1)
				x1=[0.0 for xv in range(temp3.shape[0])]
				x1=np.array(x1)
				for i in xrange(temp3.shape[0]):
					x1[i]=np.mean(temp3[i,:])
				x1=x1.reshape(lons.shape[0],lons.shape[1])
				
				x2=[0.0 for xv in range(temp31.shape[0])]
				x2=np.array(x2)
				for i in xrange(temp31.shape[0]):
					x2[i]=np.mean(temp31[i,:])
				x2=x2.reshape(lons.shape[0],lons.shape[1])
				x=x2-x1
				for i in xrange(0,lons.shape[0],lstl):
					for j in xrange(0,lons.shape[1],lstl):
						if(x[i][j]>0) :
							ax1.scatter(lons1[i][j],lats1[i][j],c= co)
				
				#ax1.contour(lons1,lats1,x[:,:])
				canvas.show()
				if vpresinc.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()

def pres1():
				a ,level, varn1 = onetime();
				a= int(a); level=int(level)
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']

				enrand=ensembles[29]
				url=ensrand(enrand)[a]
				dset = Dataset(url)
				if varn1== 'PRMSL_GDS3_MSL':
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp3=(windu**2+windv**2)**0.5
				else:
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[level,:,:])
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				temp3=temp3.ravel()
				temp3 = temp3.reshape(len(temp3), 1)
				for i in xrange(29):
					enrand=ensembles[i]
					url=ensrand(enrand)[a]
					dset = Dataset(url)

					if varn1== 'PRMSL_GDS3_MSL':
						temp = dset.variables[varn1][:]
						temp=np.array(temp[:,:])
					elif varn1== 'UV_GRD_GDS3_ISBL':
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						windu=np.array(windu[level,:,:])
						windv=np.array(windv[level,:,:])
						temp=(windu**2+windv**2)**0.5
					else:
						temp = dset.variables[varn1][:]
						temp=np.array(temp[level,:,:])
					mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
					#minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
					temp=temp.ravel()
					#pres=pres.ravel()
					temp3 = np.insert(temp3, 0, temp, axis=1)
					#pres3 = np.insert(pres3, 0, pres, axis=1)
				x1=[0.0 for xv in range(temp3.shape[0])]
				x1=np.array(x1)
				for i in xrange(temp3.shape[0]):
					x1[i]=np.mean(temp3[i,:])
				x1=x1.reshape(lons.shape[0],lons.shape[1])

				ax1.contour(lons1,lats1,x1[:,:])
				canvas.show()
				if vPressure.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()
def preshumid1():

				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
				b, level, varn1, varn2, co ,r ,timedis= tilevatwo()
				b= int(b); level= int(level); timedis= int(timedis); r= int(r)
				timestep=b


				#timestep=a-1
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep+1]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]

				if varn1== 'PRMSL_GDS3_MSL':
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[:,:])
				elif varn1== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp3=(windu**2+windv**2)**0.5
				else:
					temp = dset.variables[varn1][:]
					temp3=np.array(temp[level,:,:])
				if varn2== 'PRMSL_GDS3_MSL':
					pres = dset.variables[varn2][:]
					pres3=np.array(pres[:,:])
				elif varn2== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					pres3=(windu**2+windv**2)**0.5
				else:
					pres = dset.variables[varn2][:]
					pres3=np.array(pres[level,:,:])

				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				temp3=temp3.ravel()
				pres3=pres3.ravel()
				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				for j in xrange(timedis):
					timestep=timestep+1
					for i in xrange(29):
							enrand=ensembles[i]
							url=ensrand(enrand)[timestep]
							dset = Dataset(url)

							if varn1== 'PRMSL_GDS3_MSL':
								temp = dset.variables[varn1][:]
								temp=np.array(temp[:,:])
							elif varn1== 'UV_GRD_GDS3_ISBL':
								windu = dset.variables['U_GRD_GDS3_ISBL'][:]
								windv = dset.variables['V_GRD_GDS3_ISBL'][:]
								windu=np.array(windu[level,:,:])
								windv=np.array(windv[level,:,:])
								temp=(windu**2+windv**2)**0.5
							else:
								temp = dset.variables[varn1][:]
								temp=np.array(temp[level,:,:])
							if varn2== 'PRMSL_GDS3_MSL':
								pres = dset.variables[varn2][:]
								pres=np.array(pres[:,:])
							elif varn2== 'UV_GRD_GDS3_ISBL':
								windu = dset.variables['U_GRD_GDS3_ISBL'][:]
								windv = dset.variables['V_GRD_GDS3_ISBL'][:]
								windu=np.array(windu[level,:,:])
								windv=np.array(windv[level,:,:])
								pres=(windu**2+windv**2)**0.5
							else:
								pres = dset.variables[varn2][:]
								pres=np.array(pres[level,:,:])

							mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
							minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
							temp=temp.ravel()
							pres=pres.ravel()
							temp3 = np.insert(temp3, 0, temp, axis=1)
							pres3 = np.insert(pres3, 0, pres, axis=1)

				d33 = [0 for x in range(temp3.shape[0])] 
				for i in xrange(temp3.shape[0]):
					xx=temp3[i,:]
					yy=pres3[i,:]
					for k in xrange(r):
						if((i-k)>=0):
							xx=np.append(xx,temp3[i-k,:])
							yy=np.append(yy,pres3[i-k,:])
						else:
							pass
						if ((i+k)<temp3.shape[0]):
							xx=np.append(xx,temp3[i+k,:])
							yy=np.append(yy,pres3[i+k,:])
						else:
							pass
						if (i-(157*k)>=0):
							xx=np.append(xx,temp3[i-(157*k),:])
							yy=np.append(yy,pres3[i-(157*k),:])
						else:
							pass
						if (i+(157*k)<temp3.shape[0]):    
							xx=np.append(xx,temp3[i+(157*k),:])
							yy=np.append(yy,pres3[i+(157*k),:])
						else:
							pass
						if (i-(157*k)-k>=0):
							xx=np.append(xx,temp3[i-(157*k)-k,:])
							yy=np.append(yy,pres3[i-(157*k)-k,:])
						else:
							pass
						if (i+(157*k-k)<temp3.shape[0]):    
							xx=np.append(xx,temp3[i+(157*k)-k,:])
							yy=np.append(yy,pres3[i+(157*k)-k,:])
						else:
							pass
						if (i-(157*k)+k>=0):
							xx=np.append(xx,temp3[i-(157*k)+k,:])
							yy=np.append(yy,pres3[i-(157*k)+k,:])
						else:
							pass
						if (i+(157*k)+k<temp3.shape[0]):    
							xx=np.append(xx,temp3[i+(157*k)+k,:])
							yy=np.append(yy,pres3[i+(157*k)+k,:])
						else:
							pass                                                
					d33[i]=pearcor(xx, yy)

				vx1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vy1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vx1=np.array(vx1)
				vy1=np.array(vy1)
				d5=np.array(d33)
				d6=d5.reshape(lons.shape[0],lons.shape[1])
				for i in xrange(length):
						vx1[i]=1/(1+d6[i]**2)**0.5
						vy1[i]=d6[i]/(1+d6[i]**2)**0.5                 
				for i in xrange(0,lons.shape[0],lstl):
						for j in xrange(0,lons.shape[1],lstl):
							ax1.quiver(lons1[i][j],lats1[i][j],vx1[i][j],vy1[i][j],width=0.001,linewidth=0.1,scale=1/0.015,color= co)
				canvas.show()
				if vHumidity.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()
						

						
def map1():
				p = f.gca()
				#root = Tk.Tk()
				#fig = Figure()  ## here
				#ax1.set_visible(True)
				ax1 = f.add_subplot(111)  ## 
				"""m = Basemap(width=9000000,height=7000000,projection='lcc', 
			resolution='c',lat_1=45.,lat_2=55,lat_0=50,lon_0=-97.,
			ax=ax1) ## here
				
				m = Basemap(llcrnrlon=-145.5,llcrnrlat=1.,urcrnrlon=-2.566,urcrnrlat=46.352,\
								rsphere=(6378137.00,6356752.3142),\
								resolution='l',area_thresh=1000.,projection='lcc',\
								lat_1=50.,lon_0=-97,ax=ax1)"""
				m.drawcoastlines()
				m.drawcountries()
				m.drawstates()
				ny = lons.shape[0]; nx = lons.shape[1]
				lons1, lats1 = m(lons, lats)
				#m.drawmapboundary(fill_color='aqua')
				#m.fillcontinents(color='coral',lake_color='aqua')
				#canvas = FigureCanvasTkAgg(f, master=root)  ## here
				canvas.show()
				if map2.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()
def ensrand(enrand):
				#enrand=random.choice(ensembles)
				l=[]
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l.append("C:/Users/Najmeh/Documents/dissertation/1999030418/")
				l=[s + enrand for s in l]
				l[0]=l[0]+"/wrfprs_1999-03-01_18_00_00.nc"
				l[1]=l[1]+"/wrfprs_1999-03-01_19_00_00.nc"
				l[2]=l[2]+"/wrfprs_1999-03-01_20_00_00.nc"
				l[3]=l[3]+"/wrfprs_1999-03-01_21_00_00.nc"
				l[4]=l[4]+"/wrfprs_1999-03-01_22_00_00.nc"
				l[5]=l[5]+"/wrfprs_1999-03-01_23_00_00.nc"
				l[6]=l[6]+"/wrfprs_1999-03-02_00_00_00.nc"
				l[7]=l[7]+"/wrfprs_1999-03-02_01_00_00.nc"
				l[8]=l[8]+"/wrfprs_1999-03-02_02_00_00.nc"
				l[9]=l[9]+"/wrfprs_1999-03-02_03_00_00.nc"
				l[10]=l[10]+"/wrfprs_1999-03-02_04_00_00.nc"
				l[11]=l[11]+"/wrfprs_1999-03-02_05_00_00.nc"
				l[12]=l[12]+"/wrfprs_1999-03-02_06_00_00.nc"
				l[13]=l[13]+"/wrfprs_1999-03-02_07_00_00.nc"
				l[14]=l[14]+"/wrfprs_1999-03-02_08_00_00.nc"
				l[15]=l[15]+"/wrfprs_1999-03-02_09_00_00.nc"
				l[16]=l[16]+"/wrfprs_1999-03-02_10_00_00.nc"
				l[17]=l[17]+"/wrfprs_1999-03-02_11_00_00.nc"
				l[18]=l[18]+"/wrfprs_1999-03-02_12_00_00.nc"
				l[19]=l[19]+"/wrfprs_1999-03-02_13_00_00.nc"
				l[20]=l[20]+"/wrfprs_1999-03-02_14_00_00.nc"
				l[21]=l[21]+"/wrfprs_1999-03-02_15_00_00.nc"
				l[22]=l[22]+"/wrfprs_1999-03-02_16_00_00.nc"
				l[23]=l[23]+"/wrfprs_1999-03-02_17_00_00.nc"
				l[24]=l[24]+"/wrfprs_1999-03-02_18_00_00.nc"
				l[25]=l[25]+"/wrfprs_1999-03-02_19_00_00.nc"
				l[26]=l[26]+"/wrfprs_1999-03-02_20_00_00.nc"
				l[27]=l[27]+"/wrfprs_1999-03-02_21_00_00.nc"
				l[28]=l[28]+"/wrfprs_1999-03-02_22_00_00.nc"
				l[29]=l[29]+"/wrfprs_1999-03-02_23_00_00.nc"
				l[30]=l[30]+"/wrfprs_1999-03-03_00_00_00.nc"
				l[31]=l[31]+"/wrfprs_1999-03-03_01_00_00.nc"
				l[32]=l[32]+"/wrfprs_1999-03-03_02_00_00.nc"
				l[33]=l[33]+"/wrfprs_1999-03-03_03_00_00.nc"
				l[34]=l[34]+"/wrfprs_1999-03-03_04_00_00.nc"
				l[35]=l[35]+"/wrfprs_1999-03-03_05_00_00.nc"
				l[36]=l[36]+"/wrfprs_1999-03-03_06_00_00.nc"
				l[37]=l[37]+"/wrfprs_1999-03-03_07_00_00.nc"
				l[38]=l[38]+"/wrfprs_1999-03-03_08_00_00.nc"
				l[39]=l[39]+"/wrfprs_1999-03-03_09_00_00.nc"
				l[40]=l[40]+"/wrfprs_1999-03-03_10_00_00.nc"
				l[41]=l[41]+"/wrfprs_1999-03-03_11_00_00.nc"
				l[42]=l[42]+"/wrfprs_1999-03-03_12_00_00.nc"
				l[43]=l[43]+"/wrfprs_1999-03-03_13_00_00.nc"
				l[44]=l[44]+"/wrfprs_1999-03-03_14_00_00.nc"
				l[45]=l[45]+"/wrfprs_1999-03-03_15_00_00.nc"
				l[46]=l[46]+"/wrfprs_1999-03-03_16_00_00.nc"
				l[47]=l[47]+"/wrfprs_1999-03-03_17_00_00.nc"
				l[48]=l[48]+"/wrfprs_1999-03-03_18_00_00.nc"
				l[49]=l[49]+"/wrfprs_1999-03-03_19_00_00.nc"
				l[50]=l[50]+"/wrfprs_1999-03-03_20_00_00.nc"
				l[51]=l[51]+"/wrfprs_1999-03-03_21_00_00.nc"
				l[52]=l[52]+"/wrfprs_1999-03-03_22_00_00.nc"
				l[53]=l[53]+"/wrfprs_1999-03-03_23_00_00.nc"
				l[54]=l[54]+"/wrfprs_1999-03-04_00_00_00.nc"
				l[55]=l[55]+"/wrfprs_1999-03-04_01_00_00.nc"
				l[56]=l[56]+"/wrfprs_1999-03-04_02_00_00.nc"
				l[57]=l[57]+"/wrfprs_1999-03-04_03_00_00.nc"
				l[58]=l[58]+"/wrfprs_1999-03-04_04_00_00.nc"
				l[59]=l[59]+"/wrfprs_1999-03-04_05_00_00.nc"
				l[60]=l[60]+"/wrfprs_1999-03-04_06_00_00.nc"
				l[61]=l[61]+"/wrfprs_1999-03-04_07_00_00.nc"
				l[62]=l[62]+"/wrfprs_1999-03-04_08_00_00.nc"
				l[63]=l[63]+"/wrfprs_1999-03-04_09_00_00.nc"
				l[64]=l[64]+"/wrfprs_1999-03-04_10_00_00.nc"
				l[65]=l[65]+"/wrfprs_1999-03-04_11_00_00.nc"
				l[66]=l[66]+"/wrfprs_1999-03-04_12_00_00.nc"
				l[67]=l[67]+"/wrfprs_1999-03-04_13_00_00.nc"
				l[68]=l[68]+"/wrfprs_1999-03-04_14_00_00.nc"
				l[69]=l[69]+"/wrfprs_1999-03-04_15_00_00.nc"
				l[70]=l[70]+"/wrfprs_1999-03-04_16_00_00.nc"
				l[71]=l[71]+"/wrfprs_1999-03-04_17_00_00.nc"
				l[72]=l[72]+"/wrfprs_1999-03-04_18_00_00.nc"
				return l 


def clusteringaxes():
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				#timestep=randint(0,71)
				#print timestep
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				minhu=humid3.min();maxhu=humid3.max();humid3=(humid3-minhu)/(maxhu-minhu)
				minhe=height3.min();maxhe=height3.max();height3=(height3-minhe)/(maxhe-minhe)
				minwu=windu3.min();maxwu=windu3.max();windu3=(windu3-minwu)/(maxwu-minwu)
				minwv=windv3.min();maxwv=windv3.max();windv3=(windv3-minwv)/(maxwv-minwv)

				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3=height3.ravel()
				humid3=humid3.ravel()
				windu3=windu3.ravel()
				windv3=windv3.ravel()

				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				height3 = height3.reshape(len(height3), 1)
				humid3 = humid3.reshape(len(humid3), 1)
				windu3 = windu3.reshape(len(windu3), 1)
				windv3 = windv3.reshape(len(windv3), 1)

								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)

						temp=temp.ravel()
						pres=pres.ravel()
						height=height.ravel()
						humid=humid.ravel()
						windu=windu.ravel()
						windv=windv.ravel()
						
						temp3 = np.insert(temp3, 0, temp, axis=1)
						pres3 = np.insert(pres3, 0, pres, axis=1)#hstack((temp3,pres3))
						humid3 = np.insert(humid3, 0, humid, axis=1)#ensdata = np.hstack((ensdata,humid3))
						height3 = np.insert(height3, 0, height, axis=1)#ensdata = np.hstack((ensdata,height3))
						windu3 = np.insert(windu3, 0, windu, axis=1)#ensdata = np.hstack((ensdata,windu3))
						windv3 = np.insert(windv3, 0, windv, axis=1)#ensdata = np.hstack((ensdata,windv3))

				ensdata=temp3
				#print ensdata.shape
				#ensdata=[]
				#np.insert(ensdata,1,temp3,axis=0)
				ensdata=np.insert(ensdata,20253,pres3,axis=0)
				ensdata=np.insert(ensdata,40506,height3,axis=0)
				ensdata=np.insert(ensdata,60759,humid3,axis=0)
				ensdata=np.insert(ensdata,81012,windu3,axis=0)
				ensdata=np.insert(ensdata,101265,windv3,axis=0)
				batch_size=100  
				#print ensdata.shape  #3645540
				mbk = MiniBatchKMeans(init='k-means++', n_clusters=5, batch_size=batch_size,
									  n_init=10, max_no_improvement=10, verbose=0)
				temp1 = ensdata#np.resize(ensdata,(3645540,1))
				mbk.fit(temp1)
				mbk_means_labels = mbk.labels_ # 3645540 number between 0 and 4 
				mbk_means_cluster_centers = mbk.cluster_centers_ # 5 numbers between 0 and 1 
				mbk_means_labels_unique = np.unique(mbk_means_labels)# [0 1 2 3 4]
				#print mbk_means_labels.shape
				#print ensdata.shape
				temp4=mbk_means_labels[0:20253]
				pres4=mbk_means_labels[20253:40506]
				height4=mbk_means_labels[40506:60759]
				humid4=mbk_means_labels[60759:81012]
				windu4=mbk_means_labels[81012:101265]
				windv4=mbk_means_labels[101265:121518]
				#print '1'
				allen=20253
				allv=[]
				tim = allen/30
				allv=[0 for su1 in xrange(allen)]
				alltime=[0 for su1 in xrange(tim)]
				alltime1=[0 for su1 in xrange(tim)]
				ax1 = f.add_subplot(2,3,1)
				ax2 = f.add_subplot(2,3,2)
				ax3 = f.add_subplot(2,3,3)
				ax4 = f.add_subplot(2,3,4)
				ax5 = f.add_subplot(2,3,5)
				ax6 = f.add_subplot(2,3,6)
				temp4=np.reshape(temp4,(129,157))
				pres4=np.reshape(pres4,(129,157))
				height4=np.reshape(height4,(129,157))
				humid4=np.reshape(humid4,(129,157))
				windu4=np.reshape(windu4,(129,157))
				windv4=np.reshape(windv4,(129,157))
				
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				ax1.pcolor(lons1,lats1,temp4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax2.pcolor(lons1,lats1,pres4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax3.pcolor(lons1,lats1,height4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax4.pcolor(lons1,lats1,humid4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax5.pcolor(lons1,lats1,windu4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax6.pcolor(lons1,lats1,windv4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax1.set_title("Temperature")
				ax2.set_title("Pressure")
				ax3.set_title("Height")
				ax4.set_title("Humidity")
				ax5.set_title("Windu")
				ax6.set_title("Windv")
				ax1.set_visible(True)
				ax2.set_visible(True)
				ax3.set_visible(True)
				ax4.set_visible(True)
				ax5.set_visible(True)
				ax6.set_visible(True)

				canvas.show()
				if clustera.get()== 0:
						ax1.cla()
						ax1.set_visible(False)
						ax2.cla()
						ax3.cla()
						ax4.cla()
						ax5.cla()
						ax6.cla()
						plt.cla()
						ax2.set_visible(False)
						ax3.set_visible(False)
						ax4.set_visible(False)
						ax5.set_visible(False)
						ax6.set_visible(False)
						#cb.outline.set_visible(False)
						#cb.set_ticks([])
						#cb.outline.set_visible(False)
						#ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1 = f.add_subplot(111)
						canvas.show()


def clusteringallcol():
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				#timestep=randint(0,71)
				#print timestep
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				minhu=humid3.min();maxhu=humid3.max();humid3=(humid3-minhu)/(maxhu-minhu)
				minhe=height3.min();maxhe=height3.max();height3=(height3-minhe)/(maxhe-minhe)
				minwu=windu3.min();maxwu=windu3.max();windu3=(windu3-minwu)/(maxwu-minwu)
				minwv=windv3.min();maxwv=windv3.max();windv3=(windv3-minwv)/(maxwv-minwv)

				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3=height3.ravel()
				humid3=humid3.ravel()
				windu3=windu3.ravel()
				windv3=windv3.ravel()

##				temp3 = temp3.reshape(len(temp3), 1)
##				pres3 = pres3.reshape(len(pres3), 1)
##				height3 = height3.reshape(len(height3), 1)
##				humid3 = humid3.reshape(len(humid3), 1)
##				windu3 = windu3.reshape(len(windu3), 1)
##				windv3 = windv3.reshape(len(windv3), 1)

								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)

						temp=temp.ravel()
						pres=pres.ravel()
						height=height.ravel()
						humid=humid.ravel()
						windu=windu.ravel()
						windv=windv.ravel()
						#print temp.shape
						#print temp3.shape
						temp3 = np.insert(temp3, 0, temp, axis=0)
						pres3 = np.insert(pres3, 0, pres, axis=0)#hstack((temp3,pres3))
						humid3 = np.insert(humid3, 0, humid, axis=0)#ensdata = np.hstack((ensdata,humid3))
						height3 = np.insert(height3, 0, height, axis=0)#ensdata = np.hstack((ensdata,height3))
						windu3 = np.insert(windu3, 0, windu, axis=0)#ensdata = np.hstack((ensdata,windu3))
						windv3 = np.insert(windv3, 0, windv, axis=0)#ensdata = np.hstack((ensdata,windv3))
##
##				plt.subplot(231)
##				plt.title("Temperature")
##				plt.subplot(232)
##				plt.title("Pressure")
##				plt.subplot(233)
##				plt.title("Humidity")
##				plt.subplot(234)
##				plt.title("Height")
##				plt.subplot(235)
##				plt.title("Windu")
##				plt.subplot(236)
##				plt.title("Windv")
				ax1 = f.add_subplot(2,3,1)
				ax2 = f.add_subplot(2,3,2)
				ax3 = f.add_subplot(2,3,3)
				ax4 = f.add_subplot(2,3,4)
				ax5 = f.add_subplot(2,3,5)
				ax6 = f.add_subplot(2,3,6)
				ax1.set_title("Temperature")
				ax2.set_title("Pressure")
				ax3.set_title("Height")
				ax4.set_title("Humidity")
				ax5.set_title("Windu")
				ax6.set_title("Windv")
				ax1.set_visible(True)
				ax2.set_visible(True)
				ax3.set_visible(True)
				ax4.set_visible(True)
				ax5.set_visible(True)
				ax6.set_visible(True)
				

				allen=20253
				allv=temp3
				#print temp3.shape#(607590,)
				#print allv
				tim = allen/30
				#allv=[0 for su1 in xrange(allen)]
				alltime=[0 for su1 in xrange(allen)]
				alltime1=[0 for su1 in xrange(allen)]
				alltime2=[0 for su1 in xrange(allen)]
				alltime3=[0 for su1 in xrange(allen)]
				alltime4=[0 for su1 in xrange(allen)]
				alltime5=[0 for su1 in xrange(allen)]
				alltime6=[0 for su1 in xrange(allen)]


##				for i in xrange(allen):
##						allv[i]=temp4[i]+humid4[i]+height4[i]+windu4[i]+windv4[i]
##
##				#print '2'       
				for i in xrange(30):
						j=i*allen
						#print i
						for k in xrange(allen):
							if alltime1[k]==7777:
								   pass
							else:
								   tempor = temp3[k]
								   alltime1[k]= temp3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.05 < alltime1[k] < tempor+0.05:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime1[k]= 7777

							if alltime2[k]==7777:
								   pass
							else:
								   tempor = pres3[k]
								   alltime2[k]= pres3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.09 < alltime2[k] < tempor+0.09:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime2[k]= 7777

							if alltime3[k]==7777:
								   pass
							else:
								   tempor = humid3[k]
								   alltime3[k]= humid3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.3 < alltime3[k] < tempor+0.3:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime3[k]= 7777
									   
							if alltime4[k]==7777:
								   pass
							else:
								   tempor = height3[k]
								   alltime4[k]= height3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.09 < alltime4[k] < tempor+0.09:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime4[k]= 7777

							if alltime5[k]==7777:
								   pass
							else:
								   tempor = windu3[k]
								   alltime5[k]= windu3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.2 < alltime5[k] < tempor+0.2:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime5[k]= 7777

							if alltime6[k]==7777:
								   pass
							else:
								   tempor = windv3[k]
								   alltime6[k]= windv3[k+j]
								   #print (alltime1[k],tempor)
								   if tempor-0.2 < alltime6[k] < tempor+0.2:
									   #print (alltime1[k],tempor)
									   pass
								   else:
									   alltime6[k]= 7777 


									   

				temp2=np.reshape(temp3[0:20253],(129,157))
				alltime1=np.reshape(alltime1[0:20253],(129,157))
				pres2=np.reshape(pres3[0:20253],(129,157))
				alltime2=np.reshape(alltime2[0:20253],(129,157))
				humid2=np.reshape(humid3[0:20253],(129,157))
				alltime3=np.reshape(alltime3[0:20253],(129,157))
				height2=np.reshape(height3[0:20253],(129,157))
				alltime4=np.reshape(alltime4[0:20253],(129,157))
				windu2=np.reshape(windu3[0:20253],(129,157))
				alltime5=np.reshape(alltime5[0:20253],(129,157))
				windv2=np.reshape(windv3[0:20253],(129,157))
				alltime6=np.reshape(alltime6[0:20253],(129,157))
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				ax1.pcolor(lons1,lats1,temp2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax2.pcolor(lons1,lats1,pres2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax3.pcolor(lons1,lats1,humid2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax4.pcolor(lons1,lats1,height2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax5.pcolor(lons1,lats1,windu2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				ax6.pcolor(lons1,lats1,windv2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				
				for i in xrange(129):
					for j in xrange(157):
						if alltime1[i][j]==7777:
							ax1.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')
						if alltime2[i][j]==7777:
							ax2.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')
						if alltime3[i][j]==7777:
							ax3.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')
						if alltime4[i][j]==7777:
							ax4.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')
						if alltime5[i][j]==7777:
							ax5.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')
						if alltime6[i][j]==7777:
							ax6.scatter(lons1[i][j],lats1[i][j],facecolor='red',s=4,linewidth='0.01', edgecolor='black')

				canvas.show()
				if clusterac.get()== 0:
						ax1.set_visible(False)
						ax2.set_visible(False)
						ax3.set_visible(False)
						ax4.set_visible(False)
						ax5.set_visible(False)
						ax6.set_visible(False)
						plt.cla()
						#cb.outline.set_visible(False)
						#cb.set_ticks([])
						#cb.outline.set_visible(False)
						#ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1 = f.add_subplot(111)
						canvas.show()



def clustering1():
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				#timestep=randint(0,71)
				#print timestep
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				minhu=humid3.min();maxhu=humid3.max();humid3=(humid3-minhu)/(maxhu-minhu)
				minhe=height3.min();maxhe=height3.max();height3=(height3-minhe)/(maxhe-minhe)
				minwu=windu3.min();maxwu=windu3.max();windu3=(windu3-minwu)/(maxwu-minwu)
				minwv=windv3.min();maxwv=windv3.max();windv3=(windv3-minwv)/(maxwv-minwv)

				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3=height3.ravel()
				humid3=humid3.ravel()
				windu3=windu3.ravel()
				windv3=windv3.ravel()

				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				height3 = height3.reshape(len(height3), 1)
				humid3 = humid3.reshape(len(humid3), 1)
				windu3 = windu3.reshape(len(windu3), 1)
				windv3 = windv3.reshape(len(windv3), 1)

								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)

						temp=temp.ravel()
						pres=pres.ravel()
						height=height.ravel()
						humid=humid.ravel()
						windu=windu.ravel()
						windv=windv.ravel()
						
						temp3 = np.insert(temp3, 0, temp, axis=1)
						pres3 = np.insert(pres3, 0, pres, axis=1)#hstack((temp3,pres3))
						humid3 = np.insert(humid3, 0, humid, axis=1)#ensdata = np.hstack((ensdata,humid3))
						height3 = np.insert(height3, 0, height, axis=1)#ensdata = np.hstack((ensdata,height3))
						windu3 = np.insert(windu3, 0, windu, axis=1)#ensdata = np.hstack((ensdata,windu3))
						windv3 = np.insert(windv3, 0, windv, axis=1)#ensdata = np.hstack((ensdata,windv3))
##                                print temp3.shape  #20253,30
##                                print temp.shape   #20253,
##				ensdata=np.hstack((temp3,pres3))
##				ensdata=np.hstack((ensdata,height3))
##				ensdata=np.hstack((ensdata,humid3))
##				ensdata=np.hstack((ensdata,windu3))
##				ensdata=np.hstack((ensdata,windv3))
				ensdata=temp3
				ensdata=np.insert(ensdata,2,pres3,axis=0)
				ensdata=np.insert(ensdata,3,height3,axis=0)
				ensdata=np.insert(ensdata,4,humid3,axis=0)
				ensdata=np.insert(ensdata,5,windu3,axis=0)
				ensdata=np.insert(ensdata,6,windv3,axis=0)
				#print ensdata.shape
##				ensdata=temp3
##				ensdata=np.append(ensdata,pres3)
##				ensdata=np.append(ensdata,height3)
##				print ensdata.shape
##				ensdata=np.append(ensdata,humid3)
##				ensdata=np.append(ensdata,windu3)
##				ensdata=np.append(ensdata,windv3)

##				print ensdata.shape#(20253, 180)

				batch_size=100  
				#print ensdata.shape  #3645540
				mbk = MiniBatchKMeans(init='k-means++', n_clusters=5, batch_size=batch_size,
									  n_init=10, max_no_improvement=10, verbose=0)
				temp1 = ensdata#np.resize(ensdata,(3645540,1))
				mbk.fit(temp1)
				mbk_means_labels = mbk.labels_ # 3645540 number between 0 and 4 
				mbk_means_cluster_centers = mbk.cluster_centers_ # 5 numbers between 0 and 1 
				mbk_means_labels_unique = np.unique(mbk_means_labels)# [0 1 2 3 4]
				#print mbk_means_labels.shape
				#print ensdata.shape
				temp4=mbk_means_labels[0:20253]
				pres4=mbk_means_labels[20253:40506]
				humid4=mbk_means_labels[40506:60759]
				height4=mbk_means_labels[60759:81012]
				windu4=mbk_means_labels[81012:101265]
				windv4=mbk_means_labels[101265:121518]
				#print '1'
				allen=20253
				allv=[]
				tim = allen/30
				allv=[0 for su1 in xrange(allen)]
				alltime=[0 for su1 in xrange(tim)]
				alltime1=[0 for su1 in xrange(tim)]
##				ax1 = f.add_subplot(2,3,1)
##				ax2 = f.add_subplot(2,3,2)
##				ax3 = f.add_subplot(2,3,3)
##				ax4 = f.add_subplot(2,3,4)
##				ax5 = f.add_subplot(2,3,5)
##				ax6 = f.add_subplot(2,3,6)
##				temp4=np.reshape(temp4,(129,157))
##				pres4=np.reshape(pres4,(129,157))
##				humid4=np.reshape(humid4,(129,157))
##				height4=np.reshape(height4,(129,157))
##				windu4=np.reshape(windu4,(129,157))
##				windv4=np.reshape(windv4,(129,157))
				
##				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
##				ax1.pcolor(lons1,lats1,temp4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
##				ax2.pcolor(lons1,lats1,pres4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
##				ax3.pcolor(lons1,lats1,humid4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
##				ax4.pcolor(lons1,lats1,height4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
##				ax5.pcolor(lons1,lats1,windu4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
##                                ax6.pcolor(lons1,lats1,windv4, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)

				for i in xrange(allen):
						allv[i]=temp4[i]+humid4[i]+height4[i]+windu4[i]+windv4[i]
##
##				#print '2'       
##				for i in xrange(30):
##						j=i*tim
##						for k in xrange(tim):
##							   alltime1[k]= allv[k+j]
##							   alltime[k]= alltime[k] + alltime1[k]
##				
				temp2=np.reshape(allv,(129,157))
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				im=ax1.pcolor(lons1,lats1,temp2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				cbar = f.colorbar(mappable=im, cax=ax1)
				cbar.ax.set_ylabel('Cluster Density', rotation=270)
				#cb=f.colorbar(dd)
				canvas.show()
				if cluster1.get()== 0:
						plt.cla()
						#cb.outline.set_visible(False)
						#cb.set_ticks([])
						#cb.outline.set_visible(False)
						#ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1 = f.add_subplot(111)
						canvas.show()


def clustering2():

				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				#timestep=randint(0,71)
				#print timestep
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				minhu=humid3.min();maxhu=humid3.max();humid3=(humid3-minhu)/(maxhu-minhu)
				minhe=height3.min();maxhe=height3.max();height3=(height3-minhe)/(maxhe-minhe)
				minwu=windu3.min();maxwu=windu3.max();windu3=(windu3-minwu)/(maxwu-minwu)
				minwv=windv3.min();maxwv=windv3.max();windv3=(windv3-minwv)/(maxwv-minwv)

				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3=height3.ravel()
				humid3=humid3.ravel()
				windu3=windu3.ravel()
				windv3=windv3.ravel()

				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				height3 = height3.reshape(len(height3), 1)
				humid3 = humid3.reshape(len(humid3), 1)
				windu3 = windu3.reshape(len(windu3), 1)
				windv3 = windv3.reshape(len(windv3), 1)

								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)

						temp=temp.ravel()
						pres=pres.ravel()
						height=height.ravel()
						humid=humid.ravel()
						windu=windu.ravel()
						windv=windv.ravel()
						
						temp3 = np.insert(temp3, 0, temp, axis=1)
						pres3 = np.insert(pres3, 0, pres, axis=1)#hstack((temp3,pres3))
						humid3 = np.insert(humid3, 0, humid, axis=1)#ensdata = np.hstack((ensdata,humid3))
						height3 = np.insert(height3, 0, height, axis=1)#ensdata = np.hstack((ensdata,height3))
						windu3 = np.insert(windu3, 0, windu, axis=1)#ensdata = np.hstack((ensdata,windu3))
						windv3 = np.insert(windv3, 0, windv, axis=1)#ensdata = np.hstack((ensdata,windv3))
##                                print temp3.shape  #20253,30
##                                print temp.shape   #20253,
##				ensdata=np.hstack((temp3,pres3))
##				ensdata=np.hstack((ensdata,height3))
##				ensdata=np.hstack((ensdata,humid3))
##				ensdata=np.hstack((ensdata,windu3))
##				ensdata=np.hstack((ensdata,windv3))
				ensdata=temp3
				#print ensdata.shape
				#ensdata=[]
				#np.insert(ensdata,1,temp3,axis=0)
				ensdata=np.insert(ensdata,20253,pres3,axis=0)
				ensdata=np.insert(ensdata,40506,height3,axis=0)
				ensdata=np.insert(ensdata,60759,humid3,axis=0)
				ensdata=np.insert(ensdata,81012,windu3,axis=0)
				ensdata=np.insert(ensdata,101265,windv3,axis=0)
				#print ensdata.shape
##				ensdata=temp3
##				ensdata=np.append(ensdata,pres3)
##				ensdata=np.append(ensdata,height3)
##				print ensdata.shape
##				ensdata=np.append(ensdata,humid3)
##				ensdata=np.append(ensdata,windu3)
##				ensdata=np.append(ensdata,windv3)

##				print ensdata.shape#(20253, 180)

				batch_size=100  
				#print ensdata.shape  #3645540
				mbk = MiniBatchKMeans(init='k-means++', n_clusters=5, batch_size=batch_size,
									  n_init=10, max_no_improvement=10, verbose=0)
				temp1 = ensdata#np.resize(ensdata,(3645540,1))
				mbk.fit(temp1)
				mbk_means_labels = mbk.labels_ # 3645540 number between 0 and 4 
				mbk_means_cluster_centers = mbk.cluster_centers_ # 5 numbers between 0 and 1 
				mbk_means_labels_unique = np.unique(mbk_means_labels)# [0 1 2 3 4]
				#print mbk_means_labels.shape
				#print ensdata.shape
				sixall=[0 for su1 in xrange(6)]
				cluster=[0 for su1 in xrange(20253)]
				temp4=mbk_means_labels[0:20253]
				pres4=mbk_means_labels[20253:40506]
				height4=mbk_means_labels[40506:60759]
				humid4=mbk_means_labels[60759:81012]
				windu4=mbk_means_labels[81012:101265]
				windv4=mbk_means_labels[101265:121518]
				for i in xrange(20253):
					sixall[0]=temp4[i]
					sixall[1]=pres4[i]
					sixall[2]=height4[i]
					sixall[3]=humid4[i]
					sixall[4]=windu4[i]
					sixall[5]=windv4[i]
					sixall2=sixall
					unique_words = set(sixall2)             # == set(['a', 'b', 'c'])
					unique_word_count = len(unique_words)
					cluster[i]=unique_word_count#np.count_nonzero(sixall2==sixall)

##                                        
##				#print '1'
##				allen=20253
##				allv=[]
##				tim = allen/30
##				allv=[0 for su1 in xrange(allen)]
##				alltime=[0 for su1 in xrange(tim)]
##				alltime1=[0 for su1 in xrange(tim)]
##
##
##				#print '1'
##				allen=607590
##				allv=[]
##				tim = allen/30
##				allv=[0 for su1 in xrange(allen)]
##				alltime=[0 for su1 in xrange(tim)]
##				alltimetemp=[0 for su1 in xrange(tim)]
##				alltimepres=[0 for su1 in xrange(tim)]
##				alltimehumid=[0 for su1 in xrange(tim)]
##				alltimeheight=[0 for su1 in xrange(tim)]
##				alltimewindu=[0 for su1 in xrange(tim)]
##				alltimewindv=[0 for su1 in xrange(tim)]
##
##				"""
##				for i in xrange(allen):
##						allv[i]=temp4[i]+humid4[i]+height4[i]+windu4[i]+windv4[i]
##				"""
##				#print '2'       
##				for i in xrange(30):
##						j=i*tim
##						for k in xrange(tim):
##							   alltimetemp[k]= temp4[k+j]+alltimetemp[k]
##							   alltimepres[k]= pres4[k+j]+alltimepres[k]
##							   alltimehumid[k]= humid4[k+j]+alltimehumid[k]
##							   alltimeheight[k]= height4[k+j]+alltimeheight[k]
##							   alltimewindu[k]= windu4[k+j]+alltimewindu[k]
##							   alltimewindv[k]= windv4[k+j]+alltimewindv[k]
##
##				te=0; pr=0; hu=0; he=0; wu=0; wv=0
##				cluster=[0 for su1 in xrange(tim)]
##				sixall=[0 for su1 in xrange(6)]
##
##				for i in xrange(tim):
##					te=0
##					sixall[0]=alltimetemp[i]
##					sixall[1]=alltimepres[i]
##					sixall[2]=alltimehumid[i]
##					sixall[3]=alltimeheight[i]
##					sixall[4]=alltimewindu[i]
##					sixall[5]=alltimewindv[i]
##					sixall2=sixall
##					unique_words = set(sixall2)             # == set(['a', 'b', 'c'])
##					unique_word_count = len(unique_words)
##					"""
##					for j in xrange(5):
##						if sixall[j]!=sixall2[j]:
##							te=te+1
##					print te
##					"""
##					cluster[i]=unique_word_count#np.count_nonzero(sixall2==sixall)
##			  
				temp2=np.reshape(cluster,(129,157))
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				im=ax1.pcolor(lons1,lats1,temp2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				cbar = f.colorbar(mappable=im, cax=ax1)
				cbar.ax.set_ylabel('Number of Clusters', rotation=270)
				canvas.show()
				if clustern2.get()== 0:
						ax1.cla()
						#cb.cla()
						#cb.outline.set_visible(False)
						#cb.set_ticks([])
						#ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1=f.add_subplot(111)
						canvas.show()

def clusterensembles():

				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				#timestep=randint(0,71)
				#print timestep
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				minhu=humid3.min();maxhu=humid3.max();humid3=(humid3-minhu)/(maxhu-minhu)
				minhe=height3.min();maxhe=height3.max();height3=(height3-minhe)/(maxhe-minhe)
				minwu=windu3.min();maxwu=windu3.max();windu3=(windu3-minwu)/(maxwu-minwu)
				minwv=windv3.min();maxwv=windv3.max();windv3=(windv3-minwv)/(maxwv-minwv)

				temp3=temp3.ravel()
				pres3=pres3.ravel()
				height3=height3.ravel()
				humid3=humid3.ravel()
				windu3=windu3.ravel()
				windv3=windv3.ravel()

				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				height3 = height3.reshape(len(height3), 1)
				humid3 = humid3.reshape(len(humid3), 1)
				windu3 = windu3.reshape(len(windu3), 1)
				windv3 = windv3.reshape(len(windv3), 1)

								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)

						temp=temp.ravel()
						pres=pres.ravel()
						height=height.ravel()
						humid=humid.ravel()
						windu=windu.ravel()
						windv=windv.ravel()
						
						temp3 = np.insert(temp3, 0, temp, axis=1)
						pres3 = np.insert(pres3, 0, pres, axis=1)#hstack((temp3,pres3))
						humid3 = np.insert(humid3, 0, humid, axis=1)#ensdata = np.hstack((ensdata,humid3))
						height3 = np.insert(height3, 0, height, axis=1)#ensdata = np.hstack((ensdata,height3))
						windu3 = np.insert(windu3, 0, windu, axis=1)#ensdata = np.hstack((ensdata,windu3))
						windv3 = np.insert(windv3, 0, windv, axis=1)#ensdata = np.hstack((ensdata,windv3))
		
				temp3=np.insert(temp3, 0, pres3, axis=1)#np.hstack((temp3,pres3))
				temp3=np.insert(temp3, 0, height3, axis=1)#np.hstack((temp3,height3))
				temp3=np.insert(temp3, 0, humid3, axis=1)#np.hstack((temp3,humid3))
				temp3=np.insert(temp3, 0, windu3, axis=1)#np.hstack((temp3,windu3))
				temp3=np.insert(temp3, 0, windv3, axis=1)#np.hstack((temp3,windv3))
				print temp3.shape
				#mbk = AgglomerativeClustering(n_clusters=5, compute_full_tree=True, affinity='euclidean', linkage='complete')#AgglomerativeClustering(linkage='complete', n_clusters=10)
				#t0 = time()
				#mbk.fit(X_red)
				batch_size=100    
				mbk = MiniBatchKMeans(init='k-means++', n_clusters=5, batch_size=batch_size, n_init=10, max_no_improvement=10, verbose=0)
				#temp3=np.transpose(temp3)
				#print temp3.shape
				mbk.fit(temp3)
				mbk_means_labels = mbk.labels_
				#print mbk_means_labels.shape
				temp2=np.reshape(mbk_means_labels,(129,157))
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				im=ax1.pcolor(lons1,lats1,temp2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				#cbar = f.colorbar(mappable=im, cax=ax1)
				cbar = f.colorbar(mappable=im, cax=ax1)#, orientation = 'horizontal')
				#cbar = f.colorbar(mappable=im, cax=ax1)
				cbar.ax.set_ylabel('Cluster Number', rotation=270)
				canvas.show()
				if clusterens2.get()== 0:
						ax1.clear()
						#cbar=cbar.on_mappable_changed(im)
						cbar.ax.clear()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1=f.add_subplot(111)
						canvas.show()


def clustertemp():

				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']

				b, level, varn = tileva()
				b= int(b); level= int(level)
				timestep=b
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				if varn== 'PRMSL_GDS3_MSL':
					temp = dset.variables[varn][:]
					temp3=np.array(temp[:,:])
				elif varn== 'UV_GRD_GDS3_ISBL':
					windu = dset.variables['U_GRD_GDS3_ISBL'][:]
					windv = dset.variables['V_GRD_GDS3_ISBL'][:]
					windu=np.array(windu[level,:,:])
					windv=np.array(windv[level,:,:])
					temp3=(windu**2+windv**2)**0.5
				else:
					temp = dset.variables[varn][:]
					temp3=np.array(temp[level,:,:])
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)

				temp3=temp3.ravel()

				temp3 = temp3.reshape(len(temp3), 1)

				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						if varn== 'PRMSL_GDS3_MSL':
							temp = dset.variables[varn][:]
							temp=np.array(temp[:,:])
						elif varn== 'UV_GRD_GDS3_ISBL':
							windu = dset.variables['U_GRD_GDS3_ISBL'][:]
							windv = dset.variables['V_GRD_GDS3_ISBL'][:]
							windu=np.array(windu[level,:,:])
							windv=np.array(windv[level,:,:])
							temp=(windu**2+windv**2)**0.5
						else:
							temp = dset.variables[varn][:]
							temp=np.array(temp[level,:,:])
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						temp=temp.ravel()						
						temp3 = np.insert(temp3, 0, temp, axis=1)

				batch_size=100    
				mbk = MiniBatchKMeans(init='k-means++', n_clusters=5, batch_size=batch_size, n_init=10, max_no_improvement=10, verbose=0)    
				mbk.fit(temp3)
				mbk_means_labels = mbk.labels_
				temp2=np.reshape(mbk_means_labels,(129,157))
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				im=ax1.pcolor(lons1,lats1,temp2, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				#cbar = f.colorbar(mappable=im, cax=ax1)
				cbar = plt.colorbar(mappable=im, cax=ax1)#, orientation = 'horizontal')
				cbar.ax.set_ylabel('Cluster Number', rotation=270)
				canvas.show()
				if clustertemp2.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1=f.add_subplot(111)
						canvas.show()

def regression1():
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']
			   
				timestep=b#randint(0,71)
				#print timestep
				#timestep=62     
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				pres221 = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				temp3=np.array(temp[19,:,:])
				pres3=np.array(pres221[:,:])
				height3=np.array(height[19,:,:])
				humid3=np.array(humid[19,:,:])
				windu3=np.array(windu[19,:,:])
				windv3=np.array(windv[19,:,:])
								
				#def ensselect(temp1,pres1,humid1,height1,windu1,windv1):
				for i in xrange(29):
						enrand=ensembles[i]
						url=ensrand(enrand)[timestep]
						dset = Dataset(url)
						lats = dset.variables['g3_lat_0'][:]
						lons = dset.variables['g3_lon_1'][:]
						lons=lons[:,:]
						lats=lats[:,:]
						pres = dset.variables['PRMSL_GDS3_MSL'][:]
						height = dset.variables['HGT_GDS3_ISBL'][:]
						temp = dset.variables['TMP_GDS3_ISBL'][:]
						windu = dset.variables['U_GRD_GDS3_ISBL'][:]
						windv = dset.variables['V_GRD_GDS3_ISBL'][:]
						humid = dset.variables['SPF_H_GDS3_ISBL'][:]
						temp=np.array(temp[19,:,:])
						pres=np.array(pres[:,:])
						height=np.array(height[19,:,:])
						humid=np.array(humid[19,:,:])
						windu=np.array(windu[19,:,:])
						windv=np.array(windv[19,:,:])
						
						mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
						minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
						minhu=humid.min();maxhu=humid.max();humid=(humid-minhu)/(maxhu-minhu)
						minhe=height.min();maxhe=height.max();height=(height-minhe)/(maxhe-minhe)
						minwu=windu.min();maxwu=windu.max();windu=(windu-minwu)/(maxwu-minwu)
						minwv=windv.min();maxwv=windv.max();windv=(windv-minwv)/(maxwv-minwv)
						
						temp3=np.append(temp3,temp,1)
						pres3=np.append(pres3,pres,1)
						height3=np.append(height3,height,1)
						humid3=np.append(humid3,humid,1)
						windu3=np.append(windu3,windu,1)
						windv3=np.append(windv3,windv,1)
						#return temp3,pres3,humid3,height3,windu3,windv3
				#temp3,pres3,humid3,height3,windu3,windv3 = ensselect(temp1,pres1,humid1,height1,windu1,windv1)
				#ensdata2 = np.append(temp3,pres3)
				ensdata2 = temp3       
				ensdata2 = np.append(ensdata2,humid3,1)
				ensdata2 = np.append(ensdata2,height3,1)
				ensdata2 = np.append(ensdata2,windu3,1)
				ensdata2 = np.append(ensdata2,windv3,1)
				from sklearn import datasets, linear_model
				lm = linear_model.LinearRegression()
				#ffff=height
				#gg=np.append(ffff,temp,1)
				#lm.fit(ensdata2, pres3)
				#print lm.intercept_
				#print lm.coef_.shape     (4710,23550)
				#print pres3.shape   (129,4710)
				lm.fit(pres,ensdata2)#(temp,pres)
				#print lm.coef_.shape
				#print lm.intercept_.shape
				hh=lm.predict(pres)
				#print hh.shape
				cmap = matplotlib.colors.ListedColormap(['#7a0177','#c51b8a','#f768a1','#fbb4b9','#feebe2'])
				im=ax1.pcolor(lons1,lats1,hh, cmap=cmap)#cmap=cm, vmin=-6, vmax=6)
				#im=ax1.pcolor(lons1,lats1,hh)#[:,23394:])#windv, hh[:,0:156], temp   23550=157 *30 *5
				canvas.show()
				#print lm.coef_#.shape
				#print lm.intercept_#.shape
				#temp2=np.reshape(lm.coef_,(129,157))
				#ax1.pcolor(lons1,lats1,temp2, cmap='RdBu')#cmap=cm, vmin=-6, vmax=6)
				if regression2.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						#ax1=f.add_subplot(111)
						canvas.show()
				


def pcaf():

				from sklearn.decomposition import PCA
				ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
				'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
				,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
				,'ens_26','ens_27','ens_28','ens_29','ens_30']

				b=42
				timestep=b-1
				enrand=ensembles[29]
				url=ensrand(enrand)[timestep+1]
				dset = Dataset(url)
				lats = dset.variables['g3_lat_0'][:]
				lons = dset.variables['g3_lon_1'][:]
				lons=lons[:,:]
				lats=lats[:,:]
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				pres = dset.variables['PRMSL_GDS3_MSL'][:]
				height = dset.variables['HGT_GDS3_ISBL'][:]
				temp = dset.variables['TMP_GDS3_ISBL'][:]
				humid = dset.variables['SPF_H_GDS3_ISBL'][:]
				humid3=np.array(humid[19,:,:])
				height3=np.array(height[19,:,:])
				temp3=np.array(temp[19,:,:])
				windu=np.array(windu[19,:,:])
				windv=np.array(windv[19,:,:])
				pres3=np.array(pres[:,:])
				windu=np.array(windu[:,:])
				windv=np.array(windv[:,:])
				wind3 = np.sqrt(windv**2 + windu**2)
				mint=height3.min();maxt=height3.max();height3=(height3-mint)/(maxt-mint)
				mint=humid3.min();maxt=humid3.max();humid3=(humid3-mint)/(maxt-mint)
				mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
				mint=wind3.min();maxt=wind3.max();wind3=(wind3-mint)/(maxt-mint)
				minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
				temp3=temp3.ravel()
				pres3=pres3.ravel()
				humid3=humid3.ravel()
				height3=height3.ravel()
				wind3=wind3.ravel()
				
				temp3 = temp3.reshape(len(temp3), 1)
				pres3 = pres3.reshape(len(pres3), 1)
				height3 = height3.reshape(len(height3), 1)
				humid3 = humid3.reshape(len(humid3), 1)
				wind3 = wind3.reshape(len(wind3), 1)
				for i in xrange(6):
					timestep=timestep+1
					for i in xrange(3):
							enrand=ensembles[i]
							url=ensrand(enrand)[timestep]
							dset = Dataset(url)
							windu = dset.variables['U_GRD_GDS3_ISBL'][:]
							windv = dset.variables['V_GRD_GDS3_ISBL'][:]
							pres = dset.variables['PRMSL_GDS3_MSL'][:]
							height = dset.variables['HGT_GDS3_ISBL'][:]
							temp = dset.variables['TMP_GDS3_ISBL'][:]
							humid = dset.variables['SPF_H_GDS3_ISBL'][:]
							humid=np.array(humid[19,:,:])
							height=np.array(height[19,:,:])
							temp=np.array(temp[19,:,:])
							windu=np.array(windu[19,:,:])
							windv=np.array(windv[19,:,:])
							pres=np.array(pres[:,:])
							windu=np.array(windu[:,:])
							windv=np.array(windv[:,:])
							wind = np.sqrt(windv**2 + windu**2)
							mint=height.min();maxt=height.max();height=(height-mint)/(maxt-mint)
							mint=humid.min();maxt=humid.max();humid=(humid-mint)/(maxt-mint)
							mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
							mint=wind.min();maxt=wind.max();wind=(wind-mint)/(maxt-mint)
							minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
							temp=temp.ravel()
							pres=pres.ravel()
							humid=humid.ravel()
							height=height.ravel()
							wind=wind.ravel()
							temp3 = np.insert(temp3, 0, temp, axis=1)
							pres3 = np.insert(pres3, 0, pres, axis=1)
							wind3 = np.insert(wind3, 0, wind, axis=1)
							humid3 = np.insert(humid3, 0, humid, axis=1)
							height3 = np.insert(height3, 0, height, axis=1)

				d33 = [0 for x in range(temp3.shape[0])] 
				leng=175
				for i in xrange(temp3.shape[0]):
					xx=temp3[i,:]
					yy=pres3[i,:]
					zz=wind3[i,:]
					mm=humid3[i,:]
					hh=height3[i,:]
					if (i-1>=0):
						xx=np.append(xx,temp3[i-1,:])
						yy=np.append(yy,pres3[i-1,:])
						zz=np.append(yy,wind3[i-1,:])
						mm=np.append(yy,humid3[i-1,:])
						hh=np.append(yy,height3[i-1,:])
					else:
						pass
					if (i-2>=0):
						xx=np.append(xx,temp3[i-2,:])
						yy=np.append(yy,pres3[i-2,:])
						zz=np.append(yy,wind3[i-2,:])
						mm=np.append(yy,humid3[i-2,:])
						hh=np.append(yy,height3[i-2,:])
					else:
						pass
					if (i+1<temp3.shape[0]):
						xx=np.append(xx,temp3[i+1,:])
						yy=np.append(yy,pres3[i+1,:])
						zz=np.append(yy,wind3[i+1,:])
						mm=np.append(yy,humid3[i+1,:])
						hh=np.append(yy,height3[i+1,:])
					else:
						pass
					if (i+2<temp3.shape[0]):
						xx=np.append(xx,temp3[i+2,:])
						yy=np.append(yy,pres3[i+2,:])
						zz=np.append(xx,wind3[i+2,:])
						mm=np.append(xx,humid3[i+2,:])
						hh=np.append(xx,height3[i+2,:])
					else:
						pass
					if (i-157>=0):
						xx=np.append(xx,temp3[i-157,:])
						yy=np.append(yy,pres3[i-157,:])
						zz=np.append(yy,wind3[i-157,:])
						mm=np.append(yy,humid3[i-157,:])
						hh=np.append(yy,height3[i-157,:])						
					else:
						pass
					if (i-(157*2)>=0):
						xx=np.append(xx,temp3[i-(157*2),:])
						yy=np.append(yy,pres3[i-(157*2),:])
						zz=np.append(yy,wind3[i-(157*2),:])
						mm=np.append(yy,humid3[i-(157*2),:])
						hh=np.append(yy,height3[i-(157*2),:])

						
					if (i+157<temp3.shape[0]):    
						xx=np.append(xx,temp3[i+157,:])
						yy=np.append(yy,pres3[i+157,:])
						zz=np.append(yy,wind3[i+157,:])
						mm=np.append(yy,humid3[i+157,:])
						hh=np.append(yy,height3[i+157,:])						
					else:
						pass
					
					if (i+(157*2)<temp3.shape[0]):
						xx=np.append(xx,temp3[i+(157*2),:])
						yy=np.append(yy,pres3[i+(157*2),:])
						zz=np.append(yy,wind3[i+(157*2),:])
						mm=np.append(yy,humid3[i+(157*2),:])
						hh=np.append(yy,height3[i+(157*2),:])
					else:
						pass

					ensdata2 = xx#np.append(temp3,pres3)
					yy = yy.reshape(len(yy), 1)
					zz = zz.reshape(len(zz), 1)
					mm = mm.reshape(len(mm), 1)
					hh = hh.reshape(len(hh), 1)
					ensdata2 = ensdata2.reshape(len(xx), 1)
##					ensdata2 = np.hstack((ensdata2,yy))
##					ensdata2 = np.hstack((ensdata2,zz))
##					ensdata2 = np.hstack((ensdata2,mm))
##					ensdata2 = np.append(ensdata2,hh)
					ensdata2 = np.insert(ensdata2, 0, yy, axis=1)
					#print ensdata2.shape
					#ensdata2 = ensdata2.reshape(len(xx), 2)
					#print ensdata2.shape
					#ensdata2 = ensdata2.reshape(len(ensdata2), 1)
					ensdata2 = np.insert(ensdata2, 0, zz, axis=1)
					ensdata2 = np.insert(ensdata2, 0, mm, axis=1)
					ensdata2 = np.insert(ensdata2, 0, hh, axis=1)
					#print ensdata2.shape
					pca = PCA(n_components=5)
					pca.fit(ensdata2)
					d33[i] = pca.explained_variance_ratio_[0]
				#print d33
				#d33[i]=pearcor(xx, yy)
				#print xx.shape
				#print height3.shape
				#print d33.shape

				vx1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vy1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
				vx1=np.array(vx1)
				vy1=np.array(vy1)
				d5=np.array(d33)
				d6=d5.reshape(lons.shape[0],lons.shape[1])
				for i in xrange(length):
						vx1[i]=1/(1+d6[i]**2)**0.5
						vy1[i]=d6[i]/(1+d6[i]**2)**0.5                 
				for i in xrange(0,lons.shape[0],lstl):
						for j in xrange(0,lons.shape[1],lstl):
							ax1.quiver(lons1[i][j],lats1[i][j],vx1[i][j],vy1[i][j],width=0.001,linewidth=0.1,scale=1/0.015,color= '#e0ecf4')

				canvas.show()
				if pca2.get()== 0:
						ax1.cla()
						plt.xlabel("Longtitude")
						plt.ylabel("Latitude")
						canvas.show()


##
##						temp3 = np.insert(temp3, 0, temp, axis=0)
##						pres3= np.insert(pres3, 0, pres, axis=0)
##						#return temp3,pres3,humid3,height3,windu3,windv3
##				#temp3,pres3,humid3,height3,windu3,windv3 = ensselect(temp1,pres1,humid1,height1,windu1,windv1)
##				ensdata2 = humid3#np.append(temp3,pres3)
##				ensdata2 = np.insert(ensdata2, 0, windv3, axis=1)
##				ensdata21 = windu3#np.append(temp3,pres3)
##				ensdata21 = np.insert(ensdata21, 0, height3, axis=1)
##				print ensdata2.shape
##				#ensdata2 = temp3       
####				ensdata2 = np.append(ensdata2,humid3,1)
####				ensdata2 = np.append(ensdata2,height3,1)
####				ensdata2 = np.append(ensdata2,windu3,1)
####				ensdata2 = np.append(ensdata2,windv3,1)
##
##				pca = PCA(n_components=2)
##				pca.fit(ensdata2)
##				print pca.explained_variance_ratio_.shape
##				print(pca.explained_variance_ratio_)
##				pca = PCA(n_components=2)
##				pca.fit(ensdata21)
##				print pca.explained_variance_ratio_.shape
##				print(pca.explained_variance_ratio_)
				
				
						

						
theta1a=[[330 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
theta2a=[[360 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
def filled_arc1(center, radius, theta1, theta2, ax, color):
	circ = mpatches.Wedge(center, radius, theta1, theta2, fill=True, color=color,zorder=0)
	ax.add_patch(circ)

def wideline(d3):
	#for i in xrange(lons.shape[0]):
	#for j in xrange(lons.shape[1]):
			if(0<d3<=0.1) or (-0.1<d3<=0):
				d3=d3*1.07
			elif(0.1<d3<=0.2) or (-0.2<d3<=-0.1):
				d3=d3*1.1
			elif(0.2<d3<=0.3) or (-0.3<d3<=-0.2):
				d3=d3*1.2
			elif(0.3<d3<=0.4) or (-0.4<d3<=-0.3):
				d3=d3*1.3
			elif(0.4<d3<=0.5) or (-0.5<d3<=-0.4):
				d3=d3*1.4
			elif(0.5<d3<=0.6) or (-0.6<d3<=-0.5):
				d3=d3*1.5
			elif(0.6<d3<=0.7) or (-0.7<d3<=-0.6):
				d3=d3*1.7
			elif(0.7<d3<=0.8) or (-0.8<d3<=-0.7):
				d3=d3*2.1
			elif(0.8<d3<=0.9) or (-0.9<d3<=-0.8):
				d3=d3*2.5
			elif(0.9<d3<=1) or (-1<d3<=-0.9):
				d3=d3*3
			return d3


def arcdraw(d3l,d3h,co):
	for i in xrange(0,lons.shape[0],lstl):
		for j in xrange(0,lons.shape[1],lstl):

					d3l[i][j]=float("%.2f" % round(d3l[i][j],2))
					if 2.6<d3l[i][j]<=3:
						theta1a[i][j]= d3l[i][j]-2.6+68
					elif 2.4<d3l[i][j]<=2.6:
						theta1a[i][j]= d3l[i][j]-2.4+66
					elif 2.2<d3l[i][j]<=2.4:
						theta1a[i][j]= d3l[i][j]-2.2+64
					elif 2<d3l[i][j]<=2.2:
						theta1a[i][j]= d3l[i][j]-2+63
					elif 1.95<d3l[i][j]<=2:
						theta1a[i][j]= d3l[i][j]-1.95+62
					elif 1.9<d3l[i][j]<=1.95:
						theta1a[i][j]= d3l[i][j]-1.9+61.5
					elif 1.85<d3l[i][j]<=1.9:
						theta1a[i][j]= d3l[i][j]-1.85+60.8
					elif 1.80<d3l[i][j]<=1.85:
						theta1a[i][j]= d3l[i][j]-1.8+60.5
					elif 1.75<d3l[i][j]<=1.8:
						theta1a[i][j]= d3l[i][j]-1.75+59.5
					elif 1.7<d3l[i][j]<=1.75:
						theta1a[i][j]= d3l[i][j]-1.7+58
					elif 1.65<d3l[i][j]<=1.7:
						theta1a[i][j]= d3l[i][j]-1.65+57.5
					elif 1.6<d3l[i][j]<=1.65:
						theta1a[i][j]= d3l[i][j]-1.6+57
					elif 1.55<d3l[i][j]<=1.6:
						theta1a[i][j]= d3l[i][j]-1.55+56
					elif 1.5<d3l[i][j]<=1.55:
						theta1a[i][j]= d3l[i][j]-1.5+55
					elif 1.45<d3l[i][j]<=1.5:
						theta1a[i][j]= d3l[i][j]-1.45+54
					elif 1.4<d3l[i][j]<=1.45:
						theta1a[i][j]= d3l[i][j]-1.4
					elif 1.35<d3l[i][j]<=1.4:
						theta1a[i][j]= d3l[i][j]-1.35+52
					elif 1.3<d3l[i][j]<=1.35:
						theta1a[i][j]= ((8)*(d3l[i][j]-1.3))*10+47
					elif 1.25<d3l[i][j]<=1.3:
						theta1a[i][j]= d3l[i][j]-1.25+50
					elif 1.2<d3l[i][j]<=1.25:
						theta1a[i][j]= d3l[i][j]-1.2+44.5
					elif 1.15<d3l[i][j]<=1.2:
						theta1a[i][j]= d3l[i][j]-1.15+48#((8)*(d3l[i][j]-1.15))*10+43
					elif 1.1<d3l[i][j]<=1.15:
						theta1a[i][j]= d3l[i][j]-1.1+46.5#((8)*(d3l[i][j]-1.1))*10+41.5
					elif 1.05<d3l[i][j]<=1.1:
						theta1a[i][j]= d3l[i][j]-1.05+45
					elif 1<d3l[i][j]<=1.05:
						theta1a[i][j]= (d3l[i][j]-1)+42
					elif 0.9<d3l[i][j]<=1:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.9))*10+37
					elif 0.85<d3l[i][j]<=0.9:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.85))*10+36
					elif 0.83<d3l[i][j]<=0.85:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.83))*10+35
					elif 0.8<d3l[i][j]<=0.83:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.8))*10+33
					elif 0.7<d3l[i][j]<=0.75:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.7))*10+33
					elif 0.75<d3l[i][j]<=0.8:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.75))*10+32
					elif 0.6<d3l[i][j]<=0.7:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.6))*10+26
					elif 0.52<d3l[i][j]<=0.6:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.52))*9+22
					elif 0.50<d3l[i][j]<=0.52:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.5))*10+24
					elif 0.4<d3l[i][j]<=0.5:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.4))*8+19
					elif 0.3<d3l[i][j]<=0.4:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.3))*9+15
					elif 0.2<d3l[i][j]<=0.3:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.2))*8+9
					elif 0.1<d3l[i][j]<=0.2:
						theta1a[i][j]= ((8)*(d3l[i][j]-0.1))*8+4
					elif 0<d3l[i][j]<=0.1:
						theta1a[i][j]= d3l[i][j]-0.1+1
					elif -0.1<d3l[i][j]<=0:
						theta1a[i][j]= ((360-355)*(d3l[i][j]+0.1))*10+355
					elif -0.2<d3l[i][j]<=-0.1:
						theta1a[i][j]= ((355-347)*(d3l[i][j]+0.2)*10)+348
					elif -0.3<d3l[i][j]<=-0.2:
						theta1a[i][j]= ((347-343)*(d3l[i][j]+0.3)*10)+345
					elif -0.4<d3l[i][j]<=-0.3:
						theta1a[i][j]= ((343-336)*(d3l[i][j]+0.4)*10)+336
					elif -0.50<d3l[i][j]<=-0.4:
						theta1a[i][j]= ((336-333)*(d3l[i][j]+0.50)*10)+335
					elif -0.60<d3l[i][j]<=-0.50:
						theta1a[i][j]= ((333-328)*(d3l[i][j]+0.6)*10)+330
					elif -0.70<d3l[i][j]<=-0.60:
						theta1a[i][j]= ((328-325)*(d3l[i][j]+0.7)*10)+327
					elif -0.80<d3l[i][j]<=-0.70:
						theta1a[i][j]= ((325-320)*(d3l[i][j]+0.8)*10)+324
					elif -0.90<d3l[i][j]<=-0.80:
						theta1a[i][j]= ((320-316)*(d3l[i][j]+0.9)*10)+320
					elif -1<=d3l[i][j]<=-0.90:
						theta1a[i][j]= ((316-310)*(d3l[i][j]+1)*10)+310                                     
					elif -1.1<d3l[i][j]<=-1:
						theta1a[i][j]= d3l[i][j]+1.2+318
					elif -1.2<d3l[i][j]<=-1.1:
						theta1a[i][j]= d3l[i][j]+1.2+314
					elif -1.6<d3l[i][j]<=-1.2:
						theta1a[i][j]= d3l[i][j]+1.6+307
					elif -2<d3l[i][j]<=-1.6:
						theta1a[i][j]= d3l[i][j]+2+304
					elif -2.5<d3l[i][j]<=-2:
						theta1a[i][j]= d3l[i][j]+2.5+298
					elif -2.8<d3l[i][j]<=-2.5:
						theta1a[i][j]= d3l[i][j]+3+294
					elif -3<=d3l[i][j]<=-2.8:
						theta1a[i][j]= d3l[i][j]+2.8+290
					if 2.6<d3h[i][j]<=3:
						theta2a[i][j]= d3h[i][j]-2.6+68
					elif 2.4<d3h[i][j]<=2.6:
						theta2a[i][j]= d3h[i][j]-2.4+66
					elif 2.2<d3h[i][j]<=2.4:
						theta2a[i][j]= d3h[i][j]-2.2+64
					elif 2<d3h[i][j]<=2.2:
						theta2a[i][j]= d3h[i][j]-2+63
					elif 1.95<d3h[i][j]<=2:
						theta2a[i][j]= d3h[i][j]-1.95+62
					elif 1.9<d3h[i][j]<=1.95:
						theta2a[i][j]= d3h[i][j]-1.9+61.5
					elif 1.85<d3h[i][j]<=1.9:
						theta2a[i][j]= d3h[i][j]-1.85+60.8
					elif 1.80<d3h[i][j]<=1.85:
						theta2a[i][j]= d3h[i][j]-1.8+60.5
					elif 1.75<d3h[i][j]<=1.8:
						theta2a[i][j]= d3h[i][j]-1.75+59.5
					elif 1.7<d3h[i][j]<=1.75:
						theta2a[i][j]= d3h[i][j]-1.7+58
					elif 1.65<d3h[i][j]<=1.7:
						theta2a[i][j]= d3h[i][j]-1.65+57.5
					elif 1.6<d3h[i][j]<=1.65:
						theta2a[i][j]= d3h[i][j]-1.6+57
					elif 1.55<d3h[i][j]<=1.6:
						theta2a[i][j]= d3h[i][j]-1.55+56
					elif 1.5<d3h[i][j]<=1.55:
						theta2a[i][j]= d3h[i][j]-1.5+55
					elif 1.45<d3h[i][j]<=1.5:
						theta2a[i][j]= d3h[i][j]-1.45+54
					elif 1.4<d3h[i][j]<=1.45:
						theta2a[i][j]= d3h[i][j]-1.4
					elif 1.35<d3h[i][j]<=1.4:
						theta2a[i][j]= d3h[i][j]-1.35+52
					elif 1.3<d3h[i][j]<=1.35:
						theta2a[i][j]= ((8)*(d3h[i][j]-1.3))*10+47
					elif 1.25<d3h[i][j]<=1.3:
						theta2a[i][j]= d3h[i][j]-1.25+50
					elif 1.2<d3h[i][j]<=1.25:
						theta2a[i][j]= d3h[i][j]-1.2+44.5
					elif 1.15<d3h[i][j]<=1.2:
						theta2a[i][j]= d3h[i][j]-1.15+48#((8)*(d3h[i][j]-1.15))*10+43
					elif 1.1<d3h[i][j]<=1.15:
						theta2a[i][j]= d3h[i][j]-1.1+46.5#((8)*(d3h[i][j]-1.1))*10+41.5
					elif 1.05<d3h[i][j]<=1.1:
						theta2a[i][j]= d3h[i][j]-1.05+45
					elif 1<d3h[i][j]<=1.05:
						theta2a[i][j]= (d3h[i][j]-1)+42
					elif 0.9<d3h[i][j]<=1:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.9))*10+37
					elif 0.85<d3h[i][j]<=0.9:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.85))*10+37
					elif 0.83<d3h[i][j]<=0.85:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.83))*10+35
					elif 0.8<d3h[i][j]<=0.83:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.8))*10+33
					elif 0.7<d3h[i][j]<=0.75:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.7))*10+33
					elif 0.75<d3h[i][j]<=0.8:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.75))*10+33
					elif 0.6<d3h[i][j]<=0.7:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.6))*10+26
					elif 0.52<d3h[i][j]<=0.6:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.52))*9+22
					elif 0.50<d3h[i][j]<=0.52:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.5))*10+24
					elif 0.4<d3h[i][j]<=0.5:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.4))*8+19
					elif 0.3<d3h[i][j]<=0.4:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.3))*9+15
					elif 0.2<d3h[i][j]<=0.3:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.2))*8+9
					elif 0.1<d3h[i][j]<=0.2:
						theta2a[i][j]= ((8)*(d3h[i][j]-0.1))*8+4
					elif 0<d3h[i][j]<=0.1:
						theta2a[i][j]= d3h[i][j]-0.1+1
					elif -0.1<d3h[i][j]<=0:
						theta2a[i][j]= ((360-355)*(d3h[i][j]+0.1))*10+355
					elif -0.2<d3h[i][j]<=-0.1:
						theta2a[i][j]= ((355-347)*(d3h[i][j]+0.2)*10)+348
					elif -0.3<d3h[i][j]<=-0.2:
						theta2a[i][j]= ((347-343)*(d3h[i][j]+0.3)*10)+345
					elif -0.4<d3h[i][j]<=-0.3:
						theta2a[i][j]= ((343-336)*(d3h[i][j]+0.4)*10)+336
					elif -0.50<d3h[i][j]<=-0.4:
						theta2a[i][j]= ((336-333)*(d3h[i][j]+0.50)*10)+335
					elif -0.60<d3h[i][j]<=-0.50:
						theta2a[i][j]= ((333-328)*(d3h[i][j]+0.6)*10)+330
					elif -0.70<d3h[i][j]<=-0.60:
						theta2a[i][j]= ((328-325)*(d3h[i][j]+0.7)*10)+327
					elif -0.80<d3h[i][j]<=-0.70:
						theta2a[i][j]= ((325-320)*(d3h[i][j]+0.8)*10)+324
					elif -0.90<d3h[i][j]<=-0.80:
						theta2a[i][j]= ((320-316)*(d3h[i][j]+0.9)*10)+320
					elif -1<=d3h[i][j]<=-0.90:
						theta2a[i][j]= ((316-310)*(d3h[i][j]+1)*10)+310                                     
					elif -1.1<d3h[i][j]<=-1:
						theta2a[i][j]= d3h[i][j]+1.2+318
					elif -1.2<d3h[i][j]<=-1.1:
						theta2a[i][j]= d3h[i][j]+1.2+314
					elif -1.6<d3h[i][j]<=-1.2:
						theta2a[i][j]= d3h[i][j]+1.6+307
					elif -2<d3h[i][j]<=-1.6:
						theta2a[i][j]= d3h[i][j]+2+304
					elif -2.5<d3h[i][j]<=-2:
						theta2a[i][j]= d3h[i][j]+2.5+298
					elif -2.8<d3h[i][j]<=-2.5:
						theta2a[i][j]= d3h[i][j]+3+294
					elif -3<=d3h[i][j]<=-2.8:
						theta2a[i][j]= d3h[i][j]+2.8+290
					if(theta1a[i][j]>theta2a[i][j]):
						theta1a[i][j]=theta2a[i][j]
			 
	for i in xrange(0,lons.shape[0],lstl):
		for j in xrange(0,lons.shape[1],lstl):
						filled_arc1((lons1[i][j],lats1[i][j]), 200000, theta1a[i][j], theta2a[i][j], ax1, co)
 


def prestemp1lo():
	time1, radius, level, varn1, varn2 = locationr()
	time1 = int(time1);radius = int(radius)
	ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
	'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
	,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
	,'ens_26','ens_27','ens_28','ens_29','ens_30']

	#time1=42;time2=46;distime=1
	r=radius
	enrand=ensembles[29]
	url=ensrand(enrand)[time1]
	dset = Dataset(url)
	lats = dset.variables['g3_lat_0'][:]
	lons = dset.variables['g3_lon_1'][:]
	lons=lons[:,:]
	lats=lats[:,:]
	if varn1== 'PRMSL_GDS3_MSL':
		temp = dset.variables[varn1][:]
		temp3=np.array(temp[:,:])
	elif varn1== 'UV_GRD_GDS3_ISBL':
		windu = dset.variables['U_GRD_GDS3_ISBL'][:]
		windv = dset.variables['V_GRD_GDS3_ISBL'][:]
		windu=np.array(windu[level,:,:])
		windv=np.array(windv[level,:,:])
		temp3=(windu**2+windv**2)**0.5
	else:
		temp = dset.variables[varn1][:]
		temp3=np.array(temp[level,:,:])
	if varn2== 'PRMSL_GDS3_MSL':
		pres = dset.variables[varn2][:]
		pres3=np.array(pres[:,:])
	elif varn2== 'UV_GRD_GDS3_ISBL':
		windu = dset.variables['U_GRD_GDS3_ISBL'][:]
		windv = dset.variables['V_GRD_GDS3_ISBL'][:]
		windu=np.array(windu[level,:,:])
		windv=np.array(windv[level,:,:])
		pres3=(windu**2+windv**2)**0.5
	else:
		pres = dset.variables[varn2][:]
		pres3=np.array(pres[level,:,:])	
	mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
	minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
	temp3=temp3.ravel()
	pres3=pres3.ravel()
	temp3 = temp3.reshape(len(temp3), 1)
	pres3 = pres3.reshape(len(pres3), 1)
	min11 = [[100000 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	max11 = [[-100000 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	counter = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	d3 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	for k in xrange(29):
		enrand=ensembles[k]
		#for timestep in xrange(time1,time2,distime):
		url=ensrand(enrand)[time1]
		dset = Dataset(url)
		lats = dset.variables['g3_lat_0'][:]
		lons = dset.variables['g3_lon_1'][:]
		lons=lons[:,:]
		lats=lats[:,:]
		if varn1== 'PRMSL_GDS3_MSL':
			temp = dset.variables[varn1][:]
			temp=np.array(temp[:,:])
		elif varn1== 'UV_GRD_GDS3_ISBL':
			windu = dset.variables['U_GRD_GDS3_ISBL'][:]
			windv = dset.variables['V_GRD_GDS3_ISBL'][:]
			windu=np.array(windu[level,:,:])
			windv=np.array(windv[level,:,:])
			temp=(windu**2+windv**2)**0.5
		else:
			temp = dset.variables[varn1][:]
			temp=np.array(temp[level,:,:])
		if varn2== 'PRMSL_GDS3_MSL':
			pres = dset.variables[varn2][:]
			pres=np.array(pres[:,:])
		elif varn2== 'UV_GRD_GDS3_ISBL':
			windu = dset.variables['U_GRD_GDS3_ISBL'][:]
			windv = dset.variables['V_GRD_GDS3_ISBL'][:]
			windu=np.array(windu[level,:,:])
			windv=np.array(windv[level,:,:])
			pres=(windu**2+windv**2)**0.5
		else:
			pres = dset.variables[varn2][:]
			pres=np.array(pres[level,:,:])
		mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
		minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
		temp3 = temp#np.insert(temp3, 0, temp, axis=1)
		pres3 = pres#np.insert(pres3, 0, pres, axis=1)

		meantemp=[]
		meanpres=[]
		max1=-10

		vx1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
		vy1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
		leng=175#temp3.shape[0]
		for i in xrange(lons.shape[0]):
			for j in xrange(lons.shape[1]):
				xx=temp3[i][j]
				yy=pres3[i][j]
				print len(xx)
				for k in xrange(r):
					if ((i-k)>=0):
						xx=np.append(xx,temp3[i-k][j])
						yy=np.append(yy,pres3[i-k][j])
						if ((j-k>=0)):
							xx=np.append(xx,temp3[i-k][j-k])
							yy=np.append(yy,pres3[i-k][j-k])
						if ((j+k<temp3.shape[1])):
							xx=np.append(xx,temp3[i-k][j+k])
							yy=np.append(yy,pres3[i-k][j+k])
					if ((j-k)>=0):
						xx=np.append(xx,temp3[i][j-k])
						yy=np.append(yy,pres3[i][j-k])
					if ((j+k)<temp3.shape[1]):
						xx=np.append(xx,temp3[i][j+k])
						yy=np.append(yy,pres3[i][j+k])
					if ((i+k)<temp3.shape[0]):
						if ((j-k)>=0):
							xx=np.append(xx,temp3[i+k][j-k])
							yy=np.append(yy,pres3[i+k][j-k])
						if ((j+k)<temp3.shape[1]):
							xx=np.append(xx,temp3[i+k][j+k])
							yy=np.append(yy,pres3[i+k][j+k])
						xx=np.append(xx,temp3[i+k][j])
						yy=np.append(yy,pres3[i+k][j])
				print len(xx)	
				d33[i][j]=pearcor(xx, yy)
				vx1[i][j]=1/(1+d33[i][j]**2)**0.5
				vy1[i][j]=d33[i][j]/(1+d33[i][j]**2)**0.5
				if d33[i][j]>max11[i][j]:
				    max11[i][j]=d33[i][j]
				if d33[i][j]<min11[i][j]:
				    min11[i][j]=d33[i][j]
		for i in xrange(0,lons.shape[0],lstl):
			for j in xrange(0,lons.shape[1],lstl):
				ax1.quiver(lons1[i][j],lats1[i][j],vx1[i][j],vy1[i][j],width=0.0006,linewidth=0.01,scale=1/0.035,color= '#f768a1')

	d3l=min11;d3h=max11

	arcdraw(d3l,d3h,'#fbb4b9')
	canvas.show()
	if lo1.get()== 0:
			ax1.cla()
			plt.xlabel("Longtitude")
			plt.ylabel("Latitude")
			canvas.show()



def prestemp1ti():
	time1, time2, level, varn1, varn2 = val()
	time1 = int(time1);time2 = int(time2)
	#print(time1,time2)
	ensembles=['ens_01','ens_02','ens_03','ens_04','ens_05','ens_06','ens_07',\
	'ens_08','ens_09','ens_10','ens_11','ens_12','ens_13','ens_14','ens_15','ens_16'\
	,'ens_17','ens_18','ens_19','ens_20','ens_21','ens_22','ens_23','ens_24','ens_25'\
	,'ens_26','ens_27','ens_28','ens_29','ens_30']
	#time1=42
	#time2=46;
	distime=1;dis=time2-time1+1
	#print(time1)
	r=1
	enrand=ensembles[29]
	url=ensrand(enrand)[time1]
	dset = Dataset(url)
	lats = dset.variables['g3_lat_0'][:]
	lons = dset.variables['g3_lon_1'][:]
	lons=lons[:,:]
	lats=lats[:,:]

	if varn1== 'PRMSL_GDS3_MSL':
		temp = dset.variables[varn1][:]
		temp3=np.array(temp[:,:])
	elif varn1== 'UV_GRD_GDS3_ISBL':
		windu = dset.variables['U_GRD_GDS3_ISBL'][:]
		windv = dset.variables['V_GRD_GDS3_ISBL'][:]
		windu=np.array(windu[level,:,:])
		windv=np.array(windv[level,:,:])
		temp3=(windu**2+windv**2)**0.5
	else:
		temp = dset.variables[varn1][:]
		temp3=np.array(temp[level,:,:])
	if varn2== 'PRMSL_GDS3_MSL':
		pres = dset.variables[varn2][:]
		pres3=np.array(pres[:,:])
	elif varn2== 'UV_GRD_GDS3_ISBL':
		windu = dset.variables['U_GRD_GDS3_ISBL'][:]
		windv = dset.variables['V_GRD_GDS3_ISBL'][:]
		windu=np.array(windu[level,:,:])
		windv=np.array(windv[level,:,:])
		pres3=(windu**2+windv**2)**0.5
	else:
		pres = dset.variables[varn2][:]
		pres3=np.array(pres[level,:,:])	
	mint=temp3.min();maxt=temp3.max();temp3=(temp3-mint)/(maxt-mint)
	minp=pres3.min();maxp=pres3.max();pres3=(pres3-minp)/(maxp-minp)
	temp3=temp3.ravel()
	pres3=pres3.ravel()
	temp3 = temp3.reshape(len(temp3), 1)
	pres3 = pres3.reshape(len(pres3), 1)
	min11 = [[100000 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	max11 = [[-100000 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	counter = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	d3 = [[0 for x in range(lons.shape[1])] for x in range(lons.shape[0])]
	for k in xrange(29):
		xx= np.zeros((lons.shape[0],lons.shape[1],dis))
		yy= np.zeros((lons.shape[0],lons.shape[1],dis))
		timfirst=time1
		for timestep in xrange(time1,time2,distime):
			index1=timestep-timfirst
			enrand=ensembles[k]
			#for timestep in xrange(time1,time2,distime):
			url=ensrand(enrand)[timestep]
			dset = Dataset(url)
			lats = dset.variables['g3_lat_0'][:]
			lons = dset.variables['g3_lon_1'][:]
			lons=lons[:,:]
			lats=lats[:,:]

			if varn1== 'PRMSL_GDS3_MSL':
				temp = dset.variables[varn1][:]
				temp=np.array(temp[:,:])
			elif varn1== 'UV_GRD_GDS3_ISBL':
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				windu=np.array(windu[level,:,:])
				windv=np.array(windv[level,:,:])
				temp=(windu**2+windv**2)**0.5
			else:
				temp = dset.variables[varn1][:]
				temp=np.array(temp[level,:,:])
			if varn2== 'PRMSL_GDS3_MSL':
				pres = dset.variables[varn2][:]
				pres=np.array(pres[:,:])
			elif varn2== 'UV_GRD_GDS3_ISBL':
				windu = dset.variables['U_GRD_GDS3_ISBL'][:]
				windv = dset.variables['V_GRD_GDS3_ISBL'][:]
				windu=np.array(windu[level,:,:])
				windv=np.array(windv[level,:,:])
				pres=(windu**2+windv**2)**0.5
			else:
				pres = dset.variables[varn2][:]
				pres=np.array(pres[level,:,:])
			mint=temp.min();maxt=temp.max();temp=(temp-mint)/(maxt-mint)
			minp=pres.min();maxp=pres.max();pres=(pres-minp)/(maxp-minp)
			temp3 = temp#np.insert(temp3, 0, temp, axis=1)
			pres3 = pres#np.insert(pres3, 0, pres, axis=1)
			#print(xx)
			meantemp=[]
			meanpres=[]
			max1=-10
			vx1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
			vy1=[[0.0 for xv in range(lons.shape[1])] for xv in range(lons.shape[0])]
			leng=175#temp3.shape[0]s
			#print(xx.shape)
			for i in xrange(lons.shape[0]):
				for j in xrange(lons.shape[1]):
					xx[i,j,index1]=temp3[i][j]
					yy[i,j,index1]=pres3[i][j]
					d33[i][j]=pearcor(xx[i][j], yy[i][j])
					vx1[i][j]=1/(1+d33[i][j]**2)**0.5
					vy1[i][j]=d33[i][j]/(1+d33[i][j]**2)**0.5
					if d33[i][j]>max11[i][j]:
					    max11[i][j]=d33[i][j]
					if d33[i][j]<min11[i][j]:
					    min11[i][j]=d33[i][j]
		for i in xrange(0,lons.shape[0],lstl):
			for j in xrange(0,lons.shape[1],lstl):
				ax1.quiver(lons1[i][j],lats1[i][j],vx1[i][j],vy1[i][j],width=0.00006,linewidth=0.01,scale=1/0.035,color= '#f768a1')
	d3l=min11;d3h=max11
	arcdraw(d3l,d3h,'#fbb4b9')
	canvas.show()
	if ti1.get()== 0:
			ax1.cla()
			plt.xlabel("Longtitude")
			plt.ylabel("Latitude")
			canvas.show()

			

#Map Entry
map2 = IntVar()
sampleSize3 = Checkbutton(mainframe, text="Map", variable=map2, command=map1)
sampleSize3.grid(column = 0, row = 0, sticky = W)#(W, E))

#Humidity Entry
vHumidity = IntVar()
Humiditysize = Checkbutton(mainframe, text="correlation between two variables", variable=vHumidity, command=preshumid1,selectcolor='#253494')
Humiditysize.grid(column = 0, row = 1, sticky = W)#(W, E))

#prestemphumid1
vprestemphumid = IntVar()
TempHeightsize = Checkbutton(mainframe, text="Correlation between three variables", variable=vprestemphumid, command=prestemphumid1, selectcolor='#e6550d')
TempHeightsize.grid(column = 0, row = 2, sticky = W)#(W, E))
#presinc1
vpresinc = IntVar()
TempHeightsize = Checkbutton(mainframe, text="Variable Increasing", variable=vpresinc, command=presinc1 ,selectcolor='#feb24c')
TempHeightsize.grid(column = 0, row = 3, sticky = W)#(W, E))
#Pressure Entry
vPressure = IntVar()
epres = Entry()
sampleSize4 = Checkbutton(mainframe, text="Variable Contour", variable = vPressure, command=pres1)
sampleSize4.grid(column = 0, row = 4, sticky = W)#(W, E))
#u3
#Correlation(pres-temp-time)-Uncertainety
ti1 = IntVar()
pca1 = Checkbutton(mainframe, text="Correlation(time)-Uncertainety", variable=ti1, command=prestemp1ti)
pca1.grid(column = 1, row = 0, sticky = W)#(W, E))

#Correlation(pres-temp-location)-Uncertainety
lo1 = IntVar()
regression12 = Checkbutton(mainframe, text="Correlation(location)-Uncertainety", variable=lo1, command=prestemp1lo)
regression12.grid(column = 1, row = 1, sticky = W)#(W, E))

#Cluster Entry
clusterac = IntVar()
clustera1 = Checkbutton(mainframe, text="Uncertainety", variable=clusterac, command=clusteringallcol)
clustera1.grid(column = 1, row = 2, sticky = W)#(W, E))

#clustertemp
clustertemp2 = IntVar()
clustertemp1 = Checkbutton(mainframe, text="Clustering Variables", variable=clustertemp2, command=clustertemp)
clustertemp1.grid(column = 1, row = 3, sticky = W)#(W, E))

#clusteensembles 
clusterens2 = IntVar()
clusteensembles1 = Checkbutton(mainframe, text="Clustering All Variables", variable=clusterens2, command=clusterensembles)
clusteensembles1.grid(column = 1, row = 4, sticky = W)#(W, E))
#Cluster Entry
cluster1 = IntVar()
sampleSize1 = Checkbutton(mainframe, text="Clustering Density", variable=cluster1, command=clustering1)
sampleSize1.grid(column = 2, row = 0, sticky = W)#(W, E))


#Cluster Entry
clustera = IntVar()
clustera1 = Checkbutton(mainframe, text="Clustering all(6)", variable=clustera, command=clusteringaxes)
clustera1.grid(column = 2, row = 1, sticky = W)#(W, E))

#Cluster2 Entry
clustern2 = IntVar()
sampleSize2 = Checkbutton(mainframe, text="Number of Clusters", variable=clustern2, command=clustering2)
sampleSize2.grid(column = 2, row = 2, sticky = W)#(W, E))

#PCA
pca2 = IntVar()
pca1 = Checkbutton(mainframe, text="PCA", variable=pca2, command=pcaf)
pca1.grid(column = 2, row = 3, sticky = W)#(W, E))

#Regression Entry
regression2 = IntVar()
regression12 = Checkbutton(mainframe, text="Regression", variable=regression2, command=regression1)
regression12.grid(column = 2, row = 4, sticky = W)#(W, E))


plt.xlabel("Longtitude")
plt.ylabel("Latitude")
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()
plt.close()

