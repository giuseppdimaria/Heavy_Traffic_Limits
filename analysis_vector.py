import numpy as np
import matplotlib.pyplot as plt
import json
import os

def mean_convergence(array):
    array = np.asarray(array)
    meaned = []
    meaned.append(array[0])
    for i in range(1, array.size):
        meaned.append(np.mean(array[:i]))
    return meaned

def plot_measure(dir_measure):
    DATA_JSON_DIR = "analysis_results/json"
    CHARTS_DIR = "charts"

    if not os.path.exists(CHARTS_DIR):
        os.makedirs(CHARTS_DIR)

    for root, dirs, files in os.walk(DATA_JSON_DIR):
        for file in files:
            if file == "File-vec.json":
                json_file = os.path.join(root, file)
                json_folder = os.path.basename(os.path.dirname(json_file))
                chart_dir = os.path.join(CHARTS_DIR, json_folder)

                if not os.path.exists(chart_dir):
                    os.makedirs(chart_dir)

                with open(json_file) as pointed_file:
                    data = json.load(pointed_file)

                    vectors = []
                    for k in data.keys():
                        if "vectors" in data[k]:
                            vectors += data[k]["vectors"]

                    if vectors:
                        fig, graph = plt.subplots()
                        for vector in vectors:
                            graph.plot(vector['time'], mean_convergence(vector['value']))
                        
                        chart_file = os.path.splitext(file)[0] + ".png"
                        chart_path = os.path.join(chart_dir, chart_file)

                        configname = data[k]['attributes']['configname']
                        graph.set_title(configname)
                        graph.autoscale_view()
                        plt.savefig(chart_path, bbox_inches='tight')
                        plt.clf()
                        

if __name__ == "__main__":
    plot_measure("lifeTime")
    #plot_measure("queueLength")
