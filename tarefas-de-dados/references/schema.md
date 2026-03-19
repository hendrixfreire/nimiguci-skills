# Tarefas de Dados — schema operacional

## Database alvo

- Nome: `Tarefas de Dados`
- data_source_id: `a018cdde-9097-4093-a9a0-4e48cb00a2ea`
- database_id: `a9399605-45b8-4741-b749-f6c3f8c472fd`

## Campo de título

- `O que precisa?` — type `title`
- Usar como nome curto e claro da tarefa.

## Campos realmente úteis para criação

### Essenciais
- `O que precisa?` — título da tarefa
- `Status` — status inicial
- `Prioridade` — prioridade inicial

### Fortemente recomendados quando houver informação
- `Data para entrega` — prazo
- `Tipo` — categoria do trabalho
- `Cliente` — cliente relacionado
- `Do que se trata?` — resumo curto em linguagem natural

## Defaults recomendados

Usar estes defaults quando o usuário pedir para criar uma tarefa e não especificar nada melhor:

- `Status`: `Backlog`
- `Prioridade`: `Média`
- `Do que se trata?`: resumo de 1 frase do pedido do usuário

## Campos que não são essenciais no cadastro inicial

Preencher só se o usuário pedir ou fornecer claramente:

- `Responsável`
- `Envolvidos`
- `Nome do/a solicitante`
- `Poderia trazer mais detalhes sobre este pedido?`
- `Contexto adicional`
- `SLA`
- `Tempo estimado (min)`
- `Tempo gasto (min)`
- `Story Points`
- `Complexidade (Fibonacci)`
- `Se houver arquivos para referência, inclua aqui por favor.`

## Valores válidos úteis

### Status
- `Backlog`
- `Falta briefing`
- `Em progresso`
- `Bloqueado`
- `Em revisão`
- `Concluído`
- `Cancelado`

### Prioridade
- `Crítica`
- `Alta`
- `Média`
- `Baixa`

### Tipo
- `Admin/Infra`
- `Análise`
- `Dashboard`
- `E-mail`
- `Modelagem`
- `Newsletter`
- `PDI`
- `Proposta`
- `Qualidade de dados`
- `Relatório`

## Heurísticas de mapeamento

- Se o usuário disser só “adiciona uma tarefa”, assumir esta database.
- Se o pedido vier sem prazo, não inventar `Data para entrega`.
- Se o pedido vier sem cliente, não inventar `Cliente`.
- Se o tipo for claro pelo texto, preencher `Tipo`; se não for, deixar vazio.
- Gerar `Do que se trata?` como resumo curto, sem floreio.
- Não preencher campos de estimativa/complexidade sem sinal claro do usuário.

## Heurísticas simples para `Tipo`

- Dashboard, gráfico, looker, datastudio, painel → `Dashboard`
- Analisar, investigar, levantar, validar resultado → `Análise`
- Modelar tabela, estruturar base, schema, transformação → `Modelagem`
- Corrigir métrica, inconsistência, qualidade, duplicidade → `Qualidade de dados`
- Relatório, report, fechamento, consolidado → `Relatório`
- Infra, acesso, credencial, automação interna, configuração → `Admin/Infra`

## Padrão de criação recomendado

Criar novas tarefas com no máximo estes campos por padrão:

1. `O que precisa?`
2. `Status`
3. `Prioridade`
4. `Do que se trata?`
5. `Data para entrega` (se houver)
6. `Tipo` (se inferível com segurança)
7. `Cliente` (se explícito)

Isso mantém o cadastro leve e evita poluir a base com chute fantasiado de dado.
