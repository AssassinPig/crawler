from worker import Worker
import settings
from strategy import Strategy
from multiprocessing import Pool, Process

def generate_process(i):
    start_urls = []
    strategy = Strategy(Strategy.BSF)
    worker = Worker(start_urls=start_urls, strategy=strategy, settings=settings)
    worker.run()

if __name__ == '__main__':
    #i = settings.WORKER_NUM 
    #if i is None:
    #    i = 5
    #p = Pool(5)
    #params = range(5)

    #debug
    p = Process(target=generate_process, args=(1,)) 
    p.start()
    p.join()
