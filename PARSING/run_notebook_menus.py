import os
import papermill as pm

# Percorso della cartella contenente i PDF
cartella_menu = "C:/Users/lparigi/Downloads/letspizza/Hackapizza Dataset/Menu"

# Trova tutti i file PDF nella cartella
pdf_files = [f for f in os.listdir(cartella_menu) if f.endswith(".pdf")]

# Nome del notebook da eseguire
notebook_input = "C:/Users/lparigi/Downloads/letspizza/PARSING/PARSE_MENUs.ipynb"

# Esegui il notebook per ogni file PDF
for pdf in pdf_files:
    file_path = os.path.join(cartella_menu, pdf)
    output_notebook = f"output_{pdf.replace('.pdf', '')}.ipynb"

    print(f"Eseguo il notebook per: {file_path}")

    pm.execute_notebook(
        notebook_input,    # Notebook di input
        output_notebook,   # Notebook di output
        parameters={"file_path": file_path}  # Passa il parametro dinamico
    )

print("Tutte le esecuzioni sono complete! 🚀")
