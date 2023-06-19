# Importa il modulo "os" che fornisce una serie di funzioni per interagire con il sistema operativo
import os

# Imposta il numero di ripetizioni e l'etichetta di replicazione
repeat = 20
replication_label = "rep"

for config_file in os.listdir('.'):
    if config_file.startswith('HeavyTrafficLimits_') and config_file.endswith('.ini'):
        # Ottiene il nome della configurazione (senza l'estensione ".ini")
        config_name = config_file
        #print("config_name: ", config_name)
        
        # Esegue la simulazione per la configurazione corrente e tutte le ripetizioni
        for i in range(1, repeat+1):
            # Imposta il seed per la ripetizione corrente in base all'indice
            seed = i*10
            # Costruisce il comando per eseguire la simulazione per la ripetizione corrente
            command = f"heavy_traffic_limits.exe -u Cmdenv -f {config_file}"
            
            # Esegue il comando in un nuovo processo shell
            os.system(command)


