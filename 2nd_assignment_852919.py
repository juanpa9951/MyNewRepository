def RCalcSeries(resistances):
    resistancesResults = {}
    R_tot=0
    for resistance in resistances:
        type_resistance = resistance["type"]
        if type_resistance == "cond":
            A = resistance["area"]
            L = resistance["length"]
            k = resistance["k"]
            R= round(L/(k*A),2)
                
        if type_resistance=="conv":
            A = resistance["area"]
            h = resistance["hConv"]
            R=round(1/(h*A),2)
            
        R_tot=R_tot+R
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)


    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults 

def RCalcParallel(resistances):
    resistancesResults = {}
    R_tot_inv=0
    for resistance in resistances:
        type_resistance = resistance["type"]
        if type_resistance == "cond":
            A = resistance["area"]
            L = resistance["length"]
            k = resistance["k"]
            R= round(L/(k*A),2)
            R_inv= 1/(R)          
        if type_resistance=="conv":
            A = resistance["area"]
            h = resistance["hConv"]
            R=round(1/(h*A),2)
            R_inv=1/(R)
        R_tot_inv += R_inv   # this is the same as R_tot_inv=R_tot_inv + R_inv
        nameOfResistance = resistance["name"]
        resistancesResults[nameOfResistance] = round(R,2)

    R_tot = 1/R_tot_inv
    resistancesResults["R_total"] = round(R_tot,2)  
    return resistancesResults  

Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
parallelSetResults = RCalcParallel(parallelSet)
R_parallel = parallelSetResults["R_total"]
print(parallelSetResults)

SerieSet = [Ri,R1,R2,R6,Ro]
SerieSetResults = RCalcSeries(SerieSet)
R_series = SerieSetResults["R_total"]
print(SerieSetResults)

R_overAll = R_parallel + R_series
print(R_overAll)


         
            
    
        
    
        
        