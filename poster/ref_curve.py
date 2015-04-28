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

def refl(q):
	r0= 0.995
	qc= 2.17e-2
	m = 3.6
	a = 3.99
	w = 1e-3
	if q <= qc:
		return r0
	else:
		c = 1.-numpy.tanh((q-m*qc)/w)
		d = 1.-a*(q-qc)
		return r0/2.*c*d


f=pylab.figure()
ax=f.add_subplot(111)

x=numpy.linspace(0,.1,100)
y=[]
for i in range(0,len(x)):
	y.append(refl(x[i]))

ax.plot(x,y,linewidth=2)

ax.set_xlabel(r'Q (\AA$^{-1}$)')
ax.set_ylabel(r'Reflectivity')

ax.grid('on')
ax.set_ylim([-0.1,1.1])
ax.set_xlim([0.0,.1])

pylab.show()