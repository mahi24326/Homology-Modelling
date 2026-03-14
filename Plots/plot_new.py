import matplotlib.pyplot as plt
import os

# Robust function to read the profile files and avoid empty plots
def read_profile(filename):
    residues = []
    energies = []
    if not os.path.exists(filename):
        print(f"⚠️ SKIPPED: Cannot find '{filename}'. Did you generate it yet?")
        return residues, energies
        
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if not line.startswith('#') and len(line.split()) >= 2:
                parts = line.split()
                try:
                    residues.append(int(parts[0]))  
                    energies.append(float(parts[-1])) 
                except ValueError:
                    continue
    print(f"✅ SUCCESS: Plotted '{filename}'")
    return residues, energies

# ==========================================
# GRAPH 1: Wild-Type Model vs WT Templates
# ==========================================
plt.figure(figsize=(12, 6))

# Plot the 3 WT templates using your exact filenames
x, y = read_profile('output1.profile')
if x: plt.plot(x, y, label='Template 1', color='green', linewidth=2)

x, y = read_profile('output2.profile') 
if x: plt.plot(x, y, label='Template 2', color='red', linewidth=2)

x, y = read_profile('output3.profile')
if x: plt.plot(x, y, label='Template 3', color='blue', linewidth=2)

# Plot your best WT model (Make sure to generate this file in Modeller!)
x, y = read_profile('output3.profile')
if x: plt.plot(x, y, label='Best WT Model', color='yellow', linewidth=1.5)

plt.title('DOPE Score Profile: Wild-Type Model vs Templates')
plt.xlabel('Residue Number')
plt.ylabel('DOPE Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# ==========================================
# GRAPH 2: Mutant Model vs MT Templates
# ==========================================
plt.figure(figsize=(12, 6))

# Plot the 3 MT templates using your exact filenames
x, y = read_profile('output4.profile')
if x: plt.plot(x, y, label='Template 1', color='green', linewidth=2)

x, y = read_profile('output5.profile') 
if x: plt.plot(x, y, label='Template 2', color='red', linewidth=2)

# 9U9V is used as a template for both WT and MT according to your table
x, y = read_profile('output6.profile')
if x: plt.plot(x, y, label='Template 3', color='blue', linewidth=2)

# Plot your best MT model (Make sure to generate this file in Modeller!)
x, y = read_profile('output5.profile')
if x: plt.plot(x, y, label='Best MT Model', color='yellow', linewidth=1.5)

plt.title('DOPE Score Profile: Mutant Model vs Templates')
plt.xlabel('Residue Number')
plt.ylabel('DOPE Score')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Show both graphs
plt.show()