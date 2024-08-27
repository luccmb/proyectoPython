base_datos = {}

def registrar_usuario():
    nombre_usuario = input("Ingrese el nombre de usuario: ")
    if nombre_usuario in base_datos:
        print("El nombre de usuario ya existe. Intente con otro.")
        return
    
    contrasena = input("Ingrese la contraseña: ")
    base_datos[nombre_usuario] = contrasena

    print(f"Usuario {nombre_usuario} registrado exitosamente.")

def mostrar_usuarios():
    if not base_datos:
        print("No hay usuarios registrados.")
        return

    print("Usuarios registrados:")
    for usuario in base_datos:
        print(f"Usuario: {usuario}")
    print()

def login_usuario():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if nombre_usuario in base_datos and base_datos[nombre_usuario] == contrasena:
        print(f"Inicio de sesión exitoso. ¡Bienvenido, {nombre_usuario}!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

def menu():
    while True:
        print("1. Registrar nuevo usuario")
        print("2. Mostrar usuarios registrados")
        print("3. Iniciar sesión")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

menu()
