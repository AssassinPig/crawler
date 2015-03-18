from master import Master
import settings
if __name__ == '__main__':
    start_urls = [ 'http://www.woaidu.org/' ]
    master = Master(settings=settings, start_urls=start_urls)
    master.run()
