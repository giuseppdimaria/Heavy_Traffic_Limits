import os

# Set the number of repetitions and the replication label
repeat = 20
replication_label = "rep"

# Set the possible values for the lambda and switchProbability parameters
lambda_values = [2.0, 1.4, 1.2, 1.0]
switch_prob_values = [0.2, 0.4, 0.8]

# Set the possible values for the serviceTime parameter
server_service_times = [
    "uniform(1s,6s)",
    "uniform(2s,4s)",
    "exponential(0.33s)",
    "exponential(0.25s)"
]

# Set the possible values for the S1 exponential distribution parameter
s1_exponential_params = [
    {"mean": "0.333s", "name": "mu1_3"},
    {"mean": "0.25s", "name": "mu1_4"}
]

# Set the crash times for the servers
server_crash_times = {
    "server1": 500,
    "server2": 750,
    "server3": 1000
}

# Iterate over all the possible combinations of the parameters
for lambda_val in lambda_values:
    for switch_prob_val in switch_prob_values:
        for service_time in server_service_times:
            # Create a unique name for the configuration based on the values of the parameters
            config_name = f"lambda_{lambda_val}-switchProb_{switch_prob_val}-serviceTime_{service_time}"
            
            # Create the directory for the simulation results
            result_dir = f"results/{config_name}"
            #os.makedirs(result_dir, exist_ok=True)
            
            # Generate the configuration file for the current combination of parameters
            with open(f"HeavyTrafficLimits_{config_name}.ini", "w") as f:
                f.write(f"""[General]
network = HeavyTrafficLimits
sim-time-limit = 100000s
repeat = {repeat}
replication-label = {replication_label}${{repetition}}
result-dir = {result_dir}
warmup-period = 30000s
**.source.lambda = {lambda_val}
**.router.switchProbability = {switch_prob_val}
**.server1.serviceTime = {service_time}
**.server2.serviceTime = {service_time}
**.server3.serviceTime = {service_time}
**.server1.crashTime = {server_crash_times["server1"]}
**.server2.crashTime = {server_crash_times["server2"]}
**.server3.crashTime = {server_crash_times["server3"]}
**.server1.queueLength.record = true
**.server1.serviceTime.record = true
**.server2.serviceTime.record = true
**.server3.serviceTime.record = true
""")
        for s1_exp_param in s1_exponential_params:
            # Create a unique name for the configuration based on the values of the parameters
            config_name = f"lambda_{lambda_val}-switchProb_{switch_prob_val}-s1ExpMean_{s1_exp_param['name']}"
            
            # Create the directory for the simulation results
            result_dir = f"results/{config_name}"
            #os.makedirs(result_dir, exist_ok=True)
            
            # Generate the configuration file for the current combination of parameters
            with open(f"HeavyTrafficLimits_{config_name}.ini", "w") as f:
                f.write(f"""[General]
network = HeavyTrafficLimits
sim-time-limit = 100000s
repeat = {repeat}
replication-label = {replication_label}${{repetition}}
result-dir = {result_dir}
warmup-period = 30000s
**.source.lambda = {lambda_val}
**.router.switchProbability = {switch_prob_val}
**.server1.serviceTime = exponential(0.33s)
**.server2.serviceTime = exponential(0.33s)
**.server3.serviceTime = exponential(0.33s)
**.server1.crashTime = {server_crash_times["server1"]}
**.server2.crashTime = {server_crash_times["server2"]}
**.server3.crashTime = {server_crash_times["server3"]}
# imposta il tempo di servizio esponenziale per la coda S1 del JobNetwork.
**.S1.serviceTime = exponential({s1_exp_param["mean"]})
**.server1.queueLength.record = true
**.server1.serviceTime.record = true
**.server2.serviceTime.record = true
**.server3.serviceTime.record = true
""")