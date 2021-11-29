import os
import pandas as pd

# replace with path to your directory
directoryR = "/Users/Rebecca 1/Desktop/Jam_Sessions/data/reactive-gases-grids/"
reactive_data = []
for file in os.listdir(directoryR):
    if file.endswith(".txt"):
        files = pd.read_csv(directoryR + file, skiprows=12,
                            names=["long", "lat", "value"])
        files['filename'] = os.path.basename(file)

        reactive_data.append(files)
reactive_data = pd.concat(reactive_data)
print(reactive_data)
# replace with path to your directory
#reactive_data.to_csv("/Users/Rebecca 1/Desktop/Jam_Sessions/data/combinedReactiveData.csv", index = False)

# replace with path to your directory
directoryS = "/Users/Rebecca 1/Desktop/Jam_Sessions/data/so2-grids/"
so2_data = []
for file in os.listdir(directoryS):
    if file.endswith("0"):
        files = pd.read_csv(directoryS + file, skiprows=3, sep='\t',
                            names=["so2_emissions"]) # also tried read_table
        files['filename'] = os.path.basename(file)

        so2_data.append(files)
so2_data = pd.concat(so2_data)
print(so2_data)
