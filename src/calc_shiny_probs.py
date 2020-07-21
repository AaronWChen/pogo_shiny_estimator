# This Python script contains functions necessary to compute the probabilities 
# for finding a shiny Pokemon

# Author: Aaron Washington Chen
# Contact Info: 
#   Github: https://github.com/AaronWChen

import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
import seaborn as sns
import math
import bokeh

def expected_binom_shinies(appearances, shiny_rate=1/450):
    """This function gives the number of expected shiny Pokemon appearances for 
    a user-provided number of appearances of all Pokemon

    The default shiny rate is empirically recorded by Silph Road:
    https://thesilphroad.com/science/pokemon-go-deducing-shiny-rate/"""

    all_appearances = [1 for _ in range(1, appearances+1, 1)]
    weighted_P = np.multiply(shiny_rate, all_appearances)
    return np.sum(weighted_P)

def prob_poisson_shinies(k, appearances=140):
    """This function takes in the number of appearances (with a default of my daily rate of 140) and the number of shinies you've gotten/want to get and gives back the probability assuming a Poisson distribution.
    
    For the expected value in the Poisson equation, though, this uses the expected value for a Binomial Distribution.
    """

    exp_val = expected_shinies(appearances)
    return exp_val**k * np.exp(-exp_val) / math.factorial(k)

def prob_binom_shinies(k, appearances=140, shiny_rate=1/450):
    """This function takes in the number of appearances (with a default of my daily rate of 140) and the number of shinies you've gotten/want to get and gives back the probability assuming a binomial distribution"""
    coef_denom = math.factorial(k) * math.factorial(appearances-k)
    coef = math.factorial(appearances) / coef_denom
    return coef * shiny_rate**k * (1-shiny_rate)**(appearances-k)