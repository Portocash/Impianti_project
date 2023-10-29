import os
import json
import csv

# Ottieni il percorso della cartella "results" nel percorso corrente
result_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")

# Ottieni il percorso della cartella corrente dello script Python
script_directory = os.path.dirname(os.path.abspath(__file__))

# Crea il percorso completo per il file CSV nella stessa cartella dello script
csv_file_path = os.path.join(script_directory, "report.csv")

# Lista dei nomi delle colonne per il file CSV
csv_columns = ["CTT", "sampleCount", "errorCount", "meanResTime", "medianResTime", "throughput"]

# Apre il file CSV per la scrittura
with open(csv_file_path, "w", newline="") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_columns, delimiter='\t')
    writer.writeheader()

    # Ciclo attraverso le cartelle all'interno di "results"
    for ctt in range(300, 4301, 250):
        for num in range(1, 4):
            folder_name = f"{ctt}r_{num}_dk-report"
            json_file_path = os.path.join(result_folder, folder_name, "statistics.json")

            # Verifica se il file JSON esiste nella cartella corrente
            if os.path.exists(json_file_path):
                with open(json_file_path, "r") as json_file:
                    data = json.load(json_file)
                    # Modifica i separatori di unità-decimali da punto a virgola
                    row_data = {
                        "CTT": str(ctt).replace(".", ","),
                        "sampleCount": str(data["Total"]["sampleCount"]).replace(".", ","),
                        "errorCount": str(data["Total"]["errorCount"]).replace(".", ","),
                        "meanResTime": str(data["Total"]["meanResTime"]).replace(".", ","),
                        "medianResTime": str(data["Total"]["medianResTime"]).replace(".", ","),
                        "throughput": str(data["Total"]["throughput"]).replace(".", ","),
                    }
                    writer.writerow(row_data)

print(f"Il file report.csv è stato creato con successo in: {csv_file_path}")