# Passo a Passo de Execução

Esta pasta contém o código do seu agente financeiro.

## Setup do Ollama

```
#1. Instalar Ollama (ollama.com)
#2. Baixar um modelo leve
ollama pull gpt-oss

#3. Testar se funciona
ollama run gpt-oss "Olá!"
```

## Código completo

Todo o código fonte está no arquivo `app.py`.

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
streamlit run ./src/app.py
```
