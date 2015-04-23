#! /home/l_bergmann/anaconda/bin/python -W ignore
### loads
import numpy, pylab, cPickle, copy
from MCNPtools.mctal import mctal
from MCNPtools.plot import plot
from MCNPtools.tally import tally
from scipy import optimize
import matplotlib.pyplot as plt


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=16)


eigerPD       = mctal('/home/l_bergmann/Desktop/EIGERSS/gold/sab/eigerPD.mctal',        tex=True,verbose=False)
eigerPLATE    = mctal('/home/l_bergmann/repos/EIGER-PLATE/noref/run1/eigerPLATE.mctal',    tex=True,verbose=False)
eigerPLATEref = mctal('/home/l_bergmann/repos/EIGER-PLATE/ref/run1/eigerPLATEref.mctal', tex=True,verbose=False)


f=open('/home/l_bergmann/repos/EIGER/combined/new-wwg/20359.total_spec','r')
ws=cPickle.load(f)
f.close()

f=open('/home/l_bergmann/repos/EIGER-DXT/combined/81202.total_spec','r')
sapp=cPickle.load(f)
f.close()

def make_steps(ax,bins_in,avg_in,values_in,options=['log'],label='',ylim=False,color=False,linewidth=1):
	import numpy
	assert(len(bins_in)==len(values_in)+1)

	### make copies
	bins=bins_in[:]
	values=values_in[:]
	avg=avg_in[:]
	#err=err_in[:]

	### make rectangles
	x=[]
	y=[]
	x.append(bins[0])
	y.append(0.0)
	for n in range(len(values)):
		x.append(bins[n])
		x.append(bins[n+1])
		y.append(values[n])
		y.append(values[n])
	x.append(bins[len(values)])
	y.append(0.0)

	### plot with correct scale
	if 'lin' in options:
		if 'logy' in options:
			if color:
				ax.semilogy(x,y,label=label,color=color,linewidth=linewidth)
			else:
				ax.semilogy(x,y,label=labe,linewidth=linewidthl)
		else:
			if color:
				ax.plot(x,y,label=label,color=color,linewidth=linewidth)
			else:
				ax.plot(x,y,label=label,linewidth=linewidth)
	else:   #default to log if lin not present
		if 'logy' in options:
			if color:
				ax.loglog(x,y,label=label,color=color,linewidth=linewidth)
			else:
				ax.loglog(x,y,label=label,linewidth=linewidth)
		else:
			if color:
				ax.semilogx(x,y,label=label,color=color,linewidth=linewidth)
			else:
				ax.semilogx(x,y,label=label,linewidth=linewidth)


f=pylab.figure()
ax1=f.add_subplot(111)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
ax2 = ax1.twinx()
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

make_steps(ax1,  ws[0],[0],  ws[1], options=['log'],color='b',label='Water Scatterer',  linewidth=2)
make_steps(ax2,sapp[0],[0],sapp[1], options=['log'],color='g',label='Sapphire',         linewidth=2)

ax1.grid('on')
ax2.grid('on')
ax1.set_ylabel(r'W. Scatterer Total Current (n p$^{-1}$)')
ax2.set_ylabel(r'Sapphire Total Current (n p$^{-1}$)')

ax1.set_xlabel(r'Energy (MeV)')

ax1.set_xlim([1e-10,100])

ax2.set_ylim([0,1.31e-5])
ax2.set_yticks(numpy.linspace(0, 1.31e-5, 9))


for tl in ax1.get_yticklabels():
    tl.set_color('b')
for tl in ax2.get_yticklabels():
    tl.set_color('g')

handles1, labels1 = ax1.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(handles1+handles2,labels1+labels2,loc=1,prop={'size':12})
ax2.legend(handles1+handles2,labels1+labels2,loc=1,prop={'size':12})

pylab.show()