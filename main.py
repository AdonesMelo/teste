from dotenv import load_dotenv
import os

load_dotenv()

usuario = os.getenv('USUARIO')
senha = os.getenv('SENHA')

print(usuario, senha)