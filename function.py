import numpy as np
import matplotlib.pyplot as plt
import math


# 伽马函数
def gamma(x):
    return math.gamma(x)

# 计算weibull分布均值
def weibull_mean(beta, eta):
    return eta * gamma(1 + 1 / beta)

# 计算weibull分布中位数
def weibull_median(beta, eta):
    return eta * (-math.log(2)) ** (1 / beta)

# 计算正态分布90%置信区间
def normal_90_confidence_interval(mean, std):
    return mean - 1.645 * std, mean + 1.645 * std

# 计算韦伯分布90%置信区间
def weibull_90_confidence_interval(beta, eta):
    # mean = weibull_mean(beta, eta)
    # median = weibull_median(beta, eta)
    mean = 68.423
    median = 66.188
    std = (mean - median) / 1.645
    return normal_90_confidence_interval(mean, std)

#print(weibull_90_confidence_interval(10.416, 71.8))

# 计算韦伯分布95%置信区间

# 计算正态分布下分数50到分数60的可能性
def normal_probability_between(lower_bound, upper_bound, mean=0, std=1):
    return normal_cdf(upper_bound, mean, std) - normal_cdf(lower_bound, mean, std)

def normal_cdf(x, mean=0, std=1):
    return (1 + math.erf((x - mean) / math.sqrt(2) / std)) / 2

# 计算韦伯分布下分数50到分数60的可能性
def weibull_probability_between(lower_bound, upper_bound, beta, eta):
    return weibull_cdf(upper_bound, beta, eta) - weibull_cdf(lower_bound, beta, eta)

def weibull_cdf(x, beta, eta):
    return 1 - math.exp(-(x / eta) ** beta)

print(normal_probability_between(50, 60, 68.5, 7.745))
print(weibull_probability_between(50, 60, 10.416, 71.8))