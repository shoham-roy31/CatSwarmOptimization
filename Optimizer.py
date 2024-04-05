import os
import time
import matplotlib.pyplot as plt
from configs import hyperparameters as h
from CatSwarms import Cats
from CostFunction import CostFunction

class Optimize:
  def __init__(self,y,a,b):
    self.CF = CostFunction(y,a,b)
    self.cso = Cats(h['n_cats'],h['m_dims'],cost_function = self.CF,MR=h['MR'],
    SRD=h['SRD'],SMP=h['SMP'],positions=h['positions'],r=h['r'],c=h['c'])
  
  def __call__(self,threshold = 0.1,verbose = True,
  render_plot = True,save_plot = True) -> tuple:
    self.cso.Initialize(self.cso.position_map)
    fittest = []
    sensitivity = self.CF.resultant(self.cso.Xbest)
    iterations = 0
    while True:
      self.cso.Optimize()
      sensitivity = self.CF.resultant(self.cso.Xbest)
      fittest.append(self.cso.Xbest)
      if threshold > sensitivity:
        break
      if iterations % 10 == 0 and verbose:
        print("Fitness Score: ",self.cso.n_cats_fitness)
      iterations += 1
    if render_plot:
      self.Plot(fittest,save_plot)
    return self.cso.Xbest,iterations  # Approximated Value, Iterations

  def Plot(self,fittest,save_plot):
    Y_ = [self.CF.J(x) for x in fittest]
    plt.figure(figsize=(12,6))
    plt.plot(fittest,label='Estimations')
    plt.plot(Y_,label='Approximations')
    plt.xlabel("Iterations")
    plt.legend()
    plt.title("Convergence Graph")
    if save_plot:
      path = "CSO_Performance_" + str(time.strftime("%a, %d-%m-%Y",time.gmtime()))
      if not os.path.exists(path):
        os.mkdir(path)
    
      path = path+"/"+str(time.strftime("%H_%M_%S",time.gmtime()))
      os.mkdir(path)

    
      plt.savefig(path+'/plot.png')
