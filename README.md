# 🚀 Projeto 4 - CI/CD Avançado com Testes e Qualidade de Código

![CI Pipeline](https://github.com/SEU_USUARIO/ci-cd-project4/actions/workflows/ci.yaml/badge.svg)

## 📘 Descrição

Este é o **quarto projeto** da minha jornada de estudos em **DevOps**, focado em práticas avançadas de CI/CD. O projeto implementa um pipeline completo com:

- ✅ **Linting** automático (qualidade de código)
- ✅ **Testes unitários** com cobertura de código
- ✅ **Testes de integração** com containers Docker
- ✅ **Estrutura profissional** de projeto Python
- ✅ **Reports automáticos** (JUnit XML e Coverage)

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

1. **Separação de testes** (unit vs integration)
2. **Code coverage** com pytest-cov
3. **Linting** com flake8 (PEP 8)
4. **Testes de integração** com Docker em pipelines CI
5. **Estrutura modular** de aplicações Python
6. **Artifacts** no GitHub Actions

---

## 🧩 Tecnologias Utilizadas

### Backend
- **Python 3.10**
- **Flask 3.0.3** - Framework web
- **Gunicorn 21.2.0** - Servidor WSGI de produção

### Testes
- **Pytest 8.2.2** - Framework de testes
- **Pytest-cov 4.1.0** - Cobertura de código
- **Flake8 6.1.0** - Linter (qualidade de código)

### DevOps
- **Docker** - Containerização
- **GitHub Actions** - Pipeline CI/CD

---

## 📁 Estrutura do Projeto

```
ci-cd-project4/
├── .github/
│   └── workflows/
│       └── ci.yaml              # Pipeline CI/CD
├── app/
│   ├── __init__.py
│   └── app.py                   # Aplicação Flask
├── tests/
│   ├── unit/
│   │   └── test_app_unit.py     # Testes unitários
│   └── integration/
│       └── test_app_integration.py  # Testes de integração
├── Dockerfile                   # Containerização
├── requirements.txt             # Dependências Python
└── pytest.ini                   # Configuração do Pytest
```

---

## ⚙️ Pipeline CI/CD

O pipeline é executado automaticamente em **push** ou **pull request** na branch `main` e possui 3 jobs:

### 1️⃣ **Lint** (Qualidade de Código)
- Valida o código contra PEP 8
- Garante padrões de formatação
- Bloqueia merge se houver erros

### 2️⃣ **Unit Tests** (Testes Unitários)
- Executa testes isolados das funções
- Gera relatório de cobertura de código
- Upload de artifacts (JUnit XML + Coverage)

### 3️⃣ **Integration Tests** (Testes de Integração)
- Constrói imagem Docker da aplicação
- Sobe container e valida endpoints
- Executa testes end-to-end
- Upload de relatórios de integração

---

## 🧪 Testes

### Testes Unitários
Testam funções isoladamente, sem dependências externas:

```python
def test_home():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
```

### Testes de Integração
Testam o sistema completo rodando em container:

```python
def test_integration_echo():
    client = app.test_client()
    payload = {"x": 123}
    resp = client.post("/echo", json=payload)
    assert resp.status_code == 200
```

---

## 🐋 Docker

### Construir a imagem
```bash
docker build -t ci-cd-project4:latest .
```

### Executar o container
```bash
docker run -d -p 5000:5000 --name flask-app ci-cd-project4:latest
```

### Testar localmente
```bash
curl http://localhost:5000/
# Output: Aplicação Flask
```

---

## 🚀 Como Executar Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/SEU_USUARIO/ci-cd-project4.git
cd ci-cd-project4
```

### 2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute os testes
```bash
# Testes unitários
pytest tests/unit -v

# Testes de integração
pytest tests/integration -v

# Com cobertura
pytest --cov=app --cov-report=html
```

### 5. Execute a aplicação
```bash
# Modo desenvolvimento
python app/app.py

# Modo produção
gunicorn --bind 0.0.0.0:5000 app.app:app
```

---

## 📊 Endpoints da API

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET    | `/`      | Retorna mensagem de boas-vindas |
| POST   | `/echo`  | Retorna o JSON enviado |
| GET    | `/slow`  | Endpoint com delay (teste de performance) |

### Exemplos de uso

```bash
# GET /
curl http://localhost:5000/
# Output: Aplicação Flask

# POST /echo
curl -X POST http://localhost:5000/echo \
  -H "Content-Type: application/json" \
  -d '{"msg": "hello"}'
# Output: {"you_sent": {"msg": "hello"}}
```

---

## 📈 Evolução dos Projetos

| Projeto | Conceitos Aprendidos |
|---------|---------------------|
| **Projeto 1** | CI básico, GitHub Actions, Pytest |
| **Projeto 2** | Docker, Containerização |
| **Projeto 3** | Deploy automático (Render), Gunicorn |
| **Projeto 4** | Linting, Testes separados, Coverage, Integração com Docker no CI |

---

## 🎓 Aprendizados Principais

### ✅ Conceitos DevOps
- Separação de responsabilidades (unit vs integration)
- Pipeline multi-stage com dependências
- Artifacts e relatórios automatizados
- Health checks em containers

### ✅ Boas Práticas Python
- Estrutura modular de projetos
- Cobertura de código > 80%
- Conformidade com PEP 8
- Testes isolados e reproduzíveis

### ✅ Docker em CI/CD
- Build de imagens no pipeline
- Testes em containers efêmeros
- Cleanup automático de recursos
- Debug de containers no GitHub Actions

