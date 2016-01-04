#crawl\_leetcode\_problem\_description

爬取OJ网站[Leetcode](www.leetcode.com)的所有算法题的问题描述（除却加锁题）并将其存放在本地。

## 特点
- 使用编程语言是python 2.7.11
- 使用Requests进行网页爬取，并使用Beautifulsoup对爬取的网页进行数据提取
- 爬取后的算法题按照难易程度分成3个文件夹，写文件保存时文件名为题号+题名。

## 使用

	$ python crawl_leetcode_problem_description.py