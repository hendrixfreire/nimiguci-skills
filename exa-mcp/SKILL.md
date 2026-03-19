---
name: exa-mcp
description: Use the Exa.ai MCP (Model Context Protocol) server for advanced web search, research, and data extraction. Use when the user needs to search the web, crawl websites, research companies, find people, or perform deep research tasks. Provides tools for web_search_exa, web_search_advanced_exa, company_research_exa, people_search_exa, crawling_exa, get_code_context_exa, and deep research capabilities.
---

# Exa MCP Skill

Access Exa.ai's powerful search and research capabilities through the Model Context Protocol (MCP).

## What is Exa?

Exa is an AI-powered search engine that finds specific, high-quality information on the web. Unlike traditional search, Exa uses embeddings to understand meaning and context.

## Available Tools

| Tool | Purpose |
|------|---------|
| `web_search_exa` | Basic web search with AI understanding |
| `web_search_advanced_exa` | Advanced search with filters and options |
| `get_code_context_exa` | Find and analyze code from repositories |
| `crawling_exa` | Crawl and extract content from websites |
| `company_research_exa` | Deep research on companies |
| `people_search_exa` | Find information about people |
| `deep_researcher_start` | Start a comprehensive research task |
| `deep_researcher_check` | Check status of deep research |

## Setup

### Prerequisites

1. **Exa API Key**: Get one at https://exa.ai
2. **MCP Client**: This skill works with OpenClaw's mcporter or any MCP client

### Configuration

Add to your MCP config:

```json
{
  "mcpServers": {
    "exa": {
      "command": "npx",
      "args": ["-y", "@exa-ai/mcp"],
      "env": {
        "EXA_API_KEY": "your-api-key-here"
      }
    }
  }
}
```

Or use the server directly:
```
https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,crawling_exa,company_research_exa,people_search_exa,deep_researcher_start,deep_researcher_check
```

## Usage Examples

### Web Search
```
Search for recent AI breakthroughs using Exa
```

### Company Research
```
Research the company OpenAI using Exa company research
```

### Code Context
```
Find code examples for React hooks using Exa
```

### Deep Research
```
Start a deep research on quantum computing applications
```

## Tool Details

See [references/tools.md](references/tools.md) for detailed parameter documentation.

## Tips

- Use `web_search_advanced_exa` for more control over results
- `deep_researcher_start` is great for comprehensive topics
- Combine `crawling_exa` with `get_code_context_exa` for technical research
- Company and people search work best with specific, named entities
