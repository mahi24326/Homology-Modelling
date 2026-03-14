# Multiple structure alignment

from modeller import *

log.verbose()
env = Environ()

# location of pdb files
env.io.atom_files_directory = ['.']

aln = Alignment(env)

# templates
for (code, chain) in (('9U9V', 'R'), ('3KJ6', 'A'), ('9L8L', 'R')):
    mdl = Model(env, file=code,
                model_segment=('FIRST:'+chain, 'LAST:'+chain))
    aln.append_model(mdl,
                     atom_files=code,
                     align_codes=code+chain)

# SALIGN
for (weights, write_fit, whole) in (((1.,0.,0.,0.,1.,0.),False,True),
                                    ((1.,0.5,1.,1.,1.,0.),False,True),
                                    ((1.,1.,1.,1.,1.,0.),True,False)):

    aln.salign(rms_cutoff=3.5,
               normalize_pp_scores=False,
               rr_file='$(LIB)/as1.sim.mat',
               overhang=30,
               gap_penalties_1d=(-450,-50),
               gap_penalties_3d=(0,3),
               gap_gap_score=0,
               gap_residue_score=0,
               dendrogram_file='templates.tree',
               alignment_type='tree',
               feature_weights=weights,
               improve_alignment=True,
               fit=True,
               write_fit=write_fit,
               write_whole_pdb=whole,
               output='ALIGNMENT QUALITY')

aln.write(file='templates.pap', alignment_format='PAP')
aln.write(file='templates.ali', alignment_format='PIR')