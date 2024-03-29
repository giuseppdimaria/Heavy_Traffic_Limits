# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


"""
plotta due grafici separati: uno per il tempo medio di permanenza nel sistema dei job e uno per il tempo massimo di permanenza,
entrambi con i relativi intervalli di confidenza. I grafici vengono salvati nella cartella "charts" come file separati.
"""
def plot_lifeTme():
    # Carica il file CSV
    data = pd.read_csv("lifeTime_mean.csv")
    
    # Estrarre le colonne di interesse
    mean = data["Mean"]
    min_confint_90 = data["Min_ConfInt_t90"]
    max_confint_90 = data["Max_ConfInt_t90"]
    min_confint_95 = data["Min_ConfInt_t95"]
    max_confint_95 = data["Max_ConfInt_t95"]
    
    # Calcola gli errori degli intervalli di confidenza
    error_90 = (max_confint_90 - min_confint_90) / 2
    error_95 = (max_confint_95 - min_confint_95) / 2
    
    # Crea il grafico a linee con intervalli di confidenza per il tempo medio
    plt.figure(figsize=(10, 6))
    plt.errorbar(range(len(mean)), mean, yerr=[error_90, error_95], fmt="o", capsize=4)
    plt.xlabel("Configurazione di Parametri")
    plt.ylabel("Tempo Medio di Permanenza")
    plt.title("Tempo Medio di Permanenza nel Sistema dei Job")
    plt.xticks(range(len(mean)), range(len(mean)))  # Etichette degli assi x come numeri interi
    plt.legend(["Stima Puntuale", "Intervallo di Confidenza al 90%", "Intervallo di Confidenza al 95%"])
    
    # Salvare il grafico
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig('charts/lifeTime_mean.png')
    
    
    """
    # Crea il grafico a linee con intervalli di confidenza per il tempo massimo
    plt.figure(figsize=(10, 6))
    max_value = data["Max_ConfInt_t95"]
    min_value = data["Min_ConfInt_t95"]
    plt.plot(range(len(max_value)), max_value, marker="o")
    plt.plot(range(len(min_value)), min_value, marker="o")
    plt.fill_between(range(len(max_value)), min_value, max_value, alpha=0.3)
    plt.xlabel("Configurazione di Parametri")
    plt.ylabel("Tempo Massimo di Permanenza")
    plt.title("Tempo Massimo di Permanenza nel Sistema dei Job")
    plt.xticks(range(len(max_value)), range(len(max_value)))  # Etichette degli assi x come numeri interi
    plt.legend(["Stima Puntuale", "Intervallo di Confidenza al 95%"])
    
    # Salvare il grafico
    plt.savefig('charts/lifeTime_max.png')
    """
    
    # Mostra i grafici
    plt.show()



"""
plotta un grafico con la mediana della distribuzione del tempo di risposta di ogni singolo servente, insieme agli intervalli di confidenza corrispondenti.
Il grafico viene salvato nella cartella "charts" come file separato.
"""
def plot_serverResponseTime():
    # Carica il file CSV
    data = pd.read_csv("server_response_time.csv")
    
    
    # Filtra i dati solo per i tre serventi del tuo sistema
    servers = ["Server1", "Server2", "Server3"]
    filtered_data = data[data["File"].str.contains("|".join(servers))]
    
    # Estrarre le colonne di interesse
    median = filtered_data.groupby("File")["Median"].mean().values
    min_confint_90 = filtered_data.groupby("File")["Min_ConfInt_90"].mean().values
    max_confint_90 = filtered_data.groupby("File")["Max_ConfInt_90"].mean().values
    min_confint_95 = filtered_data.groupby("File")["Min_ConfInt_95"].mean().values
    max_confint_95 = filtered_data.groupby("File")["Max_ConfInt_95"].mean().values
        
    # Calcola gli errori degli intervalli di confidenza
    error_90 = (max_confint_90 - min_confint_90) / 2
    error_95 = (max_confint_95 - min_confint_95) / 2
    
    # Crea il grafico a linee con intervalli di confidenza per la mediana
    plt.figure(figsize=(10, 6))
    x = range(len(median))
    plt.bar(x, median, yerr=[error_90, error_95], capsize=4)
    plt.xlabel("Serventi")
    plt.ylabel("Mediana del Tempo di Risposta")
    plt.title("Mediana della Distribuzione del Tempo di Risposta di ogni Singolo Servente")
    plt.xticks(x, servers)  # Etichette degli assi x con i nomi dei serventi
    plt.legend(["Stima Puntuale", "Intervallo di Confidenza al 90%", "Intervallo di Confidenza al 95%"])
    
    # Salvare il grafico
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig('charts/server_response_time_median.png')
    
    # Mostra il grafico
    plt.show()





"""
plotta un grafico a barre con il fattore di utilizzo dei singoli server.
I server sono rappresentati sull'asse x, mentre il fattore di utilizzo è rappresentato sull'asse y.
"""
def plot_serverFactorUtilization():    
    # Carica il file CSV
    data = pd.read_csv("factor_utilization_data.csv")
    
    # Estrarre le colonne di interesse
    server = data["Server"]
    factor_utilization = data["Factor_Utilization"]
    
    # Crea il grafico a barre per il fattore di utilizzo
    plt.figure(figsize=(6, 4))
    plt.bar(server, factor_utilization)
    plt.xlabel("Serventi")
    plt.ylabel("Fattore di Utilizzo")
    plt.title("Fattore di Utilizzo dei Singoli Server")
    plt.xticks(range(len(server)), server)  # Etichette degli assi x come nomi dei server
    
    # Salvare il grafico
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig('charts/factor_utilization.png')
    
    # Mostra il grafico
    plt.show()




def plot_systemResponseTime():
    # Carica il file CSV specificando il delimitatore come '\t'
    data = pd.read_csv('system_response_time.csv')
    
    # Seleziona solo i dati relativi alla colonna 'File'
    file_names = data['Name']
    
    # Seleziona solo i dati relativi alla colonna 'Mean' come valore delle barre
    response_time_median = data['Mean']
    
    # Seleziona solo i dati relativi all'intervallo di confidenza del 95%
    conf_int_95_min = data['Min_ConfInt_t95']
    conf_int_95_max = data['Max_ConfInt_t95']
    
    # Seleziona solo i dati relativi all'intervallo di confidenza del 90%
    conf_int_90_min = data['Min_ConfInt_t90']
    conf_int_90_max = data['Max_ConfInt_t90']
    
    # Traccia i dati
    x = np.arange(len(file_names))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, response_time_median, width, label='Median')
    rects2 = ax.bar(x + width/2, conf_int_95_max - conf_int_95_min, width, yerr=[conf_int_95_min, conf_int_95_max], label='95% Confidence Interval')

    ax.set_xlabel('Run di Simulazione')
    ax.set_ylabel('Tempo')
    ax.set_title('Tempo di Risposta del Sistema (Mediana) con Intervallo di Confidenza al 95%')
    ax.set_xticks(x)
    ax.set_xticklabels(x)
    ax.legend()

    plt.tight_layout()
    
    # Salvare il grafico
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig('charts/system_response_time_median.png')
    
    # Mostra il grafico
    plt.show()


"""
Crea un rettangolo colorato centrato sull'indice x[i] della barra corrispondente,
con un'altezza che rappresenta il rapporto tra il periodo di warm-up (warmup_period)
e il tempo di risposta medio per quella simulazione(response_time_mean.iloc[i]).

In questo modo, il grafico a barre evidenzia il periodo del transiente iniziale rispetto alla media del tempo di risposta del sistema.
"""
def plot_transient():
    # Carica il file CSV con i dati del tempo di risposta del sistema
    data = pd.read_csv('system_response_time.csv')
    
    # Seleziona solo i dati relativi alla colonna 'File'
    file_names = data['Name']
    
    # Seleziona solo i dati relativi alla colonna 'Mean' come valore delle barre
    response_time_mean = data['Mean']
    
    # Imposta il periodo di warm-up fisso
    warmup_period = 30000
    
    # Traccia i dati
    x = np.arange(len(file_names))
    width = 0.35
    plt.bar(x, response_time_mean, width, label='Mean')
    
    # Aggiungi etichette e titoli
    plt.xlabel('Run di Simulazione')
    plt.ylabel('Tempo di Risposta (Media)')
    plt.title('Transiente Iniziale - Tempo di Risposta del Sistema')
    plt.xticks(x, rotation=90)
    plt.legend()
    
    # Aggiungi rettangoli colorati per evidenziare il periodo di warm-up
    for i in range(len(x)):
        plt.axvspan(x[i] - 0.5, x[i] + 0.5, facecolor='lightgray', alpha=0.5, ymin=0, ymax=warmup_period / response_time_mean.iloc[i])
    
    # Salvare il grafico
    if not os.path.exists('charts'):
        os.makedirs('charts')
    plt.savefig('charts/initial_transient.png')
    
    # Mostra il grafico
    plt.show()








if __name__ == "__main__":
    plot_lifeTme()
    # plot_serverResponseTime()
    # plot_serverFactorUtilization()
    # plot_systemResponseTime()
    # plot_transient()