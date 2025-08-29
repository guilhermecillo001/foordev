# Foordev - Site em HTML, CSS e Python

Site moderno e futurista da Foordev desenvolvido com HTML5, CSS3 e Python (Flask).

## 🚀 Tecnologias Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask
- **Ícones:** Lucide Icons
- **Cores:** Azul marinho escuro e cinza prateado futurístico

## 📁 Estrutura do Projeto

```
foordev-website/
├── index.html          # Página principal HTML
├── styles.css          # Estilos CSS com tema futurístico
├── script.js           # JavaScript para interatividade
├── app.py              # Backend Python/Flask
├── requirements.txt    # Dependências Python
└── README.md          # Este arquivo
```

## 🛠️ Como Executar

### 1. Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalação

```bash
# Clone ou baixe os arquivos do projeto
cd foordev-website

# Instale as dependências Python
pip install -r requirements.txt
```

### 3. Configuração

Defina as variáveis de ambiente (opcional):

```bash
export FLASK_ENV=development
export SECRET_KEY=sua-chave-secreta-aqui
```

### 4. Executar o Servidor

```bash
# Opção 1: Usando o script otimizado (recomendado)
python run.py

# Opção 2: Diretamente com Flask
python app.py
```

O site estará disponível em: `http://localhost:5000`

### 5. Teste se está funcionando

```bash
# Executar teste automatizado
python test_server.py
```

## 🔧 Troubleshooting

### Problema: Site sem design/CSS não carrega

**Sintomas:** O HTML aparece mas sem estilo visual

**Soluções:**
1. **Forçar reload:** Pressione `Ctrl+F5` no navegador
2. **Verificar arquivos:** Execute `python test_server.py`
3. **Verificar console:** Abra F12 no navegador e veja se há erros
4. **Limpar cache:** Abra DevTools > Network > Disable cache

### Problema: Ícones não aparecem

**Sintomas:** Espaços vazios onde deveriam ter ícones

**Soluções:**
1. Verificar conexão com internet (Lucide Icons é CDN)
2. Aguardar alguns segundos para carregar
3. Verificar console do navegador para erros

### Problema: WhatsApp não funciona

**Sintomas:** Botão não abre WhatsApp

**Soluções:**
1. Verificar se o número está correto em `app.py` e `script.js`
2. Preencher todos os campos do formulário
3. Verificar se WhatsApp está instalado no dispositivo

### Verificar se CSS está carregando

Se você ver uma mensagem verde "CSS Carregado com sucesso!" no canto superior direito por alguns segundos, o CSS está funcionando.

## 🌐 Funcionalidades

### Frontend (HTML/CSS/JS)
- ✅ Design responsivo e moderno
- ✅ Tema azul marinho e cinza prateado
- ✅ Animações CSS futurísticas
- ✅ Menu mobile responsivo
- ✅ Scroll suave entre seções
- ✅ Formulário de contato integrado com WhatsApp
- ✅ Seções: Hero, Sobre, Serviços, Projetos, Contato, Footer

### Backend (Python/Flask)
- ✅ API RESTful para formulários
- ✅ Integração com WhatsApp
- ✅ Endpoints para serviços e projetos
- ✅ Tratamento de erros
- ✅ Logs de sistema
- ✅ CORS habilitado

## 📱 Integração WhatsApp

O formulário de contato envia mensagens diretamente para o WhatsApp:
- Número configurado: `+55 (11) 92007-5704`
- Formato automático da mensagem
- Abertura em nova aba

## 🎨 Tema Visual

### Cores Principais
- **Background:** `hsl(210, 100%, 4%)` - Azul marinho escuro
- **Primary:** `hsl(215, 100%, 50%)` - Azul vibrante
- **Silver:** `hsl(0, 0%, 75%)` - Cinza prateado
- **Metallic:** `hsl(210, 8%, 50%)` - Cinza metálico

### Animações
- Elementos flutuantes no hero
- Fade-in ao rolar a página
- Hover effects nos cards
- Gradientes dinâmicos
- Parallax sutil

## 🔧 API Endpoints

### GET /
- Retorna a página HTML principal

### POST /api/contact
- Processa formulário de contato
- Body: `{ "name": "Nome", "email": "email@example.com", "message": "Mensagem" }`
- Retorna: URL do WhatsApp formatada

### GET /api/services
- Lista dos serviços disponíveis
- Retorna: Array com serviços, tecnologias e preços

### GET /api/projects
- Portfolio de projetos realizados
- Retorna: Array com projetos e detalhes

### GET /api/health
- Health check do servidor
- Retorna: Status e timestamp

## 🚀 Deploy

### Localhost
```bash
python app.py
```

### Produção com Gunicorn
```bash
gunicorn --bind 0.0.0.0:5000 app:app
```

### Docker (opcional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

## 📝 Personalização

### Alterar Número do WhatsApp
No arquivo `app.py`, linha 15:
```python
WHATSAPP_NUMBER = "5511920075704"  # Seu número aqui
```

No arquivo `script.js`, linha 49:
```javascript
const whatsappNumber = "5511920075704";  // Seu número aqui
```

### Alterar Cores
No arquivo `styles.css`, seção `:root` (linhas 11-30):
```css
:root {
  --primary: hsl(215, 100%, 50%);  /* Cor principal */
  --silver: hsl(0, 0%, 75%);       /* Cinza prateado */
  /* ... outras cores */
}
```

### Adicionar Novos Serviços
No arquivo `app.py`, função `services()` (linha 91):
```python
services_data.append({
    'id': 'novo-servico',
    'name': 'Novo Serviço',
    'description': 'Descrição do serviço',
    'technologies': ['HTML', 'CSS', 'Python'],
    'price_range': 'R$ 500 - R$ 2000'
})
```

## 🔒 Segurança

- CORS configurado
- Validação de dados de entrada
- Logs de segurança
- Tratamento de erros
- Rate limiting (recomendado para produção)

## 📞 Contato

- **WhatsApp:** +55 (11) 92007-5704
- **Site:** Foordev - Desenvolvimento Web

---

**Desenvolvido com HTML5, CSS3 e Python/Flask** 🐍✨
