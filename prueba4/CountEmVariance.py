from numpy import *
import numpy as np

def image_proc(count_files,Lx,Ly,Lprime_x,Lprime_y,samplingFraction,Nx,Ny):
    '''
    Función para calcular la varianza. Donde:
    Lx: es el lado del cuadrado pequeño  
    Lprime_x: es el lado del cuadrado grande
    Ly: es la altura del cuadrado pequeño  
    Lprime_y: es la altura del cuadrado grande
    
    '''
    nruns = 1

    A=Lx*Ly
    Aprime=Lprime_x*Lprime_y

    tau=samplingFraction
    const=(1-tau)**2/(3-2*tau)
    alpha=(1-tau)**2/(2-tau)/6

    num_faces_per_run=np.zeros(nruns)
    num_faces_per_q_run=np.zeros((Nx*Ny,nruns))
    nonzero_q_flag_per_run=np.zeros((Nx*Ny,nruns), dtype=np.int)
    nonzero_q_per_run=np.zeros(nruns)
    varq1=np.zeros(nruns)
    varN=np.zeros(nruns)
    varCav=np.zeros(nruns)
    varCavT=np.zeros(nruns)
    varNpoisson=np.zeros(nruns)

    Qi=np.zeros((Nx,nruns))
    Qie=np.zeros((Nx,nruns))
    Qio=np.zeros((Nx,nruns))
    ni=np.zeros((Nx,nruns))

    VarQi=np.zeros((Nx,nruns))
    C0=np.zeros(nruns)
    C1=np.zeros(nruns)
    C2=np.zeros(nruns)
    nu=np.zeros(nruns)

    tQi=np.zeros((Nx,nruns))
    tQie=np.zeros((Nx,nruns))
    tQio=np.zeros((Nx,nruns))
    tni=np.zeros((Nx, nruns))

    tVarQi=np.zeros((Nx,nruns))
    tC0=np.zeros(nruns)
    tC1=np.zeros(nruns)
    tC2=np.zeros(nruns)
    tnu=np.zeros(nruns)

    k=0
    kq=0
    kqnew=0
    respint=0
    respint_q=0
    nonzero_q=0
    ind = 0
    for i in range(Nx):
        for j in range(Ny):

            tempn = count_files[ind]
            ind = ind + 1

            num_faces_per_q_run[kq,k]=tempn
            tempn=0
            if num_faces_per_q_run[kq,k] != 0:
                nonzero_q=nonzero_q+1
                nonzero_q_flag_per_run[kq,k]=1
            kqnew=kqnew+1
            Qi[i,k]=Qi[i,k]+num_faces_per_q_run[kq,k]
            if num_faces_per_q_run[kq,k] != 0:
                ni[i,k]=ni[i,k]+1
            if (j % 2) == 0:
                Qio[i,k]=Qio[i,k]+num_faces_per_q_run[kq,k]
            if (j % 2) == 1:
                Qie[i,k]=Qie[i,k]+num_faces_per_q_run[kq,k]
            tQi[j, k] = tQi[j, k] + num_faces_per_q_run[kq, k]
            if num_faces_per_q_run[kq,k] != 0:
                tni[j,k]=tni[j,k]+1
            if (i % 2) == 0:
                tQio[j,k]=tQio[j,k]+num_faces_per_q_run[kq,k]
            if (i % 2) == 1:
                tQie[j,k]=tQie[j,k]+num_faces_per_q_run[kq,k]

            kq=kq+1
        VarQi[i,k]=const*(Qio[i,k]-Qie[i,k])**2

    for j in range(Ny):
        tVarQi[j,k]=const*(tQio[j,k]-tQie[j,k])**2

    nindex=nonzero(nonzero_q_flag_per_run[:,k])
    nonzero_q_per_run[k]=nonzero_q
    num_faces_per_run[k]=sum(num_faces_per_q_run[:,k])
    C0[k]=sum(Qi[:,k]**2)
    C1[k]=sum(Qi[0:Ny-1,k]*Qi[1:Ny,k])
    C2[k]=sum(Qi[0:Ny-2,k]*Qi[2:Ny,k])
    nu[k]=sum(VarQi[:,k])

    tC0[k]=sum(tQi[:,k]**2)
    tC1[k]=sum(tQi[0:Ny-1,k]*tQi[1:Ny,k])
    tC2[k]=sum(tQi[0:Ny-2,k]*tQi[2:Ny,k])
    tnu[k]=sum(tVarQi[:,k])

    varCav[k]=alpha*(3*(C0[k]-nu[k])-4*C1[k]+C2[k]) / tau**4 + nu[k] / tau**4
    varCavT[k]=0.5 * varCav[k] + 0.5 * alpha * (3 * (tC0[k] - tnu[k]) - 4 * tC1[k] + tC2[k]) / tau**4 + tnu[k] / tau**4
    if varCav[k] < 0:
        varCav[k]=0
    varq1[k]=var(num_faces_per_q_run[nindex,k])
    varN[k]=nonzero_q_per_run[k]*varq1[k]/tau**4
    varNpoisson[k]=num_faces_per_run[k]/tau**4
    meanNhat=mean(num_faces_per_run)*float(A)/float(Aprime)
    var_Nhat=var(num_faces_per_run)*float(A)**2/float(Aprime)**2

    varCav = varCavT

    varNPoisson = sqrt(varNpoisson[k])
    varCav = sqrt(varCav[k])
    varN = sqrt(varN[k])

    return varN,varCav,varNPoisson,meanNhat

#Ejemplo de uso:
# 25 Muestreos
# Quadrat: 50x30
# Rectangulo exterior: 200x120
# Fraccion de muestreo: 0.25
# Numero de quadrats por fila: 5
# Numero de quadrats por columna: 5
# Angulo de reotacion de la regilla: 0
varN, varCav, varNPoisson, meanNhat = image_proc([1,2,1,0,0,0,1,1,0,0,1,2,2,1,1,0,1,0,1,2,3,4,1,2,3],50,30,200,120,0.25,5,5)

print("Estimated: " + str(meanNhat))        # --> Numero estimado de particulas contadas
print("VarN: " + str(varN))                 # --> Varianzas N, Cav y Poisson 
print("VarCav: " + str(varCav))
print("VarNPoisson: " + str(varNPoisson))


# Jose, así adapto para el calculo de la varianza general

def varc(ag, ap, a):
    Nx, Ny = a.shape
    Lx = np.sqrt(ap)
    Ly = Lx
    Lprime_x = np.sqrt(ag)
    Lprime_y = Lprime_x
    samplingFraction = Lx/Lprime_x
    temp = a.copy()
    temp = temp.reshape(Nx * Ny).tolist()
    print(f'(temp,  {Lprime_x}, {Lprime_y}, {Lx}, {Ly}, {samplingFraction}, {Nx}, {Ny})')
    return image_proc(temp,  Lprime_x, Lprime_y, Lx, Ly, samplingFraction, Nx, Ny)[-1]
