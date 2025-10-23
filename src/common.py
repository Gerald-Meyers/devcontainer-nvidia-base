from DecisionRegion import classification_plots

from numpy import (
    ndarray, array, asarray,
    genfromtxt, unique, vectorize,
    concatenate, arange,
    vectorize, sum, any, all, where,
    argmax, ones, max, min, nan, NAN, log10,
    float32
    )

from pandas import (
    DataFrame, read_csv, set_option, to_numeric
    )

from pathlib import Path

from re import (
    compile, search,
    )

from sklearn import (
    preprocessing, impute, discriminant_analysis, decomposition, model_selection,
    svm, tree, neighbors, linear_model, ensemble,
    pipeline, metrics,
    )

from tabulate import tabulate

from time import time

from warnings import filterwarnings

from functools import wraps