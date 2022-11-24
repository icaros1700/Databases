import getpass
import sqlite3
import getpass

def main():
    username = input('Nombre de usuario: ')
    password = getpass.getpass('Contraseña: ')

    if verificar_credencial(username, password):
        print('Login Correcto')
    else:
        print('Login Incorrecto')



def verificar_credencial(username, password):
    conn = sqlite3.connect('proyecto.db')
    cursor = conn.cursor()

    rows = cursor.execute(f"SELECT id FROM users WHERE username='{username}' AND password='{password}'")
    rows.fetchone()

    cursor.close()
    conn.close()



if __name__ == '__main__':
    main()


