'''
Created on Feb 16, 2014

@author: phcostello
'''

from math import exp, sqrt
import numpy as np
from VariateGenerator import Antithetic, NormalGenerator

class GeneratorGBM(object):
    '''
    Generates a path from a multi dimensional GBM
    Uses draws from analytic solution to GBM rather than incremental stepping
    
    Inputs
    market_params - spot, rate, covariance matrix
    bm_construction - how do we contruct underlying brownian motion
    
    Members = generator, this generates
    '''


    def __init__(self, market_params, path_construction = 'incremental'):
        '''
        
        '''
    
        self.market_params = market_params #Should clean this up
        self.spot = market_params['spot']
        self.rate = market_params['rate']
        self.vol = market_params['vol']
        self.generator = NormalGenerator()
        self.path_construction = path_construction
        
        
    
    def sim_setup(self,times):
        
        '''
        Setup of variables that are constant for each path in sim
        Note that this is where setup path generation method
        Concrete generation methods implemented as "do_one_path_*"
        '''
        #Contruct log of drifts up to random draw
        
        self.times = times
        self.drifts = [ self.rate*time - 0.5 * self.vol*self.vol*time for time in times]
        self.num_times = len(times)
        
        #Setup path generating function
        self.path_generation_method = getattr(self, "do_one_path_{}".format(self.path_construction))
    
    def do_one_path(self):
        """
        This only works if path_generation_method has been set
        """
        return self.path_generation_method()
    
    def do_one_path_incremental(self):
        
        """
        Currently set to use analytic solution to GBM
        Uses incremental build of brownian motion
        """
        
        randoms = self.generator.get_variates(0,1,self.num_times)
        
        #Construct brownian motion path at times
        bm_path = []
        bm_t = 0
        
        #Incremental BM generation
        times_aug = [0]+times
        time_diffs = [ times_aug[i+1] - times_aug[i] for i in range(0,len(times))]
        
        for i in range(0, self.num_times):
            bm_t += self.vol*sqrt(self.times[i])*randoms[i]
            bm_path += [bm_t]
        
        #Construct GBM path at times
        #remember to exp as have gen logs of paths
        path = [ exp(self.drifts[i] + bm_path[i]) for i in range(0,self.num_times)]
        return path
    
    def do_one_path_brownian_bridge(self):
        
        """
        Currently Depends on numpy as using cholesky
        Can drop when I figure out dist for brownian bridge
        
        Currently set to use analytic solution to GBM
        Does brownian bridge construction of Brownian motion
        
        To do brownian bridge you:
        
        Rearrange indexes by always choosing gap where variance will be largest
        Only implemented where index gap is largest , e.g, (1,2,..,10) => (10,5,2,7,3,8,1,4,6,9]
        This is implemented in _"_bb_indexes" function below
        
        Generate BM path by generating draw for reindex incrementally, e.g for #times = 10
        
        Use brownian bridge formula http://en.wikipedia.org/wiki/Brownian_bridge
        ie if B(t_1)=a and B(t_2)=b then
        
        Look up Shrev
        
        Alternativel, you can:
        
        1. take incremental covariance matrix, rearrange indexes
        2. cov*_ij = cov_bb(i)bb(j)
        3. Cholesky facotrize cov* => A        
        4. Build incremental path using A
        5. Rearrange path back into using reverse index 
        
        """
        
        #Get randoms for draw
        randoms = self.generator.get_variates(0,1,self.num_times)
        times = self.times
        num_times = self.num_times
#         print "num_times", num_times
        
        #Construct covariance matrix for BM we want
        cov_rows = [ [min(times[i],times[j]) for j in range(0,num_times)] for i in range(0,num_times)]
        
        cov = np.matrix(cov_rows)
#         print "cov", cov
        #Rearrange  as per Brownian Bridge indexing
#         print "num times", num_times
        reind_bb = self.__bb_indexes(times)
#         print "reind vec", reind_bb
        cov_bb = cov[reind_bb,:][:,reind_bb]
#         print "cov_bb ", cov_bb
        
        #Contruct Cholesky decomp
        Abb = np.linalg.cholesky(cov_bb)
        
#         cov2 = Abb.dot(np.transpose(Abb))
        
        
        
        #Construct BM path in BB indexing
        print "Shape randoms", np.matrix(randoms).T.shape
        print "shape Abb", Abb.shape
        bm_path_bbind = np.matrix(Abb).dot(np.matrix(randoms).T)
        print "shape bmm_path", bm_path_bbind.shape
        
        #Construct matrix to reverse bb_indexing
        idm = np.identity(num_times)
        idm_ri = idm[reind_bb,:]
        idm_inv = np.linalg.inv(idm_ri)
        
        #Rearrange path back to original indexing
        bm_path = idm_inv.dot(bm_path_bbind)
        
        
#         print "cov2 ", idm_inv.dot(cov2.dot(np.transpose(idm_inv)))
        
#       #Construct order of reorder path generation
#         index = [i for i in range(0, self.num_times)]
#         bb_reind = self.__bb_indexes(index)
#         rev_reind = None
#         
#         #Construct cov matrix
#         rows = [ [min(i,j) for j in range(0,self.num_times)] for i in self.num_times]
#         
#         #Construct brownian motion path at times
#         bm_path = [0]*self.num_times
#         bm_t = 0
#         last_bbindex = 0
#         
#         
#         for i in range(0, self.num_times):
#             
#             reind = bb_reind[i]
#             if last_bbindex < reind:
#                 direction = 1.0
#                 
#             else:
#                 direction = - 1.0  
#                 
#             difftime = direction*(times[reind] -times[last_bbindex]) 
#             bm_t += direction*self.vol*sqrt(difftime)*randoms[i]
#             bm_path[reind] = bm_t
#             last_bbindex = reind
            
        #Construct GBM path at times
        #remember to exp as have gen logs of paths
        path2 = [ self.spot*exp(self.drifts[i] + bm_path[i]) for i in range(0,self.num_times)]
        return path2
    
    def __bb_indexes(self, times, index0=True):
        
        """
        Utility function for reordering brownian bridge
        index0 flag sets whether you want the indexes in the reindex starting at 0
        """
        
        times = list(times)
        bb_indexes = [0,len(times)]
        for j in range(0,len(times)-1):
            
            stmp = sorted(bb_indexes)
            #get interval sizes
            diffs = [stmp[i+1]-stmp[i] for i in range(0,len(stmp)-1)]
            #get max interval width
            max_int_width = max(diffs)
            #get left hand index of left interval
            lindex_ofmax_int = diffs.index(max_int_width)
            next_index = stmp[lindex_ofmax_int] + max_int_width/2
            bb_indexes+=[next_index]
        
#         print "BB_INDEX", bb_indexes
        
        if index0:
            bb_indexes_tmp = [ind - 1 for ind in bb_indexes]
            bb_indexes = bb_indexes_tmp
        
        return bb_indexes[1:]
    
class GeneratorStepper(object):
    '''
    We want to make a path generator that evolves by stepping of an SD
    It will generate an n-dimensional path where the paths have
    
    Inputs
    SDE - sde_drift, sde_vol
    Random_generator - has generate n variates
    Initial params - e.g, initial_spots, 
    Deterministic SDE_params - e.g, possibley rates, vols, cov
    
    
    '''

    

    def __init__(self, market_params):
        '''
        
        '''
    
        self.market_params = market_params
        self.spots = market_params['spots']
        self.rates = market_params['rates']
        self.cov = market_params['cov']
        self.generator = NormalGenerator(normal)
        
    
    def sim_setup(self,times):
        
        aug_times = [0.0]+times
        self.time_diffs = [ aug_times[i] - aug_times[i-1] for i in range(1,len(aug_times))]
        #Contruct times up to random draw
        self.drifts = [ exp(self.rate*td - 0.5 * self.vol*self.vol*td) for td in self.time_diffs]
        
        
    def do_one_path(self):
        
        """
        Currently set to use analytic solution to GBM
        Change to be a dispatcher
        """
        
        randoms = self.generator.get_variates(0,1,len(self.time_diffs))
        
        path = []
        prev_spot = self.spot
        
        for i in range(0, len(self.time_diffs)):
            next_spot = prev_spot*self.drifts[i] * exp(self.vol*sqrt(self.time_diffs[i])*randoms[i])
            path += [next_spot]
            prev_spot = next_spot
        
        
        return path
    
if __name__ == '__main__':
    
    import numpy as np
    import matplotlib.pyplot as plt
    spot = 100.
    rate = 0.05
    vol = 0.001
#     times = list(np.linspace(0.0, stop=1.0, num=4))
    times = list(np.linspace(0.0, stop=1.0, num=100))
    times = times[1:]
    print times
#     times = [1.]
    
    market_params = {'spot':spot, 'rate':rate, 'vol':vol}
    
    bgmgen = GeneratorGBM(market_params, "brownian_bridge")
#     bgmgen = GeneratorGBM(market_params)
    bgmgen.sim_setup(times)
    #Change random generator
    generator = NormalGenerator() #Make generator out of np normal generator
    athetic = Antithetic(generator)
    
    bgmgen.generator = athetic 
    print athetic.get_variates(0, 1, 3)
    print athetic.get_variates(0, 1, 3)
    
    path = bgmgen.do_one_path()
    print len(path)
    print list(times)
    plt.plot(times,path)
    plt.show()
    
#     vals = [bgmgen.do_one_path() for i in range(0,3)]
    
#     print vals
#     vals2 = [ v[0] for v in vals]
#     print vals2
#     plt.hist(vals2,50)
#     plt.show()
#     
#     print vals
    
    
    
        