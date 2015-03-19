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
   target:
   分布式爬虫 
   每个worker节点拥有bsf/dsf策略
   添加保存页面功能
   usage:
   需要在master上安装redis
   在worker上修改配置settings.py

todo:
====
1. bloom filter
2. avoid ban
3. cookie的支持
4. ajax的抓取
