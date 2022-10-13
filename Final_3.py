import math
import numpy as np
from scipy import interpolate
from matplotlib import ticker, cm
import matplotlib.pyplot as plt
plt.rc('font',family='Times New Roman')
import cmaps
import pandas as pd

def plot_contour(DataValue,SaveName,L):

           fig = plt.figure(figsize = (30, 12))
           axf = fig.gca()
           for axis in ['top','bottom','left','right']:
                      axf.spines[axis].set_linewidth(2)
           plt.rcParams['xtick.direction']='in'
           plt.rcParams['ytick.direction']='in'
           plt.yticks(fontproperties = "Times New Roman", size = 20) 
           plt.xticks(fontproperties = "Times New Roman", size = 20) 
           plt.grid(linestyle="--", linewidth='1.5')
           plt.xlabel("The Coordinate of X Axis /(A)", fontsize=25, fontproperties="Times New Roman")
           plt.ylabel("The Coordinate of Y Axis /(A)", fontsize=25, fontproperties="Times New Roman")
           plt.xlim(left=0, right=L )
           
           Temp = np.array(DataValue)       
           x_value = Temp[:, 0]
           y_value = Temp[:, 1]
           Value = Temp[:, 2]

           x,y = np.meshgrid(x_value, y_value)
           Value = interpolate.griddata((x_value, y_value), Value, (x, y), method='cubic')
           im = plt.contourf(x, y, Value, cmap='jet')

           plt.colorbar(im)
           plt.savefig(SaveName)
           cbar = plt.colorbar(im)
           #plt.show()

           return cbar.vmax
##           print(cbar.vmax, cbar.vmin)

def compute_StressValue(xvalue):

           SigmaX = []
           SigmaY = []
           TauXY = []
           MiseStress = []
           SigmaZ = []
           
           for i in range(len(xvalue)):
                      x = xvalue[i]
                      
                      hx =defhx(x)
                      ylo = c1*x - 1/2*hx
                      yli = c1*x + 1/2*hx
                      ynumber = int((yli-ylo)/0.08)
                      yvalue = np.linspace(ylo, yli, ynumber)

                      cx =defcx(x)
                      Hx = defHx(x)
                      Mx = defMx(x)
                      Vx = defVx(x)
                      
                      sigmax0 = defsigmax0(Hx, hx)
                      sigmax1 = defsigmax1(Mx, hx)
                      tau0 = deftau0(Vx, hx)

                      for j in range(len(yvalue)):
                                 y = yvalue[j] 
                                 by =defby(cx, y, hx)     
                                 sigmax = -defsigmax(by, sigmax0, sigmax1)
                                 sigmay = defsigmay(sigmax)
                                 tauxy = -deftau(sigmax0, sigmax1, by, tau0)

                                 epsilonx = defepsilonx (sigmax, sigmay)
                                 epsilony = defepsilony (sigmax, sigmay)
                                 sigmaz = defsigmaz (epsilonx, epsilony)

                                 sigmah = defsigmah(sigmax, sigmay, sigmaz) 
                                 sigmaxp = defsigmaxp(sigmax, sigmah)
                                 sigmayp = defsigmayp(sigmax, sigmah)
                                 sigmazp = defsigmazp(sigmax, sigmah)
                                 sigmaxyp = defsigmaxyp(tauxy)
                                 Mise = defMise(sigmaxp, sigmayp, sigmazp, sigmaxyp)
                                 
                                 SigmaX.append([x, y, sigmax])
                                 SigmaY.append([x, y, sigmay])
                                 SigmaZ.append([x, y, sigmaz])
                                 TauXY.append([x, y, tauxy])
                                 MiseStress.append([x, y, Mise])

           return SigmaX, SigmaY, SigmaZ, TauXY, MiseStress

def compute_StressValueLine(xvalue):

           SigmaX = []
           SigmaY = []
           TauXY = []
           MiseStress = []
           SigmaZ = []
           
           for i in range(len(xvalue)):
                      x = xvalue[i]
                      
                      hx =defhx(x)
                      ylo = c1*x - 1/2*hx
                      yli = c1*x + 1/2*hx

                      cx =defcx(x)
                      Hx = defHx(x)
                      Mx = defMx(x)
                      Vx = defVx(x)
                      print('x=', x, 'Mx=', Mx)
                      
                      sigmax0 = defsigmax0(Hx, hx)
                      sigmax1 = defsigmax1(Mx, hx)
                      tau0 = deftau0(Vx, hx)

                      y = yli
                      by =defby(cx, y, hx)     
                      sigmax = -defsigmax(by, sigmax0, sigmax1)
                      sigmay = defsigmay(sigmax)
                      tauxy = -deftau(sigmax0, sigmax1, by, tau0)

                      epsilonx = defepsilonx (sigmax, sigmay)
                      epsilony = defepsilony (sigmax, sigmay)
                      sigmaz = defsigmaz (epsilonx, epsilony)

                      sigmah = defsigmah(sigmax, sigmay, sigmaz) 
                      sigmaxp = defsigmaxp(sigmax, sigmah)
                      sigmayp = defsigmayp(sigmax, sigmah)
                      sigmazp = defsigmazp(sigmax, sigmah)
                      sigmaxyp = defsigmaxyp(tauxy)
                      Mise = defMise(sigmaxp, sigmayp, sigmazp, sigmaxyp)
                      
                      SigmaX.append([x, sigmax])
                      SigmaY.append([x, sigmay])
                      SigmaZ.append([x, sigmaz])
                      TauXY.append([x, tauxy])
                      MiseStress.append([x, Mise])

           return SigmaX, SigmaY, SigmaZ, TauXY, MiseStress

defHx = lambda x: q*(L-x)+Fx
defVx = lambda x: p*(L-x)+Fy
defMx = lambda x: (p-c1*q)*(L*x-1/2*x*x-1/2*L*L)+(Fy-c1*Fx)*(x-L)

defhx = lambda x: h1*x + h0         #棱柱在不同横坐标处的高度
defcx = lambda x: c1*x
defby = lambda cx, y, hx: 2*(cx - y)/ hx

defsigmax0 = lambda Hx, hx: Hx/hx
defsigmax1 = lambda Mx, hx: 6*Mx/(pow(hx, 2))
defsigmax = lambda by, sigmax0, sigmax1: sigmax0 + by*sigmax1
defsigmay = lambda sigmax: pow(h1,2)*sigmax
deftau0 = lambda Vx, hx: -Vx/hx
deftau = lambda sigmax0, sigmax1, by, tau0: (c1*sigmax0 - 1/2*h1*sigmax1) * (-1/2+3/2*by) - (- 1/2*h1*sigmax0 - c1*sigmax1)*by+3/2*tau0*(1-pow(by,2))

defepsilonx = lambda sigmax, sigmay: 1/E*(sigmax - miu*sigmay)
defepsilony = lambda sigmax, sigmay: 1/E*(-miu*sigmax + sigmay)
defsigmaz = lambda epsilonx, epsilony: E*miu*(epsilonx+epsilony)/((1-2*miu)*(1+miu))
defsigmah = lambda sigmax, sigmay, sigmaz: (sigmax + sigmay + sigmaz)/3 
defsigmaxp = lambda sigmax, sigmah: sigmax-sigmah
defsigmayp = lambda sigmay, sigmah: sigmay-sigmah
defsigmazp = lambda sigmaz, sigmah: sigmaz-sigmah
defsigmaxyp = lambda tau: tau
defMise = lambda sigmaxp, sigmayp, sigmazp, sigmaxyp : pow(3/2*(pow(sigmaxp, 2) + pow(sigmayp, 2) + pow(sigmazp, 2) + pow(sigmaxyp, 2)), 1/2)

defChiH = lambda hx: -8*c1*h1/(5*G*pow(hx,2))
defChiV = lambda hx: -3*h1/(5*G*pow(hx,2))
defChiM = lambda hx: (9*pow(h1,2)/(5*G*pow(hx,3)) + 12*pow(c1,2)/(G*pow(hx,3)) + 12/(E*pow(hx,3)))
defGammaH = lambda hx: c1/(5*G*hx)
defGammaV = lambda  hx: 6/(5*G*hx)
defGammaM = lambda hx: -3*h1/(5*G*pow(hx,2))

"""定义常参数"""
global theta, c1, L, hL, h0, h1, E, G, miu, Fy, press, q, p, Fx

theta = math.pi/18
c1 = math.tan(theta)            #棱柱中心线的斜率
L = 2.1                 #棱柱在水平方向的长度
hL = 0.3               #棱柱在x=L处的高度
h0 = 0.6               #棱柱在x=0处的高度
h1 = (hL - h0) / L               #描述棱柱高度改变率的参数

E = 100000
G = 40000
miu = 0.25

Fy = -100                 #集中载荷
press = 1             #均布载荷
q = -press*math.sin(theta)
p = press*math.cos(theta)
Fx = -press * 1/2 * hL

#xvalue = np.hstack( [np.linspace(0, L/10, 100), np.linspace(L/10, L, 300)])
xvalue = np.linspace(0, L, 100)
"""绘制应力云图"""
SigmaX, SigmaY, SigmaZ, TauXY, MiseStress = compute_StressValue(xvalue)
SaveName = ['SigmaX','SigmaY','SigmaZ','TauXY','MiseStress']
plot_contour(SigmaX,SaveName[0], L)
plot_contour(SigmaY,SaveName[1], L)
plot_contour(SigmaZ,SaveName[2], L)
plot_contour(TauXY,SaveName[3], L)
plt.show()
MaxMiseStress = plot_contour(MiseStress,SaveName[4], L)
print('最大等效应力为：', MaxMiseStress)

"""输出梁模型最下面边界的结果"""
SigmaXLine, SigmaYLine, SigmaZLine, TauXYLine, MiseStressLine = compute_StressValueLine(xvalue)


np.savetxt('SigmaXLine.txt', SigmaXLine)
np.savetxt('SigmaYLine.txt', SigmaYLine)
np.savetxt('SigmaZLine.txt', SigmaZLine)
np.savetxt('TauXYLine.txt', TauXYLine)
np.savetxt('MiseStressLine.txt', MiseStressLine)
