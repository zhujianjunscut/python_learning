from multiprocessing import process
import  os,time,random
from multiprocessing import pool

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())
    pass

def long_time_task(name):
    print  "run task %s (%s)....%s" % (name, os.getpid(),os.getcwd())
    start  = time.time()
    time.sleep((random.random() *3))
    end = time.time()
    print "task %s runs %0.2f seconds" % (name,(end  - start))
    pass


if __name__ == '__main__':
    # print  "parent process %s." % os.getpid()
    # p = process.Process(target=run_proc, args=('test',))
    # print "process will start"
    # p.start()
    # p.join()if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = pool.Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    pass

