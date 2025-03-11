from flask import Flask, render_template, request, jsonify
from bot_simple import WhatsAppBot
import os

app = Flask(__name__)
bot = WhatsAppBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.json
    message = data.get('message', '')
    user_id = data.get('user_id', 'web_user')
    
    response = bot.procesar_mensaje(message, user_id)
    return jsonify({'response': response})

@app.route('/dashboard')
def dashboard():
    # Obtener estadísticas del bot
    stats = bot.obtener_estadisticas()
    return render_template('dashboard.html', stats=stats)

@app.route('/estadisticas')
def estadisticas():
    # Obtener estadísticas del bot
    stats = bot.obtener_estadisticas()
    return render_template('estadisticas.html', stats=stats)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)