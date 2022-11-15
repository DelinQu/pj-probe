# Pj-Probe
A terminal visualization tool for GPU occupancy on S cluster in python based on [termgraph](https://github.com/mkaz/termgraph).


## Install
Requires Python 3.7+, install from [github](https://github.com/DelinQu/pjprob)

```
# it is recommended to use a proxy.
pip install git+https://github.com/DelinQu/pjprob
```


### Examples

Default useage: pjprobr will list all the GPU of nodes in optimal partition.
```
pjprobe
```
![image](https://user-images.githubusercontent.com/60593268/201833629-168b2569-f4c9-4799-a3aa-b999690ae64f.png)

Specify user, partition, and node type：

```bash
pjprobe --user qudelin --partition optimal --type spot
```
![image](https://user-images.githubusercontent.com/60593268/201835089-6b8f0c2c-5d48-47a2-9e53-e186ca7c74ff.png)


An example using Customized colors:

```
pjprobe  --color {yellow,magenta,blue} 
```
![image](https://user-images.githubusercontent.com/60593268/201835709-d2cca610-5edf-49c2-b19e-3a0352d67995.png)


An example using stack 
```
 pjprobe --stacke --color {green,magenta,cyan} 
```
![image](https://user-images.githubusercontent.com/60593268/201836303-5c38a2a0-3d92-460d-b833-52ea022daab7.png)

emoji: coming soon ...
```
pjprobe --custom-tick "🏃" --width 20 --title "Running Data"

# Running Data

2007: 🏃🏃🏃🏃🏃🏃🏃 183.32
2008: 🏃🏃🏃🏃🏃🏃🏃🏃🏃 231.23
2009:  16.43
2010: 🏃 50.21
2011: 🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃🏃 508.97
2012: 🏃🏃🏃🏃🏃🏃🏃🏃 212.05
2014:  1.00

```

### Usage
```
usage: pjprobe [-h] [--title TITLE] [--user USER] [--partition PARTITION] [--type TYPE] [--show_others] [--width WIDTH] [--format FORMAT] [--suffix SUFFIX] [--no-labels] [--no-values] [--space-between] [--color [COLOR ...]] [--vertical] [--stacked] [--histogram] [--bins BINS]
               [--different-scale] [--start-dt START_DT] [--custom-tick CUSTOM_TICK] [--delim DELIM] [--verbose] [--label-before] [--version]

draw basic graphs on terminal

optional arguments:
  -h, --help            show this help message and exit
  --title TITLE         Title of graph
  --user USER           username
  --partition PARTITION
                        your partition
  --type TYPE           reserved or spot
  --show_others         Display the other gpu number
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

