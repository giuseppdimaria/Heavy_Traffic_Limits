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

    csv_file = f"File.csv"
    output_file = os.path.join(param_folder, csv_file)

    command = f"opp_scavetool export -f module=~*.sink -f lifeTime:* -o {output_file} -F CSV-R {input_file}"
    subprocess.run(command, shell=True)

# Recursive function to execute ScaveTool command on .sca files in the folder and subfolders
def process_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".sca") or file.endswith(".vec"):
                input_file = os.path.join(root, file)
                export_to_csv(input_file, root, dirs)
            """
            elif file.endswith(".sca"):
                input_file = os.path.join(root, file)
                export_to_csv(input_file, root, dirs)
            """

# Execute the ScaveTool command on .sca files in the results folder and subfolders
process_files(results_folder)

# Create csv folder
csv_folder = os.path.join(os.getcwd(), "analysis_results", "csv")
os.makedirs(csv_folder, exist_ok=True)
