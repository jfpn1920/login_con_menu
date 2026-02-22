usuarios = {
    "admin": "1234",
    "usuario1": "abcd"
}
print("#--------------------------------#")
print("#--| sistema de login con menu|--#")
print("#--------------------------------#")
while True:
    username = input("ingrese su usuario: ").strip()
    password = input("ingrese su contraseña: ").strip()
    if username in usuarios and usuarios[username] == password:
        print(f"\n¡bienvenido {username}!\n")
        while True:
            print("#------------------------#")
            print("#--| menu de opciones |--#")
            print("#------------------------#")
            print("1. ver perfil")
            print("2. cambiar contraseña")
            print("3. cerrar sesión")
            opcion = input("seleccione una opcion: ").strip()
            if opcion == "1":
                print(f"perfil de usuario: {username}")
            elif opcion == "2":
                nueva = input("ingrese nueva contraseña: ").strip()
                usuarios[username] = nueva
                print("contraseña actualizada correctamente.")
            elif opcion == "3":
                print("cerrando sesión...\n")
                break
            else:
                print("opcion invalida, intente nuevamente.")
    else:
        print("usuario o contraseña incorrectos, intente de nuevo.\n")