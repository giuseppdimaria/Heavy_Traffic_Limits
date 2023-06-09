import csv
import logging
import math
import os
import pandas as pd

t95 = 2.086
t90 = 1.725
runs = 20


# def create_csv_mean(DATA, log_level):
#     logging.basicConfig(format='%(message)s', level=log_level)
#     data = []
#     for config in [directory for directory in os.listdir(DATA)]:
#         config_dir = os.path.join(DATA, config)
#         logging.debug(config)
#         for file in os.listdir(config_dir):
#             file = os.path.join(config_dir, file)
#             logging.debug('\t' + file.replace('.csv', ''))
#             if 'Mean' in file:
#                 with open(file_path, 'r') as csv_file:
#                     reader = csv.DictReader(csv_file)
#                     for row in reader:
#                         if row['type'] == 'scalar' and row['attrname'] == 'lifeTime:max':
#                             name = row['module']
#                             value = float(row['value'])
#                             data.append([name, value])
#
#                 csv_file = pd.read_csv(file)
#                 name = csv_file['Name'][0].replace(':mean', '')
#                 mean = csv_file['Unnamed: 4'].mean()
#                 logging.debug('\t\tMean: ' + str(mean))
#                 std_dev = csv_file['Unnamed: 4'].std()
#                 logging.debug('\t\tStdDev: ' + str(std_dev))
#                 var = csv_file['Unnamed: 4'].var()
#                 logging.debug('\t\tVar: ' + str(var))
#                 std_err = std_dev / (math.sqrt(runs))
#                 logging.debug('\t\tStdErr:' + str(std_err))
#                 min_95 = mean - (t95 * math.sqrt(var) / math.sqrt(runs))
#                 max_95 = mean + (t95 * math.sqrt(var) / math.sqrt(runs))
#                 logging.debug("\t\tMin t95 ConfInt: " + str(min_95) + ' - Max t95 ConfInt: ' + str(max_95))
#                 min_90 = mean - (t90 * math.sqrt(var) / math.sqrt(runs))
#                 max_90 = mean + (t90 * math.sqrt(var) / math.sqrt(runs))
#                 logging.debug("\t\tMin t90 ConfInt: " + str(min_90) + ' - Max t90 ConfInt: ' + str(max_90))
#                 data.append([config, name, round(mean, 3), round(std_dev, 3), round(var, 3), round(std_err, 3),
#                              round(min_95, 3), round(max_95, 3), round(min_90, 3), round(max_90, 3)])
#
#     df_data = pd.DataFrame(data)
#     df_data.columns = ['Config', 'Name', 'Mean', 'Std Dev', 'Var', 'Std Err', 'Min ConfInt t95', 'Max ConfInt t95',
#                        'Min ConfInt t90', 'Max ConfInt t90']
#
#     df_data = df_data.sort_values(by=['Config', 'Name'], ascending=True)
#     logging.debug(df_data)
#     logging.debug(df_data.head())
#
#     filename = os.path.join(DATA, 'Total_Data_Mean.csv')
#     df_data.to_csv(filename, index=False)
#     logging.info(f"CSV MEAN CREATED: {filename.replace('./', '')}")
#     return df_data
#
#
# # Esempio di utilizzo della funzione create_csv_mean
# DATA = 'csv_folder'  # Inserisci il percorso della directory dei dati
# log_level = logging.DEBUG  # Modifica il livello di registrazione a tuo piacimento


def create_csv_mean(DATA, log_level):
    print('ciao')

"""
create_csv_mean legge i file CSV presenti nella directory DATA e calcola le statistiche medie, deviazione standard, varianza,
errore standard e intervalli di confidenza, per i valori della colonna "Unnamed: 4" nei file CSV.
I risultati vengono quindi salvati in un nuovo file CSV chiamato "Total_Data_Mean.csv" nella stessa directory dei dati.
"""
create_csv_mean(DATA, log_level)
