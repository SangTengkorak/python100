# SangTengkorak
# May 22 2021

import platform as plt

def check_feature(feature, string):
    if feature in string.lower():
        return True
    else:
        return False

def get_value_from_string(key, string):
    value = "NONE"
    for line in string.split("\n"):
        if key in line:
            value = line.split(":")[1].strip()
    return value

cpu_features = []
with open('/proc/cpuinfo') as cpus:
    cpu_data = cpus.read()
    num_of_cpus = cpu_data.count("processor")
    cpu_features.append("Number of Processors: {0}".format(num_of_cpus))
    one_processor_data = cpu_data.split("processor")[1]
    print(one_processor_data)
    if check_feature("vmx", one_processor_data):
        cpu_features.append("CPU Vitrualization: enabled")
    if check_feature("cpu_meltdown", one_processor_data):
        cpu_features.append("Known Bugs: CPU Meltdown ")
    model_name = get_value_from_string("model name", one_processor_data)
    cpu_features.append("Model Name: {0}".format(model_name))

    cpu_mhz = get_value_from_string("cpu MHz", one_processor_data)
    cpu_features.append("CPU MHz: {0}".format((cpu_mhz)))

memory_features = []
with open('/proc/meminfo') as memory:
    memory_data = memory.read()
    total_memory = int(get_value_from_string("MemTotal", memory_data).replace(" kB",""))
    free_memory = int(get_value_from_string("MemFree", memory_data).replace(" kB",""))
    swap_memory = int(get_value_from_string("SwapTotal", memory_data).replace(" kB",""))
    total_memory_in_gb = "Total memory in GB: {0}".format((total_memory)/1024000)
    free_memory_in_gb = "Free memory in GB: {0}".format((free_memory)/1024000)
    swap_memory_in_gb = "SWAP memory in GB: {0}".format((swap_memory)/1024000)
    memory_features = [total_memory_in_gb, free_memory_in_gb, swap_memory_in_gb]

print("============System Information============")

print("""
System Type: {0}
Hostname: {1}
Kernel Version: {2}
System Version: {3}
Machine Architecture: {4}
Python Version" {5}
""".format(plt.system(),
plt.uname()[1],
plt.uname()[2],
plt.version(),
plt.machine(),
plt.python_version()))

print("============CPU Information============")
print("\n".join(cpu_features))

print("============Memory Information============")
print("\n".join(memory_features))
