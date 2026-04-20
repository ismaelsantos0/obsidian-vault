import PyPDF2, sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = {
    "IFRR": r'C:\Users\Parzival\.gemini\antigravity\brain\d6b2ce85-0932-42a6-a515-1d674b885409\.tempmediaStorage\ea092e579f67e0ea.pdf',
    "TJRR": r'C:\Users\Parzival\.gemini\antigravity\brain\d6b2ce85-0932-42a6-a515-1d674b885409\.tempmediaStorage\75b2bd74f804a994.pdf'
}

search_name = "Ismael Oliveira dos Santos"

for site, path in files.items():
    print(f"=== Analisando {site} ===")
    try:
        reader = PyPDF2.PdfReader(path)
        found = False
        for i in range(len(reader.pages)):
            text = reader.pages[i].extract_text() or ""
            if search_name.lower() in text.lower():
                print(f"[ACHADO NA PÁGINA {i+1}]")
                # Try to find the name and take 500 chars around it
                start_idx = text.lower().find(search_name.lower())
                snippet = text[max(0, start_idx-200) : min(len(text), start_idx+300)]
                print("Contexto:")
                print("..." + snippet + "...")
                print("-" * 30)
                found = True
        if not found:
            print(f"Nome completo não encontrado em {site}. Verificando nome parcial...")
            first_name = "Ismael Oliveira"
            for i in range(len(reader.pages)):
                text = reader.pages[i].extract_text() or ""
                if first_name.lower() in text.lower():
                    print(f"[PARCIAL NA PÁGINA {i+1}]")
                    start_idx = text.lower().find(first_name.lower())
                    snippet = text[max(0, start_idx-200) : min(len(text), start_idx+300)]
                    print("Contexto:")
                    print("..." + snippet + "...")
                    print("-" * 30)
                    found = True
        if not found:
            print(f"Nenhuma ocorrência encontrada em {site}.")
    except Exception as e:
        print(f"Erro ao processar {site}: {e}")
    print("\n")
