from modeller import *

log.verbose()
env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')

aln = Alignment(env)

aln.append(file='templates.ali', align_codes='all')

aln_block = len(aln)

aln.append(file='mutated_protien.pir', align_codes='MUTANT')

aln.salign(output='',
           max_gap_length=20,
           gap_function=True,
           alignment_type='PAIRWISE',
           align_block=aln_block,
           feature_weights=(1.,0.,0.,0.,0.,0.),
           overhang=0,
           gap_penalties_1d=(-450,0),
           gap_penalties_2d=(0.35,1.2,0.9,1.2,0.6,8.6,1.2,0.,0.),
           similarity_flag=True)

aln.write(file='mutant-mult.ali', alignment_format='PIR')
aln.write(file='mutant-mult.pap', alignment_format='PAP')