# Hadoop

- Для выполнение входа в hadoop используйте систему [Katakoda](https://www.katacoda.com/courses/docker/playground) через google account!

- Команда чтобы веcти в консоль 
    ```docker run -i -t sequenceiq/hadoop-ubuntu:2.6.0 /etc/bootstrap.sh -bash```

- После вводите еще несколько команд:
    - `sudo apt update`
    - `sudo apt install nano`
    - `sudo apt install git -y`

- Для проверки работы Hadoop MapReduce У тех кто уже установил Hadoop на комп
```
cd $HADOOP_PREFIX
# run the mapreduce
bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.6.0.jar grep input output 'dfs[a-z.]+'

# check the output
bin/hdfs dfs -cat output/*
```

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

 - Для тех у кого установлен Hadoop:
```
bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file hadoop-problems/mapper.py -mapper mapper.py -file   hadoop-problems/reducer.py -reducer reducer.py -input /Hadoop_File/input/* -output /Hadoop_File/output
```
Ставите версию который у вас скорее это 3.3.1 например: streaming-3.3.1.jar

5. Посмотреть результаты:
```
cat output
```
- Для тех у кого установлен Hadoop:
```
bin/hdfs dfs -cat /Hadoop_File/output/*
```


6. Map Reduce с данными рандомных чисел с выводом суммы:
```
sudo chmod +x hadoop-problems/generator.py  hadoop-problems/map.py  hadoop-problems/reduce.py

hadoop-problems/generator.py | hadoop-problems/map.py | hadoop-problems/reduce.py
```
- Для тех у кого установлен Hadoop:
```
sudo chmod +x hadoop-problems/generator.py

# Сохраняем в Файл
hadoop-problems/generator.py > generator.txt

# Кладем в HDFS

bin/hdfs dfs -copyFromLocal ./generator.txt /Hadoop_File/input/

bin/hadoop jar share/hadoop/tools/lib/hadoop-streaming-2.6.0.jar -file hadoop-problems/map.py -mapper map.py -file   hadoop-problems/reduce.py -reducer reduce.py -input /Hadoop_File/input/generator.txt  -output /Hadoop_File/output-sum

#Посмотреть результат
bin/hdfs dfs -cat /Hadoop_File/output-sum/*
```

7. Записать Сумму в файл и отправить его в Hadoop HDFS
8. Изменить Reduce файл с помощью `nano hadoop-problems/reduce.py` чтобы сделать print для минимума из списка рандомных значении