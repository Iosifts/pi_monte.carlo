
import multiprocessing,random
from multiprocessing import Pool


#caculate the number of points in the unit circle
#out of n points
def points_in_square_n_cicle(n):
    
    count = 0
    for i in range(n):
        x=random.random()
        y=random.random()
        
        # τα σημεία τα θέλω μέσα στον μοναδιαίο κύκλο
        if x**2 + y**2 <= 1:
            count+=1
        
    #return
    return count


if __name__=='__main__':
    
    p = multiprocessing.cpu_count()

    print('Τα CPU που έχουμε είναι', p)

    
    n = 10**8 #το δείγμα
    # n = 10**9
    #n = 10**2


    pi_parts=[] #καθε διεργασία μοιράζεται n/p σημεία

    for i in range(p):
        pi_parts.append(n//p)


    #Φτιαχνω worker pool (The Pool class represents a pool of worker processes.
    #  It has methods which allows tasks to be offloaded to the worker processes 
    # in a few different ways.)


    #pool = Pool(processes=8)  
    #pool = Pool(processes=4)  


    pool = Pool(processes=p)  #χρησιμοποιώ και τους 12 logical processors που εχει το πσ μ


    # τώρα κάνουμε mapping across processes
    s_points=pool.map(points_in_square_n_cicle, pi_parts)

    pi_tetarta=sum(s_points)/(n*1.0)

    print("Estimated Pi:: ", 4*pi_tetarta)  
