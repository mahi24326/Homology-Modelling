from modeller import *
from modeller.scripts import complete_pdb

# Initialize the Modeller environment
env = Environ()

# Set up the topology and parameter libraries needed for DOPE
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# --- CONFIGURATION ---
pdb_filename = 'MUTANT.B99990003.pdb' 
profile_filename = 'output6.profile'
# ---------------------

# Read the PDB file and build the topology
print("Reading and preparing " + pdb_filename + "...")
mdl = complete_pdb(env, pdb_filename)

# Select all atoms in the model
atmsel = Selection(mdl)

# Calculate the DOPE energy profile
print("Calculating DOPE profile...")
atmsel.assess_dope(output='ENERGY_PROFILE NO_REPORT', 
                   file=profile_filename,
                   normalize_profile=True, 
                   smoothing_window=15)
                   
print("Success! Energy profile saved to " + profile_filename)