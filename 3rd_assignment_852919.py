from wallCalculation import compositeWallParallel,compositeWallSeries,compositeWall,wallConvection,wallResistance,wallHeatTransfer
def materialSensitivity(material_List,resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside):
  Result=[None]*len(material_List)
  sc=0  
  for mate in material_list :
    r={}
    resistanceListParallel[1]["k"]=mate["k"]  
    heatTransfer = wallHeatTransfer(resistanceListSeries,resistanceListParallel,resistanceConv_internal,resistanceConv_external, T_inside,T_outside)
    r["Material"]=mate["name"]
    r["Heat Transfer [W]"]=heatTransfer
    Result[sc]=r
    sc=sc+1
  return Result

glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cement ={"name":"cement", "k": 1.5}
material_list = [ glassProp,brickProp,cement]

Ri={"name":"Ri","type":"conv","area":0.25,"hConv":10}
R1={"name":"R1","type":"cond","length":0.03,"area":0.25,"k":0.026}
R2={"name":"R2","type":"cond","length":0.02,"area":0.25,"k":0.22}
R3={"name":"R3","type":"cond","length":0.16,"area":0.015,"k":0.22}
R4={"name":"R4","type":"cond","length":0.16,"area":0.22,"k":0.72}
R5={"name":"R5","type":"cond","length":0.16,"area":0.015,"k":0.22}
R6={"name":"R6","type":"cond","length":0.02,"area":0.25,"k":0.22}
Ro={"name":"Ro","type":"conv","area":0.25,"hConv":25}

parallelSet = [R3,R4,R5]
serieSet= [R1,R2,R6]

Ti =20
To= 10

MatSensitivity=materialSensitivity(material_list,serieSet,parallelSet,Ri,Ro,Ti,To)
print MatSensitivity