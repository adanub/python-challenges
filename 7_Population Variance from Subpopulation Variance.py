import numpy as np

def pop_var_from_subpop_var(groups):
    pop_sum = 0 #sum of population
    pop_count = 0 #number of population values added to get the sum

    for subpop in groups:
        pop_sum += np.sum(subpop)
        pop_count += len(subpop)

    mean = pop_sum / pop_count
    sq_diff_sum = 0 #sum of squared difference of each sub population

    for subpop in groups:
        sq_diff = np.square(subpop - mean) #squared difference
        sq_diff_sum += np.sum(sq_diff)
        
    pop_var = sq_diff_sum / pop_count
    return pop_var

groups = [np.array([1,2,3,4]), np.array([5,6])]
print(pop_var_from_subpop_var(groups))
# 2.9166666666666665