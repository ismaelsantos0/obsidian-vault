$brainDir = "C:\Users\ismae\.gemini\antigravity\brain"
$obsidianDailyDir = "C:\Users\ismae\OneDrive\Documentos\OBSIDIAN\Daily_Gravity"

if (-not (Test-Path $obsidianDailyDir)) {
    New-Item -ItemType Directory -Force -Path $obsidianDailyDir | Out-Null
}

$backfillData = @{}

Write-Output "Lendo o histórico completo do agente Antigravity..."

Get-ChildItem -Path $brainDir -Directory | ForEach-Object {
    $walkthrough = Join-Path $_.FullName "walkthrough.md"
    if (Test-Path $walkthrough) {
        $modDate = (Get-Item $walkthrough).LastWriteTime.ToString("yyyy-MM-dd")
        $lines = Get-Content $walkthrough -Encoding UTF8
        $title = "Projeto: $($_.Name)"
        
        foreach ($line in $lines) {
            if ($line -match "^#\s+(.+)") {
                $title = $matches[1]
                break
            }
        }

        $entry = "### 🤖 $title`n" + ($lines -join "`n") + "`n`n---`n`n"

        if (-not $backfillData.ContainsKey($modDate)) {
            $backfillData[$modDate] = @()
        }
        $backfillData[$modDate] += $entry
    }
}

Write-Output "Salvando notas diárias..."

foreach ($date in $backfillData.Keys) {
    $dailyNotePath = Join-Path $obsidianDailyDir "$date.md"
    $contentToAdd = ""
    
    foreach ($entry in $backfillData[$date]) {
        $contentToAdd += $entry
    }

    if (Test-Path $dailyNotePath) {
        $existing = Get-Content $dailyNotePath -Encoding UTF8 -Raw
        # Para evitar encher de headers caso seja rodado varias vezes no mesmo dia
        if ($existing -notmatch "Sincronização Retroativa") {
            $header = "`n`n## 🤖 Sincronização Retroativa Antigravity ($date)`n`n**O QUE FOI DECIDIDO E FEITO PELO AGENTE:**`n`n"
            Add-Content -Path $dailyNotePath -Value ($header + $contentToAdd) -Encoding UTF8
            Write-Output "Atualizada nota existente: $date.md"
        }
    } else {
        $header = "# Daily Gravity - Histórico de Decisões`n`n**DATA:** $date`n`n## 🤖 Sincronização Antigravity`n`n**O QUE FOI DECIDIDO E FEITO PELO AGENTE:**`n`n"
        Set-Content -Path $dailyNotePath -Value ($header + $contentToAdd) -Encoding UTF8
        Write-Output "Nova nota diária gerada: $date.md"
    }
}

Write-Output "Backfill concluído com sucesso!"
