#!/bin/bash
# Skill Sync - Sincroniza skills com GitHub
# Uso: ./scripts/sync.sh [--force]

set -e

SKILLS_DIR="$HOME/.openclaw/workspace/skills"
REPO_DIR="$HOME/.openclaw/workspace/nimiguci-skills"
STATE_FILE="$HOME/.openclaw/.skill-sync-state.json"
FORCE_MODE="${1:-}"

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}🔄 Skill Sync - Sincronizando com GitHub${NC}"

# Verifica se o repo existe
if [ ! -d "$REPO_DIR/.git" ]; then
    echo -e "${RED}❌ Repositório não encontrado em $REPO_DIR${NC}"
    echo "Clone primeiro: git clone https://github.com/hendrixfreire/nimiguci-skills.git"
    exit 1
fi

# Verifica se há credenciais hardcoded nas skills (não referências a arquivos)
echo -e "${YELLOW}🔍 Verificando credenciais...${NC}"
CREDENTIALS=$(grep -riE "(api[_-]?key|token|secret|password|credential|bearer)\s*[=:]\s*['\"][a-zA-Z0-9_-]{20,}['\"]" "$SKILLS_DIR" \
    --include="*.py" --include="*.ts" --include="*.js" --include="*.json" 2>/dev/null \
    | grep -v "example\|placeholder\|your_\|\.json\|load_\|os\.path\|open(" | head -5 || true)

if [ -n "$CREDENTIALS" ]; then
    echo -e "${RED}❌ Credenciais detectadas! Não é seguro commitar:${NC}"
    echo "$CREDENTIALS"
    exit 1
fi
echo -e "${GREEN}✓ Nenhuma credencial detectada${NC}"

# Calcula hash atual das skills
CURRENT_HASH=$(find "$SKILLS_DIR" -type f \( -name "*.md" -o -name "*.py" -o -name "*.ts" -o -name "*.sh" \) \
    -exec md5sum {} \; 2>/dev/null | md5sum | cut -d' ' -f1)

# Verifica estado anterior
if [ -f "$STATE_FILE" ] && [ "$FORCE_MODE" != "--force" ]; then
    PREV_HASH=$(cat "$STATE_FILE" 2>/dev/null | grep -o '"lastCommitHash"[[:space:]]*:[[:space:]]*"[^"]*"' | cut -d'"' -f4 || true)
    if [ "$CURRENT_HASH" = "$PREV_HASH" ]; then
        echo -e "${YELLOW}ℹ️  Nenhuma mudança detectada desde o último sync${NC}"
        echo "Use --force para sincronizar mesmo assim"
        exit 0
    fi
fi

# Copia skills para o repo
echo -e "${YELLOW}📁 Copiando skills...${NC}"
cp -r "$SKILLS_DIR"/* "$REPO_DIR/"

# Remove metadados locais
echo -e "${YELLOW}🧹 Limpando metadados locais...${NC}"
cd "$REPO_DIR"
find . -name ".clawhub" -type d -exec rm -rf {} + 2>/dev/null || true
find . -name "_meta.json" -type f -delete 2>/dev/null || true

# Verifica status
STATUS=$(git status --porcelain)
if [ -z "$STATUS" ]; then
    echo -e "${YELLOW}ℹ️  Nenhuma mudança para commitar${NC}"
    exit 0
fi

# Conta mudanças
ADDED=$(echo "$STATUS" | grep -c "^[?A]" || true)
MODIFIED=$(echo "$STATUS" | grep -c "^.M" || true)
DELETED=$(echo "$STATUS" | grep -c "^.D" || true)

# Gera mensagem de commit
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
COMMIT_MSG="chore: sync skills $TIMESTAMP

"
[ $ADDED -gt 0 ] && COMMIT_MSG+="+$ADDED arquivos adicionados
"
[ $MODIFIED -gt 0 ] && COMMIT_MSG+="~$MODIFIED arquivos modificados
"
[ $DELETED -gt 0 ] && COMMIT_MSG+="-$DELETED arquivos removidos
"

# Commit
echo -e "${YELLOW}📝 Commitando mudanças...${NC}"
git add .
git commit -m "$COMMIT_MSG"

# Push
echo -e "${YELLOW}⬆️  Enviando para GitHub...${NC}"
gh auth setup-git 2>/dev/null || true
git push origin master

# Salva estado
mkdir -p "$(dirname "$STATE_FILE")"
cat > "$STATE_FILE" << EOF
{
  "lastSync": "$(date -u -Iseconds)",
  "lastCommitHash": "$CURRENT_HASH"
}
EOF

# Resumo
echo ""
echo -e "${GREEN}✅ Skills sincronizadas com sucesso!${NC}"
echo -e "📊 Mudanças:"
[ $ADDED -gt 0 ] && echo -e "   ${GREEN}+$ADDED adicionados${NC}"
[ $MODIFIED -gt 0 ] && echo -e "   ${YELLOW}~$MODIFIED modificados${NC}"
[ $DELETED -gt 0 ] && echo -e "   ${RED}-$DELETED removidos${NC}"
echo ""
echo -e "🔗 https://github.com/hendrixfreire/nimiguci-skills"
