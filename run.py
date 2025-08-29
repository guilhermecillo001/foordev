#!/usr/bin/env python3
"""
Script para executar o servidor Foordev com configurações otimizadas
"""

import os
import sys
from app import app

def main():
    print("🚀 Iniciando servidor Foordev...")
    print("=" * 50)
    
    # Configurações
    port = int(os.environ.get('PORT', 5000))
    debug = True  # Habilita debug mode
    
    # Verificar se arquivos existem
    required_files = ['index.html', 'styles.css', 'script.js']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Arquivos não encontrados: {', '.join(missing_files)}")
        print("Certifique-se de que todos os arquivos estão no diretório atual.")
        sys.exit(1)
    
    print("✅ Todos os arquivos encontrados")
    print(f"🌐 Servidor será iniciado em: http://localhost:{port}")
    print(f"🐛 Debug mode: {'Ativado' if debug else 'Desativado'}")
    print("=" * 50)
    
    # Configurar Flask
    app.config.update(
        DEBUG=debug,
        TEMPLATES_AUTO_RELOAD=debug,
        SEND_FILE_MAX_AGE_DEFAULT=0 if debug else 3600  # No cache em debug
    )
    
    try:
        app.run(
            host='0.0.0.0',
            port=port,
            debug=debug,
            use_reloader=debug
        )
    except KeyboardInterrupt:
        print("\n👋 Servidor encerrado pelo usuário")
    except Exception as e:
        print(f"❌ Erro ao iniciar servidor: {e}")

if __name__ == '__main__':
    main()
