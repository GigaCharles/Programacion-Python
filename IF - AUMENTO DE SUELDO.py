# De un operario se conoce su sueldo y los años de antiguedad. Se pide crear un programa que lea estos datos de entrada e informe: 

# Si el sueldo es inferior a 500 y su antiguedad es igual o superior a 10 años otorgarle un aumento del 20% 

# Si el sueldo es inferior a 500 perosu antiguedad es menor a 10 años, otorgarle un aumento del 5%

# Si el sueldo es mayor o igual a 500, no hay aumento

# MOstrar el resultado a pagar

sueldo = float(input("Ingrese su sueldo: "))
antiguedad = int(input("Ingrese su antiguedad dentro de la empresa: "))

if sueldo < 500 and antiguedad >= 10:
  print("¡TIENE UN AUMENTO DEL 20% EN SU SUELDO!")
  aumento = (sueldo * 20) / 100
  nuevo_sueldo = sueldo + aumento
  print("Su sueldo mas el aumento otorgado es de: ", nuevo_sueldo)
elif sueldo < 500 and antiguedad < 10:
  print("¡TIENE UN AUMENTO DEL 5% EN SU SUELDO!")
  aumento = (sueldo * 5) / 100
  nuevo_sueldo = sueldo + aumento
  print("Su sueldo mas el aumento otorgado es de: ", nuevo_sueldo)
elif sueldo >= 500:
  print("¡NO TIENE AUMENTO!")
  print("Su sueldo es de: ", sueldo)
  