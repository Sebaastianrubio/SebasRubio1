print("UNIVERSIDAD ESTATAL AMAZONICA")
file=open('my_notes.txt','r')
print(file)
linea=file.readlines()
print(linea)
file.close()


with open('my_notes2.txt','w') as archivo:
    archivo.write ('anthony\nsebastian\nflores123455\nuniversidad_estatal_Amazonica\n0997310296')
