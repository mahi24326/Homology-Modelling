from modeller import *
from modeller.scripts import complete_pdb

log.verbose()

env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

mdl = complete_pdb(env, 'MUTANT.B99990003.pdb')

s = Selection(mdl)

s.assess_dope(output='ENERGY_PROFILE NO_REPORT',
              file='wt1.profile',
              normalize_profile=True,
              smoothing_window=15)