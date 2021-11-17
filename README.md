# Hadoop

- Для выполнение входа в hadoop используйте систему [Katakoda](https://www.katacoda.com/courses/docker/playground) через google account!

- Команда чтобы веcти в консоль 
    ```docker run -i -t sequenceiq/hadoop-ubuntu:2.6.0 /etc/bootstrap.sh -bash```

- После вводите еще несколько команд:
    - `sudo apt update`
    - `sudo apt install nano`
    - `sudo apt install git -y`


# Задание

1. Cкачать файлы с помощью git clone
```
cd $HADOOP_PREFIX
git clone https://github.com/Akashi23/hadoop-problems
```

2. Попробовать положить свои файлы в HDFS
```
ls hadoop-problems
# чтобы увидеть какой файл вы хотите положить в HDFS
bin/hdfs dfs -mkdir -p /Hadoop_File/input
bin/hdfs dfs -copyFromLocal ./hadoop-problems/start.txt /Hadoop_File/input/
```

3. Попробовать вытащить свои файлы в HDFS

```
bin/hdfs dfs -copyToLocal /Hadoop_File/input/start.txt start.txt

cat start.txt
```

4. Выполнить MapReduce с помощью Python:
```
# Даем права для выполнения
sudo chmod +x ./hadoop-problems/mapper.py ./hadoop-problems/reducer.py

bin/hdfs dfs -cat /Hadoop_File/input/start.txt | ./hadoop-problems/mapper.py | sort | ./hadoop-problems/reducer.py > output
```

5. Посмотреть результаты:
```
cat output
```

6. Map Reduce с данными рандомных чисел с выводом суммы:
```
sudo chmod +x hadoop-problems/generator.py  hadoop-problems/map.py  hadoop-problems/reduce.py

hadoop-problems/generator.py | hadoop-problems/map.py | hadoop-problems/reduce.py
```

7. Записать Сумму в файл и отправить его в Hadoop HDFS
8. Изменить Reduce файл с помощью `nano hadoop-problems/reduce.py` чтобы сделать print для минимума из списка рандомных значении