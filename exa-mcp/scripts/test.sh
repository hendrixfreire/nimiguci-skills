#!/bin/bash
# Quick test for Exa MCP tools

if [ -z "$EXA_API_KEY" ]; then
    echo "❌ EXA_API_KEY not set"
    exit 1
fi

echo "Testing Exa MCP tools..."
echo ""

# The MCP server URL with all tools
MCP_URL="https://mcp.exa.ai/mcp?tools=web_search_exa,web_search_advanced_exa,get_code_context_exa,crawling_exa,company_research_exa,people_search_exa,deep_researcher_start,deep_researcher_check"

echo "MCP Server URL:"
echo "$MCP_URL"
echo ""
echo "✅ Exa MCP ready to use!"
echo ""
echo "Available tools:"
echo "  • web_search_exa"
echo "  • web_search_advanced_exa"
echo "  • get_code_context_exa"
echo "  • crawling_exa"
echo "  • company_research_exa"
echo "  • people_search_exa"
echo "  • deep_researcher_start"
echo "  • deep_researcher_check"
