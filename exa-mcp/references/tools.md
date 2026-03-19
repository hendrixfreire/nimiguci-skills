# Exa MCP Tools Reference

Complete reference for all Exa MCP tools.

## web_search_exa

Basic web search using Exa's AI-powered search.

**When to use**: General web searches, finding information, exploring topics.

**Parameters**:
- `query` (string, required): Search query
- `num_results` (number, optional): Number of results (default: 10)
- `include_domains` (array, optional): Limit to specific domains
- `exclude_domains` (array, optional): Exclude specific domains

**Example**:
```json
{
  "query": "latest AI breakthroughs 2024",
  "num_results": 5
}
```

## web_search_advanced_exa

Advanced search with more filtering options.

**When to use**: When you need specific date ranges, domain filters, or result types.

**Parameters**:
- `query` (string, required): Search query
- `num_results` (number, optional): Number of results
- `include_domains` (array, optional): Include only these domains
- `exclude_domains` (array, optional): Exclude these domains
- `start_published_date` (string, optional): ISO date (e.g., "2024-01-01")
- `end_published_date` (string, optional): ISO date
- `use_autoprompt` (boolean, optional): Let Exa optimize the query

**Example**:
```json
{
  "query": "machine learning tutorials",
  "num_results": 10,
  "include_domains": ["github.com", "arxiv.org"],
  "start_published_date": "2024-01-01"
}
```

## get_code_context_exa

Find and analyze code from repositories and documentation.

**When to use**: Looking for code examples, understanding implementations, finding libraries.

**Parameters**:
- `query` (string, required): Code-related query
- `num_results` (number, optional): Number of code snippets
- `include_domains` (array, optional): Code hosts (e.g., ["github.com"])

**Example**:
```json
{
  "query": "React useEffect hook example",
  "num_results": 5,
  "include_domains": ["github.com", "stackoverflow.com"]
}
```

## crawling_exa

Crawl and extract content from specific URLs.

**When to use**: Extracting full content from websites, documentation, articles.

**Parameters**:
- `url` (string, required): URL to crawl
- `extract_text` (boolean, optional): Extract main text content
- `extract_metadata` (boolean, optional): Extract page metadata

**Example**:
```json
{
  "url": "https://example.com/article",
  "extract_text": true,
  "extract_metadata": true
}
```

## company_research_exa

Deep research on companies.

**When to use**: Company analysis, competitive research, finding company information.

**Parameters**:
- `company_name` (string, required): Company to research
- `include_news` (boolean, optional): Include recent news
- `include_financials` (boolean, optional): Include financial information
- `depth` (string, optional): "basic", "standard", or "deep"

**Example**:
```json
{
  "company_name": "OpenAI",
  "include_news": true,
  "depth": "deep"
}
```

## people_search_exa

Find information about people.

**When to use**: Researching individuals, finding professional profiles, contact info.

**Parameters**:
- `name` (string, required): Person's name
- `company` (string, optional): Company they work at
- `role` (string, optional): Job title or role
- `include_social` (boolean, optional): Include social media profiles

**Example**:
```json
{
  "name": "Sam Altman",
  "company": "OpenAI",
  "include_social": true
}
```

## deep_researcher_start

Start a comprehensive research task.

**When to use**: Complex research that requires multiple searches and synthesis.

**Parameters**:
- `topic` (string, required): Research topic
- `subtopics` (array, optional): Specific aspects to research
- `depth` (string, optional): "brief", "standard", or "comprehensive"
- `output_format` (string, optional): "summary", "detailed", or "report"

**Example**:
```json
{
  "topic": "Quantum computing applications in cryptography",
  "subtopics": ["post-quantum cryptography", "QKD", "current implementations"],
  "depth": "comprehensive",
  "output_format": "report"
}
```

**Returns**: Research task ID

## deep_researcher_check

Check the status of a deep research task.

**When to use**: Following up on a started deep research task.

**Parameters**:
- `task_id` (string, required): Task ID from deep_researcher_start

**Example**:
```json
{
  "task_id": "task_abc123xyz"
}
```

**Returns**: Current status and results if complete

## Best Practices

1. **Be specific**: Exa works better with specific, detailed queries
2. **Use domain filters**: Narrow results to trusted sources when needed
3. **Date ranges**: Use for time-sensitive information
4. **Combine tools**: Use web_search + crawling for deep analysis
5. **Deep research**: Use for complex topics requiring synthesis

## Rate Limits

Check your Exa.ai dashboard for current rate limits based on your plan.

## Pricing

Exa offers various plans. Check https://exa.ai/pricing for details.
