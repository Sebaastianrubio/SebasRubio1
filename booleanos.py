
def caracteres():
hombres_edad =  '21'
Mujeres_edad =  '18'
Carlos_edad =  '23'
Juan_edad = '18'
Marita_edad = '29'
     
#Comprobamos si los tres cumplen la edad mínima
if Carlos_edad > Hombres_edad and Juan_edad > Hombres_edad and Marita_edad > Mujeres_edad:
    print ("Pueden pasar los tres porque cumplen la edad minima")
#Comprobamos si alguno no la cumple    
if Carlos_edad < Hombres_edad or Juan_edad < Hombres_edad or Marita_edad < Mujeres_edad:
    print ("Alguno no cumple la condicion de edad, no pueden entrar juntos")
#Validamos que Cumplan 
if Carlos_edad > Hombres_edad:
    print ("Carlos puedes pasar")
else:
    print ("Carlos no puedes pasar")
if Juan_edad > Hombres_edad:
    print ("Juan puedes pasar")
else:
    print ("Juan no puedes pasar")
if Marita_edad > Mujeres_edad:
    print ("Marita puedes pasar")
else:
    print ("Marita no puedes pasar")
