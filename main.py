import numpy as np

def calculate(input):
  if len(input) != 9:
    raise ErrorValue ("list must contain nine numbers.")

    x = np.array(input).reshape(3,3)
    print(x)
    print(x.mean(0), x.mean(1), x.mean())

    cal = dict()
    cal['mean'] = [x.mean(0).tolist(), x.mean(1).tolist(), x.mean()]
    cal['variance'] = [x.var(0).tolist(), x.var(1).tolist(), x.var()]
    cal['stadard deviation'] = [x.std(0).tolist(), x.std(1).tolist(), x.std()]
    cal['max'] = [x.max(0).tolist(), x.max(1).tolist(), x.max()]
    cal['min'] = [x.min(0).tolist(), x.min(1).tolist(), x.min()]
    cal['sum'] = [x.sum(0).tolist(), x.sum(1).tolist(), x.sum()]
    return cal

print(calculate([0,1,2,3,4,5,6,7,8]))
