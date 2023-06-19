import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os
import math
import logging
from fileinput import input
import statistics
from fontTools.pens import statisticsPen

pd.set_option('display.width', 200)
pd.set_option('display.max_columns', 10)

t95 = 2.086     # Valore critico per l'intervallo di confidenza al 95%
t90 = 1.725
runs = 20

lifeTime_index = 34


def create_csv_lifeTimemean(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    for root, dirs, files in os.walk(DATA):
        for file in files:
            if(file.endswith('lifeTime.csv')):
                print(file)
                input()
                
                csv_file = pd.read_csv(os.path.join(root, file))
                
                # print(type(csv_file['vectime'][35])) #is a string type
                # inpuit()
                
                name = csv_file['name'][36].replace(':vector', '')
                
                vectimelist = []
                
                if type(csv_file['vectime'][lifeTime_index]) == str:
                    vectimelist = list(map(float, csv_file['vectime'][lifeTime_index].split(" ")))
                elif type(csv_file['vectime'][lifeTime_index+1]) == str:
                    vectimelist = list(map(float,csv_file['vectime'][lifeTime_index+1].split(" ")))
                
                mean = statistics.fmean(vectimelist)
                std_dev = statistics.stdev(vectimelist)
                variance = statistics.variance(vectimelist)
                std_err = std_dev / (math.sqrt(runs))
        
                min_95 = mean - (t95 * math.sqrt(variance) / math.sqrt(runs))
                max_95 = mean + (t95 * math.sqrt(variance) / math.sqrt(runs))
                min_90 = mean - (t90 * math.sqrt(variance) / math.sqrt(runs))
                max_90 = mean + (t90 * math.sqrt(variance) / math.sqrt(runs))
        
                print('mean: ', mean)
                print('std_dev: ', std_dev)
                print('variance: ', variance)
                print('std_err: ', std_err)
                print('min_95: ', min_95)
                print('max_95: ', max_95)
                print('min_90: ', min_90)
                print('max_90: ', max_90)
                print('\n\n')
        
                data.append([file, name, round(mean, 3), round(std_dev, 3), round(variance, 3), round(std_err, 3),
                                 round(min_95, 3), round(max_95, 3), round(min_90, 3), round(max_90, 3)])
        df_data = pd.DataFrame(data, columns=['File', 'Name', 'Mean', 'Std_Dev', 'Variance', 'Std_Err', 'Min_ConfInt_t95', 'Max_ConfInt_t95',
                                              'Min_ConfInt_t90', 'Max_ConfInt_t90'])
        df_data = df_data.sort_values(by=['File', 'Name'], ascending=True)
        
        
    df_data.reset_index(drop=True, inplace=True)
    logging.debug(df_data)
    logging.debug(df_data.head())
    df_data.to_csv('./lifeTime_mean.csv', index=False)
    logging.info('CSV MEAN CREATED ' + DATA.replace('./', ''))
    return df_data




SRT_index = 89  # HeavyTrafficLimits.sink - responseTime:histogram

def create_csv_system_responseTime(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    for root, dirs, files in os.walk(DATA):
        for file in files:
            if(file.endswith('System_responseTime.csv')):
                csv_file = pd.read_csv(os.path.join(root, file))
                # print(csv_file)
                name = csv_file['name'][SRT_index].replace(':histogram', '')
                filtered_data = csv_file[csv_file['module'] == 'HeavyTrafficLimits.sink']
                value = filtered_data['value'].dropna()
                # print(value)
                # print(type(value))           # float type

                meanvaluelist = []
                meanvaluelist.extend(value.tolist())
                
                # print("\n\nMEAN VALUE LIST", meanvaluelist)
                
                mean = statistics.fmean(meanvaluelist)
                std_dev = statistics.stdev(meanvaluelist)
                variance = statistics.variance(meanvaluelist)
                std_err = std_dev / (math.sqrt(runs))
                
                min_95 = mean - (t95 * math.sqrt(variance) / math.sqrt(runs))
                max_95 = mean + (t95 * math.sqrt(variance) / math.sqrt(runs))
                min_90 = mean - (t90 * math.sqrt(variance) / math.sqrt(runs))
                max_90 = mean + (t90 * math.sqrt(variance) / math.sqrt(runs))
                
                print('mean: ', mean)
                print('std_dev: ', std_dev)
                print('variance: ', variance)
                print('std_err: ', std_err)
                print('min_95: ', min_95)
                print('max_95: ', max_95)
                print('min_90: ', min_90)
                print('max_90: ', max_90)
                print('\n\n')
    
                data.append([file, name, round(mean, 3), round(std_dev, 3), round(variance, 3), round(std_err, 3),
                             round(min_95, 3), round(max_95, 3), round(min_90, 3), round(max_90, 3)])
    
    df_data = pd.DataFrame(data, columns=['File', 'Name', 'Mean', 'Std_Dev', 'Variance', 'Std_Err', 'Min_ConfInt_t95', 'Max_ConfInt_t95',
                                          'Min_ConfInt_t90', 'Max_ConfInt_t90'])
    df_data = df_data.sort_values(by=['File', 'Name'], ascending=True)
    df_data.reset_index(drop=True, inplace=True)
    
    df_data.to_csv('system_response_time.csv', index=False)
    logging.info('CSV system_response_time.csv CREATED ' + DATA.replace('./', ''))
    return df_data






def calculate_utilization_factor(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    
    utilization_data = pd.DataFrame(columns=['Server', 'Factor_Utilization'])
    
    for root, dirs, files in os.walk(DATA):
        for file in files:
            if 'busy' in file:
                csv_path = os.path.join(root, file)
                csv_file = pd.read_csv(csv_path)
                
                csv_file['module'] = csv_file['module'].astype(str)  # Convert 'module' column to string
                
                filtered_data = csv_file[(csv_file['type'] == 'scalar') & (csv_file['module'].str.contains('HeavyTrafficLimits\.server[1-3]'))]
                values = filtered_data['value'].dropna().astype(float)
                
                if len(values) > 0:
                    server = file.split('_')[0]
                    utilization_factor = statistics.mean(values)
                    utilization_data = utilization_data.append({'Server': server, 'Factor_Utilization': utilization_factor}, ignore_index=True)
    
    if utilization_data.empty:
        print("No data available to calculate the utilization factor.")
        return

    utilization_data.to_csv('factor_utilization_data.csv', index=False)
    print("Utilization data saved to 'factor_utilization_data.csv'")

         


def create_csv_server_responseTime(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    
    for root, dirs, files in os.walk(DATA):
        for file in files:
            if file.endswith('_responseTime.csv'):
                csv_file = pd.read_csv(os.path.join(root, file))
                server_number = file.split('_')[0][-1]
                module = f'HeavyTrafficLimits.server{server_number}'
                filtered_data = csv_file[csv_file['module'] == module]
                values = filtered_data['value'].dropna()

                if not values.empty:
                    median = np.median(values)
                    interval_95 = np.percentile(values, [2.5, 97.5])
                    interval_90 = np.percentile(values, [5, 95])
                    
                    data.append([file, module, round(median, 3), round(interval_95[1] - interval_95[0], 3),
                                 round(interval_95[0], 3), round(interval_95[1], 3),
                                 round(interval_90[0], 3), round(interval_90[1], 3)])

    df_data = pd.DataFrame(data, columns=['File', 'Module', 'Median', 'ConfInt_95_Width',
                                          'Min_ConfInt_95', 'Max_ConfInt_95',
                                          'Min_ConfInt_90', 'Max_ConfInt_90'])
    df_data = df_data.sort_values(by=['File', 'Module'], ascending=True)
    df_data.reset_index(drop=True, inplace=True)

    df_data.to_csv('server_response_time.csv', index=False)
    logging.info('CSV server_response_time.csv created ' + DATA.replace('./', ''))
    return df_data






if __name__ == "__main__":
    
    # Extract data results with transient
    # df_data_lifeTimemean = create_csv_lifeTimemean('./analysis_results/csv/results', logging.INFO)
    # df_data_system_responseTime = create_csv_system_responseTime('./analysis_results/csv/results', logging.INFO)
    # df_data_server_busy = calculate_utilization_factor('./analysis_results/csv/results', logging.INFO)
    df_data_server_responseTime = create_csv_server_responseTime('./analysis_results/csv/results', logging.INFO)