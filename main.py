import timeit
from functions import sort0, sort1, sort2, sort3, sort4, sort5
import statistics as st
from scipy.stats import f_oneway, ttest_ind
import matplotlib.pyplot as plt
import json
import time

PRINT_ON_ITER = 50
OUTLIER_MARGIN = .33 # when - OUTLIER_MARGIN<z<OUTLIER_MARGIN is false, z is counted outlier. 
                    # Here, z is the standard Z-score.

# This is probably the first thing you want to modify
DATASET = [1, 2, 4, 5, 3, 2, 1, 9]
test0 = lambda : sort0(DATASET)
test1 = lambda : sort1(DATASET)
test2 = lambda : sort2(DATASET)
test3 = lambda : sort3(DATASET)
test4 = lambda : sort4(DATASET)
test5 = lambda : sort5(DATASET)
# And now go to the end of file. 

def sc_plot(l):
    """Draw a graph of timings taken for iterations"""

    mean = st.mean(l) # divide the data by its mean such to scale the data

    plt.scatter(list(range(len(l))), [x/mean for x in l])
    plt.show()

def compute(*funs: "List of functions to compare", 
        number: "The parameter for timeit" = 10000, 
        iterations: "The number of iterations to run" = 10):
    """Compute a statistical analysis and test whether each functions are equivalent.

    Each fun() in funs is called exactly (number*iterations) times.
    Each fun() should return outputs that have equaivalent JSON value.
    Each fun() should NOT take any parameter. If they need to, cover using a lambda expression.
    """

    # Read the print message below
    print("Ensuring that each function returns the same thing...")
    s = set([json.dumps(fun()) for fun in funs])
    try:
        assert(len(s) == 1)
        print(s)
    except Exception:
        print("All outputs not same :\\")
        [print(fun()) for fun in funs]
        time.sleep(5)


    print("Running comparison between {} functions".format(len(funs)))

    # Create empty Len(funs) x iterations resultset
    results = [[] for _ in funs]

    # THe main iteration
    for j in range(iterations):
        if j % PRINT_ON_ITER == 0:
            print("Iteration {}/{}".format(j+1, iterations)) 

        # These line of codes call fun() for each funs and appends the result of each fun 
        # on its respective resultset. index of fun() is the same as index used in resultset.
        [results[key].append(timeit.timeit(fun, number=number)/number) 
                for key,fun in enumerate(funs)]

    # Due to random events on the platform (Maybe OS, hardware), outliers on time occur. 
    # Try to remove outliers in each resultset using mean and standard deviation.
    for result in results:
        mean = st.mean(result)
        var = st.variance(result)
        result = [x for x in result if -OUTLIER_MARGIN < (x-mean)/var**.5 < OUTLIER_MARGIN]
        print("After removing outlier(s), {} dataset".format(len(result)))
        
    print("Iterations complete. ")

    # Uncomment the following line to see the time taken vs iteration graph for first dataset.
    # the data should follow a pattern like half bell curve
    # sc_plot(results[0])
    
    [print("for fun{}, mean: {} \t variance: {}".format(ind, st.mean(result), st.variance(result))) for ind, result in enumerate(results)]

    # Statistical F-Test. Usually, a p-value given by this test should be as large as possible to suggest that all the fun() passed as `funs` represent the same functions.
    print(f_oneway(*results) )

    print("Comparison complete".format())

# This is where you specify which tests you want to run.
# You don't always want to run all the tests at once 
# However, you can run any number of tests greater than 2 
# See the documentation for compute() to understand its parameters
compute(test0, test1, test2, test3, test4, number=100, iterations=2000)
