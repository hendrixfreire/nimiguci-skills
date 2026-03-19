#!/bin/bash
# Setup script for Exa MCP

echo "Setting up Exa MCP..."

# Check if EXA_API_KEY is set
if [ -z "$EXA_API_KEY" ]; then
    echo "⚠️  EXA_API_KEY not set"
    echo "Get your API key at: https://exa.ai"
    echo ""
    echo "Set it with:"
    echo "  export EXA_API_KEY='your-key-here'"
    exit 1
fi

echo "✓ EXA_API_KEY found"

# Check if npx is available
if ! command -v npx &> /dev/null; then
    echo "❌ npx not found. Install Node.js first:"
    echo "  https://nodejs.org"
    exit 1
fi

echo "✓ npx available"

# Test the MCP server
echo ""
echo "Testing Exa MCP connection..."
npx -y @exa-ai/mcp --help 2>/dev/null || echo "Note: MCP server will be installed on first use"

echo ""
echo "✅ Exa MCP setup complete!"
echo ""
echo "Add to your MCP config:"
echo '{'
echo '  "mcpServers": {'
echo '    "exa": {'
echo '      "command": "npx",'
echo '      "args": ["-y", "@exa-ai/mcp"],'
echo '      "env": {'
echo "        \"EXA_API_KEY\": \"$EXA_API_KEY\""
echo '      }'
echo '    }'
echo '  }'
echo '}'
