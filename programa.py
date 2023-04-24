mayor = lambda x, y: x if x > y else y
resultado = mayor(5, 8)
print(resultado) 

suma = lambda x, y: x + y
resultado = suma(3, 5)
print(resultado) 

division = lambda x, y: x/y
resultado = division(8, 1)
print(resultado)


N=int(input("Digite un valor: "))
def multiplicar_por (N):
  return lambda x: x * N
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)
resultado1 = duplicar(N) 
resultado2 = triplicar(N)  
resultado3 = diez_veces(N)
print(resultado1)
print(resultado2)
print(resultado3)


