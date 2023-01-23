import pandas as pd
import numpy as np
import argparse, os, random
from util import timestr_to_seconds, drop_incomplete_rows, RANDOM_SEED
from stats_tests import one_sample_ttest, two_sample_ttest, paired_ttest,\
                        chisquared_independence_test

##### STENCIL #####

def parse_args():
    parser = argparse.ArgumentParser(description="stats test runner")
    parser.add_argument('-s', help="scenario: ['one', 'two', 'three', 'four', 'five', 'all']")
    return parser.parse_args()


##### STUDENT WORK #####

def scenario_one():
    """
    Scenario:
        - A factory calibrates their milk bottle-filling machine to 150ml each and wants to 
        ensure there is no significant deviation in the volume of milk in the bottles they produce. 
        Out of 100 bottles, 35 had 150ml, 25 had 135ml, and 40 had 160ml. How likely is their 
        machine calibrated wrongly, given these results?.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    #=#=#=#=#=#=#=#=#=# Solution: two sample t-test #=#=#=#=#=#=#=#=#=#
    
    # Here is the parsed data for this scenario!
    

    # TODO:
    # Construct all necessary variables needed to make the call to the right function
    # in stats_tests (there may or may not require another variable here)

    # On line 34 our data has None values in it that should not be there when
    # we do our statistical test
    # A good habit is to clean that values out before using them later in the code
    # Clean out these None values using drop_incomplete_rows() from the imports

    

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_two():
    """
    Scenario:
        - The mean height of U.S. adults ages 20 and older is about 66.5
        inches (69.3 inches for males, 63.8 inches for females). In our
        sample data, we have a sample of 435 college students from a 
        single college.  We want to determine whether the mean height of 
        students at this college is significantly different than the mean 
        height of U.S. adults ages 20 and older.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    #=#=#=#=#=#=#=#=#=# Solution: one sample t-test #=#=#=#=#=#=#=#=#=#
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_three():
    """
    Scenario:
        - In the sample data, the students also reported their class quartile
        (1,2,3,4 for the first, second, third and fourth quartile), as well 
        as whether they live on campus. We want to test if there is a relationship 
        between one's class quartile and whether they live on campus.
        
        Note: Their class quartile is denoted in the dataset as "Rank".
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    #=#=#=#=#=#=#=#=#=# Solution: chi-squared #=#=#=#=#=#=#=#=#=#
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)
    

    # TODO: Return tstats and pvalue
    return tstats, pvalue


def scenario_four():
    """
    Scenario:
        - The students in the sample completed all 4 placement tests for
        four subject areas - English, Reading, Math, and Writing - when they
        enrolled in the university. The scores are out of 100 points, and are
        present in the dataset. We want to test if there was a significant 
        difference between the average of the English test scores and that of 
        the Math test scores.
    Input:
        - dataset: A Pandas DataFrame
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    #=#=#=#=#=#=#=#=#=# Solution: paired t-test #=#=#=#=#=#=#=#=#=#
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py. Don't forget to drop the rows that
    # contain empty/null values (in the columns that we care about)
    # before running the statistical test! :)

    
    
    # TODO: Return tstats and pvalue
    return tstats, pvalue


########## DO NOT CHANGE THIS PART OF THE CODE ##########

if __name__ == "__main__":
    random.seed()
    args = parse_args()
    scenario_type = args.s
    stype_to_fname = {
        "one": scenario_one,
        "two": scenario_two,
        "three": scenario_three,
        "four": scenario_four
    }

    # check the args input
    assert scenario_type in stype_to_fname or scenario_type == "all"

    # and then call all the function
    if scenario_type == "all":
        for num in ["one", "two", "three", "four"]:
            f = stype_to_fname[num]
            print(f"Running test for scenario {num}")
            stype_to_fname[num]()
            print("------------------------------")
    # if not, then just one function itself
    else:
        print(f"Running test for scenario {scenario_type}")
        stype_to_fname[scenario_type]()