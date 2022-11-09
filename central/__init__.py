from flask import Flask # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'   