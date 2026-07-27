# Extrair Logs do Antigravity para Obsidian

$brainDir = "C:\Users\ismae\.gemini\antigravity\brain"
$obsidianDailyDir = "C:\Users\ismae\OneDrive\Documentos\OBSIDIAN\Daily_Gravity"
$dateStr = (Get-Date).ToString("yyyy-MM-dd")
$dailyNotePath = Join-Path $obsidianDailyDir "$dateStr.md"

$content = "`n`n## 🤖 Sincronização Antigravity ($dateStr)`n`n"
$content += "**O QUE FOI DECIDIDO E FEITO PELO AGENTE:**`n`n"
$foundSomething = $false

Write-Output "Buscando os trabalhos concluídos hoje pelo agente..."

Get-ChildItem -Path $brainDir -Directory | ForEach-Object {
    $walkthrough = Join-Path $_.FullName "walkthrough.md"
    if (Test-Path $walkthrough) {
        $modDate = (Get-Item $walkthrough).LastWriteTime.ToString("yyyy-MM-dd")
        
        # Filtra apenas o que foi gerado/modificado hoje
        if ($modDate -eq $dateStr) {
            $foundSomething = $true
            $lines = Get-Content $walkthrough -Encoding UTF8
            $title = "Projeto: $($_.Name)"
            
            # Tenta encontrar o primeiro Título (# Título) no Walkthrough
            foreach ($line in $lines) {
                if ($line -match "^#\s+(.+)") {
                    $title = $matches[1]
                    break
                }
            }

            $content += "### $title`n"
            $content += ($lines -join "`n")
            $content += "`n`n---`n`n"
        }
    }
}

if ($foundSomething) {
    if (-not (Test-Path $obsidianDailyDir)) {
        New-Item -ItemType Directory -Force -Path $obsidianDailyDir | Out-Null
    }
    
    # Se a nota de hoje já existir, ele anexa (append) no final
    if (Test-Path $dailyNotePath) {
        Add-Content -Path $dailyNotePath -Value $content -Encoding UTF8
        Write-Output "Nota atualizada: Adicionado ao final de $dailyNotePath"
    } else {
        $header = "# Daily Gravity - Histórico de Decisões`n`n**DATA:** $dateStr`n`n"
        Set-Content -Path $dailyNotePath -Value ($header + $content) -Encoding UTF8
        Write-Output "Nova Daily Note gerada com sucesso em: $dailyNotePath"
    }
} else {
    Write-Output "Nenhum documento 'walkthrough.md' atualizado hoje foi encontrado no cérebro do Antigravity."
}
