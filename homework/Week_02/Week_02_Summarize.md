## HashMap 总结
1. JDK1.8 后HashMap使用 数组+红黑树结构存储数据. 
2. 扩容:
什么时候扩容：当向容器添加元素的时候, 会判断当前容器的元素个数, 如果大于等于阈值,  
(this.threshold = tableSizeFor(initialCapacity) * this.loadFactor) 的值的时候,
就要自动扩容. 方法是使用一个新的数组代替已有的容量小的数组.
3. putVal方法
```java
    final V putVal(int hash, K key, V value, boolean onlyIfAbsent,
                   boolean evict) {
        Node<K,V>[] tab; Node<K,V> p; int n, i;
        //如果table为空或者长度为0，则resize()
        if ((tab = table) == null || (n = tab.length) == 0)
            n = (tab = resize()).length;
        //确定插入table的位置，算法是(n - 1) & hash，在n为2的幂时，相当于取摸操作。
        ////找到key值对应的槽并且是第一个，直接加入
        if ((p = tab[i = (n - 1) & hash]) == null)
            tab[i] = newNode(hash, key, value, null);
        //在table的i位置发生碰撞，有两种情况，1、key值是一样的，替换value值，
        //2、key值不一样的有两种处理方式：2.1、存储在i位置的链表；2.2、存储在红黑树中
        else {
            Node<K,V> e; K k;
            //第一个node的hash值即为要加入元素的hash
            if (p.hash == hash &&
                ((k = p.key) == key || (key != null && key.equals(k))))
                e = p;
            //2.2
            else if (p instanceof TreeNode)
                e = ((TreeNode<K,V>)p).putTreeVal(this, tab, hash, key, value);
            //2.1
            else {
                //不是TreeNode,即为链表,遍历链表
                for (int binCount = 0; ; ++binCount) {
                ///链表的尾端也没有找到key值相同的节点，则生成一个新的Node,
                //并且判断链表的节点个数是不是到达转换成红黑树的上界达到，则转换成红黑树。
                    if ((e = p.next) == null) {
                         // 创建链表节点并插入尾部
                        p.next = newNode(hash, key, value, null);
                        ////超过了链表的设置长度8就转换成红黑树
                        if (binCount >= TREEIFY_THRESHOLD - 1) // -1 for 1st
                            treeifyBin(tab, hash);
                        break;
                    }
                    if (e.hash == hash &&
                        ((k = e.key) == key || (key != null && key.equals(k))))
                        break;
                    p = e;
                }
            }
            //如果e不为空就替换旧的oldValue值
            if (e != null) { // existing mapping for key
                V oldValue = e.value;
                if (!onlyIfAbsent || oldValue == null)
                    e.value = value;
                afterNodeAccess(e);
                return oldValue;
            }
        }
        ++modCount;
        if (++size > threshold)
            resize();
        afterNodeInsertion(evict);
        return null;
    }
```