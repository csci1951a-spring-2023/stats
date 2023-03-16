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
        Out of 105 bottles, 5 of them did not have available data, 35 had 150ml, 25 had 135ml, and 40 had 160ml. How likely is their 
        machine calibrated wrongly, given these results?.
    Input:
        - a Pandas dataframe (written in the stencil for you)
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    
    # Here is the parsed data for this scenario!
    data = [150]*35 + [135]*25 + [160]*40 + [None]*5
    df = pd.DataFrame(data, columns=['Volume'])

    # TODO:
    # Construct all necessary variables needed to make the call to the right function
    # in stats_tests (there may or may not require another variable here)

    # On line 34 our data has None values in it that should not be there when
    # we do our statistical test
    # A good habit is to clean that values out before using them later in the code
    # Clean out these None values using drop_incomplete_rows() from the imports

   

    # TODO: Return tstats and pvalue


def scenario_two():
    """
    Scenario:
        - We measure the grams of protein in two different brands of energy bars by sampling 
        from 10 bars in each brand. Brand A had 12, 14, 13, 11, 12, 12, 11, 14, 17, 10 grams in 
        each of their bars, whereas Brand B had 10, 10, 10, 12, 18, 18, 19, 12, 11, 10 grams each. 
        How likely are the average grams of protein in the two brands different from one another?
    Input:
        - dataset: A Pandas DataFrame (written in the stencil for you)
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Use the given data and construct any necessary variables to make the call to the right
    # function in stats_tests.py (Note: another variable may not be required!)
    
   
    # TODO: Return tstats and pvalue


def scenario_three():
    """
    Scenario:
        - A study wants to find out if there is a correlation between someone being exposed 
        to Disease X and getting the disease or vice versa. They record 15 exposed participants 
        having the disease, 5 unexposed participants having the disease, 20 unexposed not having the disease, 
        and 7 exposed to the disease not getting it.
    Input:
        - dataset: A Pandas DataFrame (written in the stencil for you)
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Use the given data and construct any  necessary variables to make the call to the right
    # function in stats_tests.py (Note: another variable may not be required!)

   
    # TODO: Return tstats and pvalue
    


def scenario_four():
    """
    Scenario:
        - A hospital wants to check if their treatment was successful in changing cholesterol levels for their 
        patients. They tested the 10 patients cholesterol levels in 2010 and then retested the same patients in 2011. 
        In 2010 the 10 patients cholesterol levels were 110mg, 115mg, 150mg, 120mg, 99mg, 132mg, 182mg, 183mg, 89mg, and 91mg.
        In 2011 the same 10 patients cholesterol levels were 84mg, 88mg, 88mg, 89mg, 90mg, 90mg, 91mg, 90mg, 90mg, 90mg.
    Input:
        - dataset: A Pandas DataFrame (written in the stencil for you)
    Output:
        - tstats: Test statistics (float)
        - p-value: P-value (float)
    """
    # TODO: Construct the necessary variables to make the call to the right
    # function in stats_tests.py (Note: another variable may not be required!)

    
    # TODO: Return tstats and pvalue


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
