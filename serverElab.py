import os
import csv

# Definisci i termini da cercare per la rimozione delle righe
terms_to_remove = ["procs", "memory", "proc", "età", "cache"]

# Directory contenente i file CSV
input_directory = "./serverResults"

# Directory dove verranno salvati i file CSV elaborati
output_directory = "./serverResults1"

# Assicurati che la directory di output esista, altrimenti creala
os.makedirs(output_directory, exist_ok=True)

# Elabora ciascun file nella directory di input
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        with open(input_path, 'r') as input_file, open(output_path, 'w', newline='') as output_file:
            csv_reader = csv.reader(input_file)
            csv_writer = csv.writer(output_file)

            for row in csv_reader:
                # Controlla se la riga contiene uno dei termini da rimuovere
                if not any(term in row for term in terms_to_remove):
                    csv_writer.writerow(row)

print("Operazione completata.")
