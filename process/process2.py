from multiprocessing import process
import  os

def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__ == '__main__':
    print  "parent process %s." % os.getpid()
    p = process.Process(target=run_proc, args=('test',))
    print "process will start"
    p.start()
    p.join()
    pass

