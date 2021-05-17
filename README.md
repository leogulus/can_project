# Can Project

## How to use the program
usage: finding_ratio.py [options]

positional arguments: \\
  <input>      input filename \\
  <output>     output filename

optional arguments: \\
  -h, --help   show this help message and exit \\
  -r, --ratio  ratio mode: divide all numbers by the average from the last row \\
  -d, --data   data mode: only raw data are shown 
  
## Example of how to use the program 
$ python finding_ratio.py vi210516_LLC1_screen.csv output_filename.csv -r
$ python finding_ratio.py vi210516_LLC1_screen.csv output_filename.csv -d
