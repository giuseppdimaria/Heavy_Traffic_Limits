import subprocess
import pandas as pd
import os

# Percorso della cartella dei risultati
results_folder = "results"

# Funzione per eseguire il comando ScaveTool e esportare i dati in json
def export_to_json(input_file, root, dirs):
    output_file = f"{input_file}.json"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:mean -o ./LifeTimeMeanTotal.json -F JSON {input_file}"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:max -o ./LifeTimeMaxTotal.json -F JSON {input_file}"
    command =f"opp_scavetool export -f module=~*.sink -f lifeTime:min -o ./LifeTimeMinTotal.json -F JSON {input_file}"
    
    command =f"opp_scavetool export -f module=~*.server -f responseTime:mean -o ./ResponseTimeTotaMean.json -F JSON {input_file}"
    command =f"opp_scavetool export -f module=~*.server -f responseTime:max -o ./ResponseTimeTotalMax.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server1 -f responseTime:mean -o ./ResponseTimeTotaMeanl.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server1 -f responseTime:max -o ./ResponseTimeTotalMax1.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server2 -f responseTime:mean -o ./ResponseTimeTotaMean2.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server2 -f responseTime:max -o ./ResponseTimeTotalMax2.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server3 -f responseTime:mean -o ./ResponseTimeTotaMean3.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.server3 -f responseTime:max -o ./ResponseTimeTotalMax3.json -F JSON {input_file}"
    
    command =f"opp_scavetool export -f module=~*.queue -f queueingTime:histogram -o ./QueueingTimeTotal.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.queue1 -f queueingTime:histogram -o ./QueueingTimeTotal1.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.queue2 -f queueingTime:histogram -o ./QueueingTimeTotal2.json -F JSON {input_file}"
    #command =f"opp_scavetool export -f module=~*.queue3 -f queueingTime:histogram -o ./QueueingTimeTotal3.json -F JSON {input_file}"

    
    subprocess.run(command, shell=True)

# Funzione ricorsiva per eseguire il comando ScaveTool su tutti i file .sca nella cartella e nelle sottocartelle
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        
        for file in files:
            if file.endswith(".sca"):
                input_file = os.path.join(root, file)
                export_to_json(input_file, root, dirs)
                #print(json_file)
                
# Esegui il comando ScaveTool su tutti i file .sca nella cartella dei risultati e nelle sottocartelle
process_files(results_folder)
