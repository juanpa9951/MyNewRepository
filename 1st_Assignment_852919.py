# -*- coding: utf-8 -*-
def RCalc():
    n_res=raw_input("How many Resistances you have ? ")
    print("Please assign an INDEX from 1 to "+str(int(n_res))+" to each Resistance \n and fill the following information: ")
    R_vect = [None]*(int(n_res)+1) 
    for j in range(1,int(n_res)+1):
       print("\n Resistance number "+str(j))
       ty=raw_input("Conductive[1] or Convective[2] ")
       if ty==str(1) :
          L=raw_input("Please Enter the LENGHT of the layer (in m): ")
          A_string=raw_input("Please enter the AREA of the layer (in m2): ")
          A=float(A_string)
          k=raw_input("Please Enter the CONDUCTIVITY of the layer (in W/(m*K)): ")
          R_vect[j]=float(L)/float(k)/A
       else:
          A_string=raw_input("Please enter the AREA of the layer (in m2): ")
          A=float(A_string)
          h=raw_input("Please Enter the convective Heat Transfer Coefficient [W/m2K ] ")
          R_vect[j]=1/(float(h)*A)

    if int(n_res)>1:
        print("\n NOW lets simplify Parallel and Series groups in LOGICAL ORDER and One at the time!!")
        j3=1
        while j3==1:
            j1=raw_input(" Simplify Parallel [1] or Series[2] Group? ")
            if j1==str(1) :
                z=raw_input("How many are in this parallel group? ")   
                PRinv=0
                for k in range(0,int(z)):
                    u=raw_input("Whats the ASSIGNED INDEX of the "+str(k+1)+" Resistance in this group ? ")
                    u=int(u)       
                    PRinv=PRinv+1/R_vect[u]
                    R_vect[u]=0
                PR=1/PRinv
                R_vect[u]=PR
                print("\n The Equivalent Parallel Resistance of this group is "+str(PR)+" ºC/W \n It has been saved and RE-ASSIGNED! to Resistance Number "+str(u)+" ")
                j4=raw_input("Are there more Parallel or Series groups? Y or N ")
                if j4=="N" :
                    j3=0                          
            else :
                z=raw_input("How many Resistances are in this series group? ")   
                SR=0
                for k in range(0,int(z)):
                    u=raw_input("Whats the ASSIGNED INDEX of the "+str(k+1)+" Resistance in this group ? ")
                    u=int(u)       
                    SR=SR+R_vect[u]
                    R_vect[u]=0
                R_vect[u]=SR
                print("\n The Equivalent Series Resistance of this group is "+str(SR)+" ºC/W \n It has been saved and RE-ASSIGNED! to Resistance Number "+str(u)+" ")
                j4=raw_input("Are there more Parallel or series groups? Y or N ")
                if j4=="N" :
                    j3=0
        
        REQ=R_vect[u]
    else:
      REQ=R_vect[1]
    print("\n The Total Resistance is :"+str(REQ)+" ºC/W")
    return REQ

RCalc()