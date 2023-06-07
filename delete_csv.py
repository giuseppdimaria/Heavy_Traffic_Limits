import subprocess
import os

# Percorso della cartella dei risultati
results_folder = "results"

# Funzione per cancellare il file .csv
def delete_csv_file(input_file):
    csv_file = f"{input_file}.csv"
    if os.path.exists(csv_file):
        os.remove(csv_file)

# Funzione ricorsiva per cancellare i file .csv corrispondenti ai file .sca nella cartella e nelle sottocartelle
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".sca"):
                input_file = os.path.join(root, file)
                delete_csv_file(input_file)

# Cancella i file .csv corrispondenti ai file .sca nella cartella dei risultati e nelle sottocartelle
process_files(results_folder)
