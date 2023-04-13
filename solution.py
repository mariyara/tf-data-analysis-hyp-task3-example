import pandas as pd
import numpy as np


chat_id = 558620654 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p_value = ttest_ind(x, y, alternative="greater").pvalue
    return p_value < 0.09
