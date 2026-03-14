from modeller import *

log.verbose()
env = Environ()

env.libs.topology.read(file='$(LIB)/top_heav.lib')

aln = Alignment(env)

# read template alignment
aln.append(file='templates.ali', align_codes='all')

aln_block = len(aln)

# append WT sequence
aln.append(file='protein.pir', align_codes='PROTEIN')

# pairwise alignment
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

aln.write(file='wt-mult.ali', alignment_format='PIR')
aln.write(file='wt-mult.pap', alignment_format='PAP')