---
name: skill-sync
description: >
  Sincroniza skills do Nimiguci com o repositório GitHub. Use quando o usuário
  pedir para "sincronizar skills", "fazer backup das skills", "commitar skills",
  "atualizar o repo de skills", ou quando quiser garantir que as skills estão
  salvas no GitHub.
---

# Skill Sync

Sincroniza as skills do Nimiguci com o repositório GitHub `hendrixfreire/nimiguci-skills`.

## Quando usar

- Usuário pede para sincronizar/backup/commitar skills
- Após criar ou modificar uma skill
- Quando quiser garantir que skills estão salvas no GitHub
- Antes de operações destrutivas no workspace

## Como funciona

1. Verifica mudanças nas skills desde o último sync
2. Copia skills atualizadas para o repositório local
3. Remove arquivos de metadados locais (`.clawhub/`, `_meta.json`)
4. Verifica se há credenciais (bloqueia se encontrar)
5. Commita com mensagem descritiva
6. Push para o GitHub
7. Reporta o que mudou

## Script

```bash
./scripts/sync.sh
```

## Segurança

- NUNCA commita arquivos de credenciais (`*-auth.json`, `*-token.json`, `*secret*`)
- Arquivos bloqueados pelo `.gitignore` não são commitados
- Verificação automática de tokens/keys antes do commit

## Repositório

https://github.com/hendrixfreire/nimiguci-skills

## Estado

O arquivo `~/.openclaw/.skill-sync-state.json` mantém o estado do último sync para evitar commits desnecessários.
