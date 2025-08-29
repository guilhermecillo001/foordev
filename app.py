#!/usr/bin/env python3
"""
Foordev Website - Flask Backend Simples
"""

from flask import Flask, request, jsonify
import os
import logging
from datetime import datetime
import urllib.parse

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration
WHATSAPP_NUMBER = "5511920075704"

@app.route('/')
def index():
    """Serve the main HTML page with inline CSS"""
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Site da Foordev</h1><p>Arquivo index.html não encontrado.</p>", 500

@app.route('/api/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({
                    'success': False,
                    'error': f'Campo {field} é obrigatório'
                }), 400
        
        name = data['name'].strip()
        email = data['email'].strip()
        message = data['message'].strip()
        
        # Log the contact attempt
        logger.info(f"Nova mensagem de contato: {name} ({email})")
        
        # Create WhatsApp message
        whatsapp_message = f"""*Nova solicitação do site Foordev*

*Nome:* {name}
*E-mail:* {email}
*Mensagem:* {message}

*Data:* {datetime.now().strftime('%d/%m/%Y às %H:%M')}"""
        
        # Generate WhatsApp URL
        encoded_message = urllib.parse.quote(whatsapp_message)
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={encoded_message}"
        
        return jsonify({
            'success': True,
            'message': 'Mensagem enviada com sucesso!',
            'whatsapp_url': whatsapp_url
        })
        
    except Exception as e:
        logger.error(f"Erro ao processar contato: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Erro interno do servidor'
        }), 500

@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return "<h1>404 - Página não encontrada</h1><p><a href='/'>Voltar para o início</a></p>", 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    logger.error(f"Erro interno: {str(error)}")
    return "<h1>500 - Erro interno</h1><p>Algo deu errado. Tente novamente.</p>", 500

if __name__ == '__main__':
    # Development server
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    print("=" * 60)
    print("🚀 FOORDEV WEBSITE")
    print("=" * 60)
    print(f"🌐 Servidor: http://localhost:{port}")
    print(f"📱 WhatsApp: +55 (11) 92007-5704")
    print(f"🐛 Debug: {'Ativado' if debug else 'Desativado'}")
    print("=" * 60)
    
    # Check if HTML file exists
    if not os.path.exists('index.html'):
        print("❌ ERRO: index.html não encontrado!")
        print("Certifique-se de que o arquivo está no diretório atual.")
        exit(1)
    
    print("✅ Arquivos encontrados")
    print("🎨 CSS incluído inline no HTML")
    print("📱 JavaScript incluído inline no HTML")
    print("=" * 60)
    
    try:
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug
        )
    except KeyboardInterrupt:
        print("\n👋 Servidor encerrado")
    except Exception as e:
        print(f"❌ Erro: {e}")
