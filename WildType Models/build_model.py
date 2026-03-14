from modeller import *
from modeller.automodel import *

env = Environ()

a = AutoModel(env,
              alnfile='wt-mult.ali',
              knowns=('9U9VR','3KJ6A','9L8LR'),
              sequence='PROTEIN')

a.starting_model = 1
a.ending_model = 3

a.make()