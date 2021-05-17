import pandas as pd
import numpy as np
import argparse, os, sys

# print("the script has the name %s" % (sys.argv)
def parse_cmd():
    parser = argparse.ArgumentParser(
        prog=os.path.basename(__file__), usage='%(prog)s [options]')
    parser.add_argument('input_filename', help='input filename', type=str, metavar='<input>')
    parser.add_argument('output_filename', help='output filename', type=str, metavar='<output>')

    parser.add_argument('-r', '--ratio', help='ratio mode: divide all numbers by the average from the last row', action='store_true')
    parser.add_argument('-d', '--data', help='data mode: only raw data are shown',action='store_true')

    params = parser.parse_args()
    return params

input_param=parse_cmd()

df = pd.read_csv(input_param.input_filename,skiprows=51).loc[0:15].copy()
df = df.drop(['Wavelength(Ex/Em)','-/0 nm'], axis=1).copy()
print(f"reading the data: {input_param.input_filename}")

df = df.astype(float)
array = df.to_numpy()
final = np.concatenate([array_i.reshape(12,2) for array_i in array], axis=1)

if input_param.ratio == True:
    pd.DataFrame(final / np.mean(final[-1])).to_csv(input_param.output_filename)
elif input_param.data == True:
    pd.DataFrame(final).to_csv(input_param.output_filename)
else:
    print("Please add -r or -d to the program to pick between ratio and data mode.")
    sys.exit()

print(f"writing out the data: {input_param.output_filename}")
