# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Permite contextualizar interações anteriores, garantindo continuidade e personalização no atendimento. |
| `perfil_investidor.json` | JSON | Usado apenas para ilustrar perfis financeiros, mas se recomendações de investimento. Serve para adaptar a linguagem e exemplo ao perfil do usuário. |
| `produtos_financeiros.json` | JSON | Reaproveitando como catálogo genérico de categorias (ex.: poupança, reserva, metas de curto/médio prazo), sem indicar produtos específicos. |
| `transacoes.csv` | CSV | Analisa padrões de gastos do cliente, ajudando a sugerir valores realistas para metas mensais. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

- Os dados não foram alterados dos originais.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

- Os arquivos *CSV e JSON* são carregados no início da sessão.
- Eles são pré-processados para garantir consistência (ex.: anonimização de dados pessoais e padronização de campos).
- O agente mantém esses dados em memória de contexto, permitindo consultas rápidas durante a interação.
- O `historico_atendimento.csv` e `transacoes.csv` são usados como tabelas de referência, enquando os JSON (`perfil_investidor.json` e `produtos_financeiros.json`) funcionam como catálogos estruturados.

```Python
import pandas as pd
import json

historico = pd.read_csv("historico_atendimento.csv")
transacoes = pd.read_csv("transacoes.csv")

with open("perfil_investidor.json", "r", encoding="utf-8") as f:
    perfil_investidor = json.load(f)

with open("produtos_financeiros.json", "r", encoding="utf-8") as f:
    produtos_financeiros = json.load(f)

# Pré-processamento simples

historico.fillna("", inplace=True) #tratar valores nulos

transaceos["valor"] = transacoes["valor"].astype(float) #garantir tipo numérico.

print("Dados carregados com sucesso!")
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

- Os dados *não ficam todos no system prompt* (para evitar excesso de informação).
- O agente consulta dinamicamente apenas os trechos relevantes conforme a necessidade da conversa.
- Exemplo:
    - Se o usuário fala sobre uma meta de viagem, o agente consulta o `transacoes.csv` para verificar padrão de gastos e sugerir um valor mensal realista.
    - Se o usuário já interagiu antes, o `historico_atendimento.csv` é usado para recuperar contexto e dar continuidade.
    - O `perfil_investidor.json` serve apenas para ajustar o tom da explicação (ex.: linguagem mais conservadora ou mais ousada), sem recomendar produtos.
- As informações são *injetadas no prompt como contexto adicional, garantindo que a resposta seja personalizada, mas sempre validada para evitar alucinações.

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Resumo de gastos (mensal):
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 320,00
- Lazer: R$ 250,00
- Educação: R$ 400
- Saúde: R$ 280,00
- Outros: R$ 150,00

Metas Financeiras:
- Viagem Internacional: R$ 12.000,00 em 24 meses
- Reserva de Emergência: R$ 10.000,00 em 18 meses
- Curso de Pós-Graduação: R$ 8.000,00 em 12 meses

Histórico de Atendimento:
- Última interação: 10/11
- Pergunta anterior: "Quanto preciso guardar por mês para minha viagem?"
- Status: Meta em andamento
```
