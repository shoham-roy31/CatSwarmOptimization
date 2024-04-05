import numpy as np


class CostFunction:
  def __init__(self,y,a,b):

    '''One can design their custom cost function
    which must be have single unknown parameter'''
    self.y = y
    self.a = a
    self.b = b

  def J(self,x):
    '''Designable Cost Function'''

    y_ = (np.cos(self.a**2)+ x)*np.cos(self.b)
    return y_

  def eval(self,x):

    '''Continous Evaluation of Fitness Scores'''
    y_ = self.J(x)
    fitness_score = 1/abs(self.y-y_)
    return fitness_score

  def resultant(self,fitness_val):
    y_ = self.J(fitness_val)
    return abs(self.y-y_)