# Nimiguci Skills

Skills personalizadas para o agente Nimiguci (OpenClaw).

## O que são Skills?

Skills são instruções especializadas que extendem as capacidades do agente. Cada skill é uma pasta contendo:

- `SKILL.md` — Documentação e instruções de quando usar
- `scripts/` — Scripts Python/TypeScript auxiliares (opcional)
- `references/` — Referências e templates (opcional)

## Skills Disponíveis

| Skill | Descrição |
|-------|-----------|
| `chart-guides` | Guia para criar gráficos profissionais |
| `cv-job-fit` | Otimiza CV do Hendrix para vagas específicas |
| `exa-mcp` | Busca web avançada via Exa.ai MCP |
| `google-ads` | Consulta dados do Google Ads API |
| `here-now` | Publica arquivos na web instantaneamente |
| `humanizer` | Remove sinais de texto gerado por IA |
| `notion` | Integração com Notion API |
| `powerpoint-pptx` | Cria e edita apresentações PowerPoint |
| `slack` | Controle do Slack via Clawdbot |
| `skill-guard` | Escaneia skills por vulnerabilidades |
| `soul-md-maker` | Criador de personalidades para agentes |
| `tarefas-de-dados` | Gerencia tarefas no Notion |
| `workspace-organizer` | Organiza e mantém estrutura do workspace |

## Instalação

Copie a pasta da skill desejada para `~/.openclaw/workspace/skills/` ou `~/.openclaw/skills/`.

## Configuração de Credenciais

Algumas skills requerem credenciais externas. **Nunca commite credenciais neste repositório.**

Arquivos de credenciais devem ficar em:
- `~/.openclaw/workspace/` (fora da pasta skills)
- `~/.openclaw/workspace/projects/<projeto>/config/`

Exemplos:
- `google-ads-auth.json` → OAuth credentials do Google Ads
- `google-ads-config.json` → Developer token do Google Ads

## Estrutura

```
nimiguci-skills/
├── chart-guides/
│   ├── SKILL.md
│   ├── scripts/
│   └── references/
├── google-ads/
│   ├── SKILL.md
│   └── scripts/
├── ...
└── README.md
```

## Atualizações

Este repositório é atualizado automaticamente pelo agente Nimiguci quando:
- Novas skills são criadas
- Skills existentes são modificadas
- Correções ou melhorias são aplicadas

---

🐦‍⬛ Mantido por Nimiguci
