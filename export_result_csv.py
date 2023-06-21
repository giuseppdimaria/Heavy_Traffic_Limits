import subprocess
import pandas as pd
import os

# Path to the results folder
results_folder = "results"

# Function to execute the ScaveTool command and export data to JSON
def export_to_csv(input_file, root, dirs):
    csv_folder = os.path.join(os.getcwd(), "analysis_results", "csv")
    os.makedirs(csv_folder, exist_ok=True)

    param_folder = os.path.join(csv_folder, root)
    os.makedirs(param_folder, exist_ok=True)
    
    config_name = os.path.basename(root)  # Get the name of the configuration folder


    # csv_file = f"{csv_file_name}.csv"
    output_file = os.path.join(param_folder, f"{config_name}_lifeTime.csv")
    output_file_2 = os.path.join(param_folder, f"{config_name}_System_RT.csv")
    output_file_3 = os.path.join(param_folder, f"{config_name}_Server1_responseTime.csv")
    output_file_4 = os.path.join(param_folder, f"{config_name}_Server1_busy.csv")
    output_file_5 = os.path.join(param_folder, f"{config_name}_Server2_responseTime.csv")
    output_file_6 = os.path.join(param_folder, f"{config_name}_Server2_busy.csv")
    output_file_7 = os.path.join(param_folder, f"{config_name}_Server3_responseTime.csv")
    output_file_8 = os.path.join(param_folder, f"{config_name}_Server3_busy.csv")

    command = f"opp_scavetool export -f module=~*.sink -f lifeTime:* -o {output_file} -F CSV-R {input_file}"
    
    command_2 = f"opp_scavetool export -f module=~*.sink -f responseTime:* -o {output_file_2} -F CSV-R {input_file}"
    
    command_3 = f"opp_scavetool export -f module=~*.server1 -f responseTime:* -o {output_file_3} -F CSV-R {input_file}"
    command_4 = f"opp_scavetool export -f module=~*.server1 -f busy:* -o {output_file_4} -F CSV-R {input_file}"
    
    command_5 = f"opp_scavetool export -f module=~*.server2 -f responseTime:* -o {output_file_5} -F CSV-R {input_file}"
    command_6 = f"opp_scavetool export -f module=~*.server2 -f busy:* -o {output_file_6} -F CSV-R {input_file}"
    
    command_7 = f"opp_scavetool export -f module=~*.server3 -f responseTime:* -o {output_file_7} -F CSV-R {input_file}"
    command_8 = f"opp_scavetool export -f module=~*.server3 -f busy:* -o {output_file_8} -F CSV-R {input_file}"
    
    
    # subprocess.run(command, shell=True)
    # subprocess.run(command_2, shell=True)
    subprocess.run(command_3, shell=True)
    # subprocess.run(command_4, shell=True)
    subprocess.run(command_5, shell=True)
    # subprocess.run(command_6, shell=True)
    subprocess.run(command_7, shell=True)
    # subprocess.run(command_8, shell=True)

# Recursive function to execute ScaveTool command on .sca files in the folder and subfolders
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".sca"):# or file.endswith(".vec"):
                input_file = os.path.join(root, file)
                export_to_csv(input_file, root, dirs)

# Execute the ScaveTool command on .sca files in the results folder and subfolders
process_files(results_folder)

# Create csv folder
csv_folder = os.path.join(os.getcwd(), "analysis_results", "csv")
os.makedirs(csv_folder, exist_ok=True)
