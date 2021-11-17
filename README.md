# Hadoop

- Для выполнение входа в hadoop используйте систему [Katakoda](https://www.katacoda.com/courses/docker/playground) через google account!

- Команда чтобы веcти в консоль 
    ```docker run -i -t sequenceiq/hadoop-ubuntu:2.6.0 /etc/bootstrap.sh -bash```

- После вводите еще несколько команд:
    - `sudo apt update`
    - `sudo apt install nano`
    - `sudo apt install git`

- Для протестирование работает ли MapReduce
```
cd $HADOOP_PREFIX
bin/hdfs dfs -cat input/*

bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar grep input output 'dfs[a-z.]+'

# check the output
bin/hdfs dfs -cat output/*
```

# Задание

1. Cкачать файлы с помощью git clone
```
cd $HADOOP_PREFIX
git clone 
```

2. Попробовать положить свои файлы в HDFS
```
ls hadoop-problems
# чтобы увидеть какой файл вы хотите положить в HDFS
bin/hdfs dfs -mkdir /Hadoop_File
bin/hdfs dfs -copyFromLocal ./hadoop-problems/Adept.txt /Hadoop_File/input/
```

3. Выполнить MapReduce с помощью Python:
```
bin/hadoop jar /usr/lib/hadoop-2.6.0/share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file ./hadoop-problems/mapper.py -mapper mapper.py -file   ./hadoop-problems/reducer.py -reducer reducer.py -input /Hadoop_File/input -output /Hadoop_File/output
```

4. Посмотреть результаты:
```
bin/hdfs dfs -cat /Hadoop_File/output
```

5. 
