import subprocess
import pandas as pd
import os

# Percorso della cartella dei risultati
results_folder = "results"

# Funzione per eseguire il comando ScaveTool e esportare i dati in CSV
def export_to_csv(input_file):
    output_file = f"{input_file}.csv"
    command = f"opp_scavetool x {input_file} -o {output_file} -F CSV-R"
    subprocess.run(command, shell=True)

# Funzione ricorsiva per eseguire il comando ScaveTool su tutti i file .sca nella cartella e nelle sottocartelle
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".sca"):
                input_file = os.path.join(root, file)
                export_to_csv(input_file)
                #print(csv_file)
                
# Esegui il comando ScaveTool su tutti i file .sca nella cartella dei risultati e nelle sottocartelle
process_files(results_folder)
