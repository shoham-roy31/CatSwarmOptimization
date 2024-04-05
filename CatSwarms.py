import numpy as np


class Cats:
  def __init__(self,n_cats,m_dims,cost_function,MR=0.4,SRD=0.1,
               SMP=5,positions = 5,r=0.02,c=0.04):
    self.n_cats = n_cats
    self.m_dims = m_dims
    self.CF = cost_function
    self.MR = MR
    self.SRD = SRD
    self.positions = positions
    self.position_map = [[[[0,0] for k in range(self.m_dims)] for j\
                          in range(self.positions)] for i in range(self.n_cats)]
    self.velocity_map = self.position_map
    self.n_cats_fitness = []
    self.Xbest = None
    self.SMP = SMP
    self.SeekingModeMemory = []
    self.rc = r*c

  def Initialize(self,mapper):

    best_in_cats,best_in_cats_pos = [],[]

    for i in range(self.n_cats):
      best_in_dim,best_positions = [],[]
      for j in range(self.positions):
        eval_fitness,eval_positions = [],[]
        for k in range(self.m_dims):
          mapper[i][j][k][0] = np.random.randint(low=5,high=999)
          mapper[i][j][k][1] = np.random.randint(low=5,high=999)
          eval_fitness.append(self.CF.eval(mapper[i][j][k][0]))
          eval_positions.append(mapper[i][j][k][0])
        best_in_dim.append(eval_fitness[np.argmax(eval_fitness)])
        best_positions.append(eval_positions[np.argmax(eval_fitness)])
      best_in_cats.append(best_in_dim[np.argmax(best_in_dim)])
      best_in_cats_pos.append(best_positions[np.argmax(best_in_dim)])

    self.SeekingModeMemory = [np.random.randint(0,1) for _ \
                              in range(self.n_cats)]
    self.n_cats_fitness = best_in_cats
    self.Xbest = best_in_cats_pos[np.argmax(best_in_cats)]


  def SeekingMode(self,seeking_cats):

    best_among_cats,best_positions,choosed_position = [],[],[]
    for cat in seeking_cats:
      SPC = np.random.randint(low=0,high=1)
      if SPC:
        smp = self.SMP
      else:
        smp = self.SMP -1
      positions = np.random.choice(len(self.position_map[cat]),smp)
      choosed_position.append(positions.tolist())
      CDC = int(self.m_dims*np.random.uniform(0.5,1))
      choosed_dims = np.random.choice( positions,CDC).tolist()
      selected_dims = [self.position_map[cat][dim] for dim in choosed_dims ]
      fitness_score,position = self.execute(selected_dims)
      best_among_cats.append(fitness_score)
      best_positions.append(position)
    Fmax = best_among_cats[np.argmax(best_among_cats)]
    Fmin = best_among_cats[np.argmin(best_among_cats)]
    probability = [i/np.sum(best_among_cats) for i in best_among_cats]

    for cat in range(self.n_cats):
      for pos in range(self.positions):
        for dim in range(self.m_dims):
          self.position_map[cat][pos][dim][0] =\
           best_positions[np.argmax(best_among_cats)]  


    curr_best = best_positions[np.argmax(best_among_cats)]

    if self.CF.eval(curr_best) > self.CF.eval(self.Xbest):
      self.Xbest = curr_best
      self.n_cats_fitness = best_among_cats



  def execute(self,selected_dim):
    score,position=[],[]
    for dim in range(len(selected_dim)):
      local_best_score , local_best_position = [], []
    
      for inner_dim in range(len(selected_dim[0])):

        selected_dim[dim][inner_dim][0] = (1 + np.random.uniform(0,1)*self.SRD)*\
         (selected_dim[dim][inner_dim][0])
        

        local_best_score.append(self.CF.eval(selected_dim[dim][inner_dim][0]))
        local_best_position.append(selected_dim[dim][inner_dim][0])
      score.append(local_best_score[np.argmax(local_best_score)])
      position.append(local_best_position[np.argmax(local_best_score)])

    best = np.argmax(score)
    return score[best],position[best]


  def TracingMode(self,tracing_cats):
    for cat in tracing_cats:
      for pos in range(self.positions):
        for dim in range(self.m_dims):
          
          self.position_map[cat][pos][dim][1] += self.rc*\
           (self.Xbest-self.position_map[cat][pos][dim][0])
          self.position_map[cat][pos][dim][0] += self.position_map[cat][pos][dim][1]


  def Optimize(self):
    seggregate = int(self.MR*self.n_cats)
    seeking_cats = self.n_cats - seggregate
    tracing_cats = seggregate
    seeking_list = np.random.choice(self.n_cats,seeking_cats).tolist()
    tracing_list = []
    for cat in range(self.n_cats):
      if not cat in seeking_list:
        tracing_list.append(cat)
    self.SeekingMode(seeking_list)
    self.TracingMode(tracing_list)
