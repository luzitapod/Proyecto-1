def saludo(nombre: str) ->str:
    return f"hola, {nombre}! Bienvenido a Git, guapo"

if __name__ == "__main__":
    nombre = input("¿Tu nombre? ")
    print(saludo(nombre))
    print("Agregado")
