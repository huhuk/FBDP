[TOC]

# project2

- @ author:  huhu

---

####聚合数据

```bash
cat positive/* > positive.txt
cat neutral/* > neutral.txt
cat negative/* > negative.txt
```

---

#### 给数据打上 **类别标签**

```bash
#!/bin/bash
C1='./positive.txt'
C2='./neutral.txt'
C3='./positive.txt'

target='./raw.txt'

awk '{print "1", $0}' ${C1} >  ${target}
awk '{print "2", $0}' ${C2} >> ${target}
awk '{print "3", $0}' ${C3} >> ${target}
```

---

#### 打乱数据 切分 训练集 和 数据集

---

#### 使用一个小数据集

```bash
head raw.txt > t1
head -600 raw.txt | tail >> t1
tail raw.txt >> t1
```

---









