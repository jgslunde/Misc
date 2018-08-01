import itertools
import scipy.special
import numpy as np
from sympy.utilities.iterables import multiset_permutations

NO_cand = 3
NO_voters = 3

NO_unq_ballots = np.math.factorial(NO_cand)
NO_total_comb = NO_unq_ballots*NO_voters
#NO_total_comb = scipy.special.comb(NO_unq_ballots, NO_voters, exact=True)

# Generating set of unique ballots.
example_ballot = np.arange(NO_cand)
permutation_set = multiset_permutations(example_ballot)
unq_ballots = np.zeros( (NO_unq_ballots, NO_cand) )
for i, ballot in enumerate(permutation_set):
    unq_ballots[i,:] = ballot

# Generating set of all possible ballot combinations
ballots = np.zeros((NO_total_comb, NO_voters, NO_cand))
permutation_set2 = itertools.combinations(unq_ballots, NO_voters)
for i, x in enumerate(permutation_set2):
    ballots[i,:,:] = x

filename = ("ballots_cand=%d_voters=%d.npy" % (NO_cand, NO_voters))
print("Total of %d possible ballot combinations" % NO_total_comb)
print("Saving file %s" % filename)
np.save(filename, ballots)