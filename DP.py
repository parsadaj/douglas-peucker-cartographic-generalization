import numpy as np,matplotlib.pyplot as plt
def fasele(x,y,x1,y1,x2,y2):
    #in tabe faseleye noghtei ba mokhtasate (x[i],y[i]) ra az khate gozarande az 2 noghteye (x1,y1) va (x2,y2) mohasebe mikonad.
    #moadele khat ra y - ax -b = 0 dar nazar migirim.
    d=[]
    if x1==x2:
        for i in range(len(x)):
            d.append(x[i]-x1) # in darsuratist ke zarib e y barabare 0 bashad. ( ke dar moadeleye y - ax -b = 0 dar nazar gerefte nashode)
    else:
        a,b=np.matmul(np.linalg.inv([[x1,1],[x2,1]]),[y1,y2]) # a va b ba hade aghal morabaat mohasebe mishavand.
        for i in range(len(x)):
            d.append(abs(y[i]-a*x[i]-b)/np.sqrt(1+a**2)) # formule fasele
    return d


def DP(x,y,d0):
    d=fasele(x,y,x[0],y[0],x[-1],y[-1])
    print('x,y=\n',x,'\n',y)
    print('d=',d)
    print('max(d)=',np.max(d))
    if np.max(d)<d0: # agar tamame fasele ha az hadde astane kamtar bashand noghate ebteda va enteha be ham vasl mishavand.
        plt.plot([x[0],x[-1]],[y[0],y[-1]],'r') 
    else: # dar gheire in surat noghat be 2 ghesmat taghsim shode va dobare baraye har ghesmat algorithme Douglas-Peucker ejra mishavad.
        DP(x[0:np.argmax(d)+1],y[0:np.argmax(d)+1],d0)
        DP(x[np.argmax(d):],y[np.argmax(d):],d0)


i=0
x=[]
y=[]
print('x va y e noghat ra vared konid.\npas az vared kardane tamame noghat ebarate end ra joloye x type konid.')
while True: # halgheye daryafte noghat az karbar
    
    text1='x['+str(i)+']='
    text2='y['+str(i)+']='
    x1=(input(text1))
    if x1=='end':
        break
    else:
        y1=(input(text2))
    i=i+1
    x.append(float(x1))
    y.append(float(y1))
t=float(input('d0=')) # daryfte hade astane az karbar
DP(x,y,t)  # farakhanie tabe e Douglas-Peucker
plt.plot(x,y,'bo') # namayeshe noghate vared shode tavasote karbar jahate moghayese ba khotute ras shode tavasote algorithm
plt.show()
