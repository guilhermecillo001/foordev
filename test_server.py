#!/usr/bin/env python3
"""
Script simples para testar se o servidor está funcionando
"""

import requests
import sys

def test_server(base_url="http://localhost:5000"):
    print(f"🧪 Testando servidor em {base_url}")
    
    # Teste 1: Página principal
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code == 200:
            print("✅ Página principal carregando")
        else:
            print(f"❌ Erro na página principal: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao conectar com servidor: {e}")
        print("🚨 Certifique-se de que o servidor está rodando: python app.py")
        return
    
    # Teste 2: CSS
    try:
        response = requests.get(f"{base_url}/styles.css")
        if response.status_code == 200 and 'text/css' in response.headers.get('Content-Type', ''):
            print("✅ CSS carregando corretamente")
        else:
            print(f"❌ Erro no CSS: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao carregar CSS: {e}")
    
    # Teste 3: JavaScript
    try:
        response = requests.get(f"{base_url}/script.js")
        if response.status_code == 200 and 'javascript' in response.headers.get('Content-Type', ''):
            print("✅ JavaScript carregando corretamente")
        else:
            print(f"❌ Erro no JavaScript: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro ao carregar JavaScript: {e}")
    
    # Teste 4: API Health
    try:
        response = requests.get(f"{base_url}/api/health")
        if response.status_code == 200:
            print("✅ API funcionando")
        else:
            print(f"❌ Erro na API: {response.status_code}")
    except Exception as e:
        print(f"❌ Erro na API: {e}")
    
    print(f"\n🌐 Acesse o site em: {base_url}")
    print("📱 Use Ctrl+F5 para forçar reload se necessário")

if __name__ == "__main__":
    test_server()
