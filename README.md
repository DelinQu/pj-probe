# Pj-Probe :basecampy:

A terminal visualization tool for GPU occupancy on S cluster in python based on [termgraph](https://github.com/mkaz/termgraph).

![image](https://user-images.githubusercontent.com/60593268/202074001-f3b7fde4-7b76-4905-9746-f5a687f6e79d.png)

- [x] :seedling: 2022-11-15 : create repo and release version 0.0.1.
- [x] :deciduous_tree: 2022-11-16 : changed the legend, fixed alignment bugs and release version 0.0.2.


## Install
Requires Python 3.7+, install from [github](https://github.com/DelinQu/pj-probe)

```
# it is recommended to use a proxy.
pip install git+https://github.com/DelinQu/pj-probe
```


### Examples

Default useage: pjprobe will list all the GPU of nodes in **optimal** partition.
```
pjprobe
```
![image](https://user-images.githubusercontent.com/60593268/202074340-e307e37d-3e00-4276-b021-b9688e512c51.png)


:point_down: :point_down: :point_down: pjprobe  in stacked mode.
```
pjprobe  --stacked
```
![image](https://user-images.githubusercontent.com/60593268/202074001-f3b7fde4-7b76-4905-9746-f5a687f6e79d.png)


Specify user, partition, and node type：

```bash
pjprobe --user xukaixin  --partition ai4science --type reserved --stacked
```
![image](https://user-images.githubusercontent.com/60593268/202075062-9b680636-f9e9-4abc-8b45-bffcfb7b9e71.png)



An example using Customized colors:

```
pjprobe  --color {yellow,magenta,blue} --stacked
```
![image](https://user-images.githubusercontent.com/60593268/202075163-25a35846-771d-48f3-886b-97b50bd2061d.png)


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

