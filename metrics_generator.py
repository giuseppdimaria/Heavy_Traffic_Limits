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

t95 = 2.086
t90 = 1.725
runs = 20

vec_index = 34


def create_csv_mean(DATA, log_level):
    logging.basicConfig(format='%(message)s', level=log_level)
    data = []
    
    for root, dirs, files in os.walk(DATA):
        
        for file in files:

            csv_file = pd.read_csv(os.path.join(root,file))
            
            name = csv_file['name'][36].replace(':vector', '')
        
            vectimelist = []
            
            if type(csv_file['vectime'][vec_index]) == str:
                vectimelist = list(map(float,csv_file['vectime'][vec_index].split(" ")))
            elif type(csv_file['vectime'][vec_index+1]) == str:
                vectimelist = list(map(float,csv_file['vectime'][vec_index+1].split(" ")))
                            
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
    df_data.to_csv('./Total_Data_Mean.csv', index=False)
    logging.info('CSV MEAN CREATED ' + DATA.replace('./', ''))
    return df_data


if __name__ == "__main__":
    # Extract data results with transient
    df_data_mean = create_csv_mean('./analysis_results/csv/results', logging.INFO)