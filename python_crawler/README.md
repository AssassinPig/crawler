plan:
====
1. simple crawler: single process/single thread/single queue
2. extract strategy through parse interface in CrawlerItem class 
3. travel strategy bsf dsf 

complete:
=========
1. single process
   单进程的爬虫
   拥有深度/广度爬取策略

2. distributed crawler implemented with redis
   分布式爬虫 
   每个worker节点拥有bsf/dsf策略

todo:
====
1. bloom filter
2. avoid ban

