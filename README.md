# Purchase calculation

### Description of the problem
Необходимо написать приложение, которое будет делать следующее:

Входным параметром является путь к файлу со строками следующего формата:

> m1 = ['A142', 'B104', 'A125', 'A142', 'C125']
> 
> m2 = ['B109', 'B140', 'B104', 'A142', 'A125', 'A142']
> 
> m3 = ['A142', 'A125', 'B104']

где m1, m2, m3 - порядковый номер месяца.
Необходимо вывести идентификатор товара и количество раз, сколько он был куплен, при условии, что он был куплен в каждом месяце.

Для примера выше результат будет:

```
'A142'---> 5
'A125'---> 3
'B104'---> 3
```

### Getting started

This solution includes the following scripts:

`purchases_generator.py` - script for generation random report about purchases.

`purchases_counter.py` - script for counting purchases represented in each month. <-- **Solution**

`demo.py` - demonstrative script.


### Installing

To install all dependencies run the following command:

```bash
pip install -r requirements.txt
```

### Running the solution demo

To take a look at the solution run the script `demo.py`:
```
python demo.py
```

### Author

🐺 Ilya Vouk 🐺

ilya.vouk@gmail.com

+375 29 2576807
