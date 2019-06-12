# WordDensity
> Shows the density of words in the file and charts plots with Python

<p align="center">
    <a href="https://github.com/timgrossmann/InstaPy/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/license-GPLv3-blue.svg" />
    </a>
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/built%20with-Python3-red.svg" />
    </a>
</p>

## Installation

```sh
pip3 install requirements.txt
```



## Quik Start

```sh
python3 quikstart.py
```


## Usage Example

#### Import library 

```python3
from util import word_density
```



#### Class

```python3
file = "Game.of.Thrones.S08E06.srt"

word_density = word_density(file)
```



#### Create a DataFrame with a class

```python3
df = word_density.get_df()
```



#### Show Chart

The graph shows 25 values  by default

```python3
word_density.get_chart()
```
```python3
word_density.get_chart(10)
```



## Meta

Furkan Tolga Yuce – [@furkantolgayuce](https://twitter.com/furkantolgayuce) – yucefurkantolga@gmail.com

[https://github.com/furkantolgayuce/word-density-in-subtitles/](https://github.com/furkantolgayuce/word-density-in-subtitles/)

## Contributing

1. Fork it (<https://github.com/furkantolgayuce/word-density-in-subtitles/>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
