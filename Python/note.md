# Note
## Array
  1. 566 Reshape the Matrix：列表生成式比append方法效率高
  2. 167 Two Sum II - Input array is sorted：...
  3. Fair Candy Swap：in操作转化成set来做
  
## Easy
  1. 141 环形链表: 快慢指针，快指针一定先到终点
## Medium
  1. 146 LRU缓存：用字典记录数据，列表记录使用顺序
  2. 5 最长回文子串：Manacher算法 O(n);加#使得回文串都变奇数
  3. 33 搜索旋转排序数组：直接二分法，中心点的左右两侧必有至少一侧是有序的
## Hard
  1. 460 LFU缓存：坑，key换一个value也算一次调用
  2. 23 合并K个排序链表：用优先队列queue.PriorityQueue可以使复杂度降为O(N*logk)