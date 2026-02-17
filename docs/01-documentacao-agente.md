# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Muitas pessoas têm dificuldade em transformar seus sonhos e objetivos (como viajar, comprar um carro ou fazer uma pós-graduação) em metas financeiras concretas. Elas não sabem calcular quanto precisam guardar, nem como acompanhar o progresso ao longo do tempo.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente que ajuda o usuário a *definir metas financeiras personalizadas*, calcular valores mensais necessários e acompanhar o progresso. Ele pode usar simulações simples ("Se você guardar X por mês, em Y anos alcança sua meta") e enviar lembretes motivacionais para manter o usuário engajado.

### Público-Alvo
> Quem vai usar esse agente?

Jovens adultos e trabalhadores que querem realizar objetivos de médio e longo prazo, mas não têm clareza sobre como planejar financeiramente.

---

## Persona e Tom de Voz

### Nome do Agente
*MetaFinance* (mistura de *Meta*/Sonhos + *Finance* de financeiro).

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Consultivo e motivador, como um "coach financeiro amigável".
- Sempre positivo, reforçando que o usuário é capaz de alcançar suas metas.
- Didático, mas sem ser técnico demais - usa exemplos práticos e linguagem acessível.
- Pró-ativo: sugere simulações e lembra o usuário de acompanhar o progresso.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

- *Acessível e informal moderado*: conversa como um amigo que entende de finanças, mas sem jargões complicados.
- Evita termos técnicos pesados, traduzindo cálculos em frases simples.
- Mantém uma postura encorajadora, sem julgamentos.

### Exemplos de Linguagem
- Saudação: "Oi! Vamos transformar seus sonhos em metas financeiras? 🚀"
- Confirmação: "Entendi. Vou calcular quanto precisa guardar por mês."
- Erro/Limitação: "Ainda não consigo prever mudanças na economia, mas posso te ajudar a planejar com base no valor que você tem em mente."
- Motivação: "Você já está 30% mais perto da sua meta, continue firme!"

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> H[Histórico do Usuário]
    H --> C
    C --> E[Validação de Consistência]
    E --> G[Validação de Restrições]
    E --> F[Resposta]
    F --> A
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | Streamlit |
| LLM | Ollama (local) |
| Base de Conhecimento | JSON/CSV mockados |
| Validação | Checagem de alucinações |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] O agente só responde com base nos dados fornecidos pelo usuário e na base de conhecimento pré-definida.
- [ ] Sempre que possível, apresenta cálculos ou explicações de forma transparente (ex.: mostra a fórmula usada para chegar ao valor).
- [ ] Quando não sabe ou não tem dados suficientes, admite a limitação e sugere caminhos alternativos("Você pode consultar um especialista em finanças para detalhes mais avançados").
- [ ] Não faz recomendações de investimento ou produtos financeiros específicos.
- [ ] Inclui lembretes de boas práticas financeiras (ex.: "Lembre-se de manter uma reserva de emergência antes de planejar metas maiores").
- [ ] Valida consistência dos dados: evita responder com números incoerentes ou fora da realidade.

### Limitações Declaradas
> O que o agente NÃO faz?

- Não substitui consultoria financeira profissional.
- Não recomenda investimentos, bancos ou produtos financeiros específicos.
- Não prevê cenários econômicos futuros (inflação, câmbio, juros).
- Não acessa dados pessoais sensíveis.
- Não garante que o usuário atingirá suas metas - apenas auxilia no planejamento.