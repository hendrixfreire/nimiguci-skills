---
name: newsletter-digest
description: Resume newsletters não lidas do INBOX do Gmail, classifica por relevância e ordena da mais interessante para a menos interessante. Usa emoji para indicar nível de interesse.
version: 1.0.0
author: Hermes Agent
tags: [gmail, newsletter, digest, email]
---

# Newsletter Digest

Resumo classificado de newsletters não lidas no INBOX do Gmail.

## Quando usar
- Usuário pede resumo de newsletters ou e-mails de newsletter
- Cron job de digest matinal

## Passos

### 1. Buscar newsletters não lidas
O usuário tem um label `newsletter` (Label_668416921152826066) que o Gmail aplica automaticamente em newsletters detectadas. Combinar com as categorias para não perder nenhuma:
```bash
python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail search "is:unread (label:newsletter OR category:updates OR category:promotions)" --max 50
```
Priorizar e-mails com `label:newsletter` (mais preciso). Os de `category:updates`/`category:promotions` servem como fallback para newsletters que o Gmail não rotulou automaticamente.

### 2. Extrair conteúdo completo
Para cada newsletter identificada, buscar o corpo do e-mail:
```bash
python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py gmail get <message_id>
```
Extrair texto limpo do HTML (remover CSS, scripts, tags, URLs longas).

### 3. Classificar e ordenar
Classificar cada newsletter com base no conteúdo (não no título):

- ⭐⭐⭐ — LEIA PRIMEIRO: conteúdo prático, insights acionáveis, relevante para o trabalho/interesses do usuário
- ⭐⭐ — Vale a pena: informação de mercado, tendências, conteúdo interessante mas não urgente
- ⭐ — Útil se tiver tempo: dicas práticas, updates de ferramentas
- ❌ — Pode ignorar: promoções puras, conteúdo irrelevante, marketing

Ordenar do mais interessante (⭐⭐⭐) para o menos interessante (❌).

### 4. Formatar resumo
Para cada newsletter, incluir:
- Classificação com emoji
- Nome da newsletter + assunto + data
- Resumo em 2-4 sentenças do conteúdo real (não do título)
- Máximo de 15 sentenças no total

### 5. Formato de entrega
```
📰 Newsletter Digest — [data]

1. ⭐⭐⭐ [Newsletter] — [Assunto] ([data])
   [Resumo do conteúdo]

2. ⭐⭐ [Newsletter] — [Assunto] ([data])
   [Resumo do conteúdo]

...

Resumo: X newsletters. Top recomendação: [nome].
```

## Dependências
- Skill `google-workspace` instalada e configurada
- Scripts em `~/.hermes/skills/productivity/google-workspace/scripts/`

## Observações
- Se não houver newsletters não lidas, informar: "Nenhuma newsletter não lida no momento."
- Se o conteúdo vier como HTML bruto, extrair texto antes de resumir
- Considerar apenas newsletters do INBOX (não spam, trash, etc.)
