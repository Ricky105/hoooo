2.2
写好了两个爬虫工具，分别用于爬取微信公众号和机器之心。
微信公众号的比较麻烦，新闻的日期需要打开才能得到，使用selenium获取每次得新建一个driver很慢，优化为使用request直接请求url得到静态页面从中获得日期，但是爬下来看见页面的date是动态加载使用js放进去的，找见对应的js脚本，用re获得时间才行。
另外，这个支持截止日期自动停止，设置好uptodate的时间，会更新到点。
潜在考虑可以使用多线程的方法优化微信公众号的脚本。

2.4
写好了update_news，使用多进程并行同时爬取微信和机器之心，print测试了一下，可以看到所有函数能够并行启动，get的时候需要等待函数执行完毕。

2.6
整体架构设计：前端：React框架；后端用Go写

2.21
requirements.txt并python=3.10

4.10
requirements的urllib3==1.26.2；增加driver版本123，需要在spiders指定版本；新增update_news超链接合并；新增到10条wechat源；想到一种自动拓源wechat，爬的时候看到底下的tag可以拉进json中