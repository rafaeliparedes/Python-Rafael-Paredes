#Programa para calcular cantidad de masa de arepas
#Se declaran los ingredientes y sus medidas estandar

agua = 1 # Agua se da en tazas
harina = 1 # harina se da en tazas 
aceite = 1/16 # aceite se da en cdas
sal = 1/16/3 # sal se da en cdtas

print("cada unidad de agua representa una taza")
print("cada unidad de harina representa una taza")
print("cada unidad de aceite esta en cdas y representa 1/16 de una taza")
print("cada unidad de sal esta en cdtas y representa 1/16/3 de una taza")
#empieza la preparacion añadiendo herramientas

bol = agua + harina + sal 
budare = bol + aceite

# se solicita al usuario cantidad de cada ingrediente
# asignando nuevas variables a inputs.
#transfiriendo inputs a floats o ints para poder operarlos. 

cagua = input("cuantas tazas de agua desea agregar? ") #respuesta es int. 
cagua = float(cagua) * agua #cambio a float y multiplicacion automatica por unidad. 

charina = input("cuantas tazas de harina desea agregar? ")
charina = float(charina) * harina 

csal = input ("cuantas cdtas de sal desea agregar" )
csal= float(csal) *1/16/3 #conversion de cdtas a tazas para misma unidad en resultado

#con las cantidades ya convertidas, se suman y se añaden a un bol

cbol= cagua + charina + csal 
print(f"en el bol hay {cbol} tazas de masa ")

caceite = input("cuantas cdas de aceite desea agregar al budare ")
caceite = float(caceite) *1/16 #conversion de cdas a tazas

masa_final= cbol + caceite 

print(f"la cantidad de masa resultante en las arepas dinamicas es de {masa_final} tazas")
#se une texto con resultado a traves de f-string
masa_final = int(masa_final) #conversion de float a entero para dar aproximado entero 
print(f"esto equivale a un aproximado de {masa_final} tazas")

#fin del programa!