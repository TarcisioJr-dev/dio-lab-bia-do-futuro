import json
import pandas as pd
import requests
import streamlit as st

# ============= CONFIGURAÇÃO ===============
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b-cloud"

# =============== CARREGAR DADOS =================
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =============== Montar Contexto =================
contexto = f"""
CLIENTE: {perfil['nome']},{perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =============== System Prompt ===============
SYSTEM_PROMPT = """Você é um agente financeiro inteligente chamado *MetaFinance* especializado em planejamento de metas financeiras.

OBJETIVO:
Ajudar o usuário a transformar seus sonhos e objetivos em metas concretas, mostrando quanto precisa guardar por mês e acompanhando o progresso.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos (saldo, perfil, resumo de gastos, metas);
2. Nunca invente informações financeiras ou valores que não estejam nos dados;
3. Se não souber algo, admita e ofereça alternativas (ex.: "Sugiro consultar um especialista");
4. Não recomende produtos financeiros específicos (bancos, fundos, ações);
5. Use linguagem acessível e motivadora, sem jargões técnicos.
6. Mostre cálculos de forma transparente (ex.: dividir meta pelo número de meses);
7. Reforce boas práticas (ex.: manter reserva de emergência antes de metas maiores);
8. JAMAIS responda perguntas fora do tema.
"""

# ============== CHAMAR OLLAMA ================
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})

    data = r.json()

    if "response" in data:
        return data["response"]
    # Caso contrário, mostra o erro ou conteúdo recebido
    elif "error" in data:
        return f"Erro do servidor Ollama: {data['error']}"
    else:
        return f"Resposta inesperada: {data}"


# ================== INTERFACE ====================
st.title("🪙MetaFinance, seu auxilio em metas financeiras💰")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))
