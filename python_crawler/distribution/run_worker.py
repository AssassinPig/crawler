from worker import Worker
import settings
from strategy import Strategy

if __name__ == '__main__':
    start_urls = []
    strategy = Strategy(Strategy.BSF)
    worker = Worker(start_urls=start_urls, strategy=strategy, settings=settings)
    worker.run()
