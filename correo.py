import re 
class CorreoElectronicoInvalido(Exception):
    pass
class CuentaBloqueada(Exception):
    pass
def analizar_correo_electronico(correo):
    if not correo:
        raise CorreoElectronicoInvalido
    elif not re.search(".*@.*\..*",correo):
        raise CorreoElectronicoInvalido("Una direccion de correo electrónico debe tener formato xxx@xxx.com")
    elif correo != "vicente@eni.es":
        raise CuentaBloqueada("Cuenta bloqueada a causa de un ataque")
    else:
        print("Hola Vicente")
def main():
    while True:
        correo = input("->")
        try:
            analizar_correo_electronico(correo)
            break
        except CorreoElectronicoInvalido as e:
            print(e)
        except CuentaBloqueada as e:
            print(e)
            break
if __name__ == "__main__":
    main()