import PyPDF2, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

f_tjrr = r'C:\Users\Parzival\.gemini\antigravity\brain\d6b2ce85-0932-42a6-a515-1d674b885409\.tempmediaStorage\75b2bd74f804a994.pdf'

reader = PyPDF2.PdfReader(f_tjrr)
print(f"TJRR - Total paginas: {len(reader.pages)}")

pg1 = reader.pages[0].extract_text() or ""
print(f"Titulo PG1: {pg1[:300]}")
print()

hits = []
for i in range(len(reader.pages)):
    try:
        t = reader.pages[i].extract_text() or ""
        if "Ismael" in t:
            hits.append((i+1, t[:1200]))
    except:
        pass

if hits:
    for pg, txt in hits:
        print(f"[PG {pg}]:")
        print(txt)
        print("---")
else:
    print("Ismael nao encontrado no PDF TJRR")
    # Busca parcial - primeiras 10 pags
    for i in range(min(10, len(reader.pages))):
        t = reader.pages[i].extract_text() or ""
        print(f"PG{i+1}: {t[:200]}")
