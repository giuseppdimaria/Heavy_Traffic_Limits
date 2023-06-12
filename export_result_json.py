import subprocess
import pandas as pd
import os

# Path to the results folder
results_folder = "results"

# Function to execute the ScaveTool command and export data to JSON
def export_to_json(input_file, root, dirs, file_index):
    json_folder = os.path.join(os.getcwd(), "analysis_results", "json")
    os.makedirs(json_folder, exist_ok=True)

    param_folder = os.path.join(json_folder, root)
    os.makedirs(param_folder, exist_ok=True)

    json_file = f"File-{file_index}.json"
    output_file = os.path.join(param_folder, json_file)

    command = f"opp_scavetool export -f module=~*.sink -f lifeTime:* -o {output_file} -F JSON {input_file}"
    subprocess.run(command, shell=True)

# Recursive function to execute ScaveTool command on .sca files in the folder and subfolders
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".vec"):
                input_file = os.path.join(root, file)
                export_to_json(input_file, root, dirs, 'vec')
                #print(csv_file)
            elif file.endswith(".sca"):
                input_file = os.path.join(root, file)
                export_to_json(input_file, root, dirs, 'sca')

# Execute the ScaveTool command on .sca files in the results folder and subfolders
process_files(results_folder)

# Create csv folder
csv_folder = os.path.join(os.getcwd(), "analysis_results", "csv")
os.makedirs(csv_folder, exist_ok=True)
