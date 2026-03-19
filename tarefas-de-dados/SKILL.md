---
name: tarefas-de-dados
description: Criar, consultar e atualizar tarefas na database do Notion "Tarefas de Dados". Use quando Hendrix pedir para criar tarefa, listar tarefas, alterar status, editar prazo, mudar responsável, definir prioridade ou consultar backlog/andamento. Esta skill usa a base "Tarefas de Dados" como padrão, assume `Responsável = Hendrix Freire` por default e filtra consultas pelo mesmo responsável, salvo instrução explícita em contrário.
---

# tarefas-de-dados

Usar esta skill como padrão sempre que Hendrix falar de tarefas, a menos que ele cite outra base.

## Regras centrais

- Usar a database `Tarefas de Dados` como padrão.
- Em criação, assumir `Responsável = Hendrix Freire`, salvo se Hendrix pedir outra pessoa.
- Em consultas e listagens, filtrar por `Responsável = Hendrix Freire`, salvo se Hendrix pedir outro escopo.
- Se faltar `Cliente` ao criar tarefa, perguntar antes de criar.
- Nunca inventar cliente, prazo, tipo, responsável, envolvidos, estimativas ou contexto adicional.
- Em atualizações, alterar apenas os campos pedidos.
- Se houver ambiguidade sobre qual tarefa atualizar, perguntar.

## Criação de tarefa

Preencher por padrão apenas:

- `O que precisa?`
- `Status`
- `Prioridade`
- `Responsável`
- `Do que se trata?`
- `Data para entrega` (se houver)
- `Tipo` (só se Hendrix disser)
- `Cliente` (obrigatório perguntar se faltar)

### Defaults

Se Hendrix não especificar:

- `Responsável` → `Hendrix Freire`
- `Status` → `Backlog`
- `Prioridade` → `Média`
- `Do que se trata?` → resumo curto do pedido
- `Tipo` → deixar em branco

## Atualização de tarefa

- Alterar só os campos explicitamente pedidos.
- Se Hendrix passar URL do Notion ou page ID, usar isso como prioridade.
- Se vier só o nome:
  1. tentar nome exato
  2. se houver múltiplas correspondências, perguntar
  3. só usar aproximação com confirmação humana

## Consultas e listagens

Suportar pedidos como:

- “lista minhas tarefas em progresso”
- “quais estão atrasadas?”
- “me mostra meu backlog”
- “quais estão bloqueadas?”

## Campos que não devem ser preenchidos por padrão

Não preencher salvo instrução explícita:

- `Envolvidos`
- `Nome do/a solicitante`
- `Poderia trazer mais detalhes sobre este pedido?`
- `Contexto adicional`
- `SLA`
- `Tempo estimado (min)`
- `Tempo gasto (min)`
- `Story Points`
- `Complexidade (Fibonacci)`

## Confirmação

Responder com mini resumo curto, claro e legível.

Exemplo:

- Tarefa criada
- Responsável: Hendrix Freire
- Status: Em progresso
- Cliente: Boticário

## Referência

Consultar `references/schema.md` quando precisar confirmar campos ou valores válidos.
