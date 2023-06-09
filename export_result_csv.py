import subprocess
import pandas as pd
import os

# Percorso della cartella dei risultati
results_folder = "results"

# Funzione per eseguire il comando ScaveTool e esportare i dati in CSV
def export_to_csv(input_file, root, dirs):
    output_file = f"{input_file}.csv"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:mean -o ./LifeTimeMeanTotal.csv -F CSV-R {input_file}"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:max -o ./LifeTimeMaxTotal.csv -F CSV-R {input_file}"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:min -o ./LifeTimeMinTotal.csv -F CSV-R {input_file}"
    
    command =f"opp_scavetool export -f module=~*.server -f responseTime:max -o ./ResponseTimeTotalMax.csv -F CSV-R {input_file}"
    command =f"opp_scavetool export -f module=~*.server -f responseTime:mean -o ./ResponseTimeTotaMean.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server1 -f responseTime:max -o ./ResponseTimeTotalMax1.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server1 -f responseTime:mean -o ./ResponseTimeTotaMeanl.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server2 -f responseTime:mean -o ./ResponseTimeTotaMean2.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server2 -f responseTime:max -o ./ResponseTimeTotalMax2.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server3 -f responseTime:mean -o ./ResponseTimeTotaMean3.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.server3 -f responseTime:max -o ./ResponseTimeTotalMax3.csv -F CSV-R {input_file}"

    command =f"opp_scavetool export -f module=~*.queue -f queueingTime:histogram -o ./QueueingTimeTotal.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.queue1 -f queueingTime:histogram -o ./QueueingTimeTotal1.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.queue2 -f queueingTime:histogram -o ./QueueingTimeTotal2.csv -F CSV-R {input_file}"
    # command =f"opp_scavetool export -f module=~*.queue3 -f queueingTime:histogram -o ./QueueingTimeTotal3.csv -F CSV-R {input_file}"

    
    subprocess.run(command, shell=True)

# Funzione ricorsiva per eseguire il comando ScaveTool su tutti i file .sca nella cartella e nelle sottocartelle
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        
        for file in files:
            if file.endswith(".sca"):
                input_file = os.path.join(root, file)
                export_to_csv(input_file, root, dirs)
                #print(csv_file)
                
# Esegui il comando ScaveTool su tutti i file .sca nella cartella dei risultati e nelle sottocartelle
process_files(results_folder)
