# Pj-Probe
A terminal visualization tool for GPU occupancy on S cluster in python based on [termgraph](https://github.com/mkaz/termgraph).
![image](https://user-images.githubusercontent.com/60593268/201825211-c1526c00-283d-4600-a440-9225ff11b01c.png)

## Install
Requires Python 3.7+, install from [githb](https://github.com/DelinQu/pjprob)

```
pip install git+https://github.com/DelinQu/pjprob
```


### Examples

```
termgraph data/ex1.dat

# Reading data from data/ex1.dat

2007: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 183.32
2008: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 231.23
2009: ▇ 16.43
2010: ▇▇▇▇ 50.21
2011: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 508.97
2012: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 212.05
2014: ▏ 1.00
```

An example using emoji as custom tick:

```
termgraph data/ex1.dat --custom-tick "🏃" --width 20 --title "Running Data"

# Running Data

2007: 🏃🏃🏃🏃🏃🏃🏃 183.32
2008: 🏃🏃🏃🏃🏃🏃🏃🏃🏃 231.23
2009:  16.43
2010: 🏃 50.21
2011: 🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃 508.97
2012: 🏃🏃🏃🏃🏃🏃🏃🏃 212.05
2014:  1.00

```


An example using stdin and emoji:

```
echo "Label,3,9,1" | termgraph --custom-tick "😀" --no-label


😀😀😀 3.00
😀😀😀😀😀😀😀😀😀 9.00
😀 1.00

```

Most results can be copied and pasted wherever you like, since they use standard block characters. However the color charts will not show, since they use terminal escape codes for color. A couple images to show color examples:

```
termgraph data/ex4.dat --color {blue,red}
```

<img src="https://user-images.githubusercontent.com/45363/43405623-1a2cc4d4-93cf-11e8-8c96-b7134d8986a2.png" width="655" alt="Multi variable bar chart with colors" />

```
termgraph data/ex7.dat --color {yellow,magenta} --stacked --title "Stacked Data"
```

<img src="https://user-images.githubusercontent.com/45363/43405624-1a4a821c-93cf-11e8-84f3-f45c65b7ca98.png" width="686" alt="Multi variable stacked bar chart with colors" />


Calendar Heatmap, expects first column to be date in yyyy-mm-dd

```
termgraph --calendar --start-dt 2017-07-01 data/cal.dat
```

<img src="https://user-images.githubusercontent.com/45363/43405619-1a15998a-93cf-11e8-8a3f-abfd2f6104a5.png" width="596" alt="Calendar Heatmap" />





### Usage
```
usage: termgraph.py [-h] [(optional arguments)] [filename]

draw basic graphs on terminal

positional arguments:
  filename              data file name (comma or space separated). Defaults to stdin.

optional arguments:
  -h, --help            show this help message and exit
  --title TITLE         Title of graph
  --width WIDTH         width of graph in characters default:50
  --format FORMAT       format specifier to use.
  --suffix SUFFIX       string to add as a suffix to all data points.
  --no-labels           Do not print the label column
  --no-values           Do not print the values at end
  --space-between       Print a new line after every field
  --color [COLOR ...]   Graph bar color( s )
  --vertical            Vertical graph
  --stacked             Stacked bar graph
  --histogram           Histogram
  --bins BINS           Bins of Histogram
  --different-scale     Categories have different scales.
  --calendar            Calendar Heatmap chart
  --start-dt START_DT   Start date for Calendar chart
  --custom-tick CUSTOM_TICK
                        Custom tick mark, emoji approved
  --delim DELIM         Custom delimiter, default , or space
  --verbose             Verbose output, helpful for debugging
  --label-before        Display the values before the bars
  --version             Display version and exit
```


### License

MIT License, see [LICENSE.txt](LICENSE.txt)

