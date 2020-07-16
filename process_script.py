import subprocess
import argparse
import os
import warnings
import pandas as pd
from glob import glob
import pandas as pd


def call_one_exe(a):
    p = subprocess.Popen(["./a.out", a],stdout=subprocess.PIPE)
    p_out, err= p.communicate()
    output = p_out.decode("utf-8")
    return output.split(',')



if __name__=='__main__':
    #parse is only needed if we want to pass arg
    parser = argparse.ArgumentParser()
#     parser.add_argument('--num_thread', type=int, default=1000)
    args, _ = parser.parse_known_args()

    
    print('Received arguments {}'.format(args))
    
    files = glob('/opt/ml/processing/input/*')
    
    for i, f in enumerate(files):
        try:
            data = pd.read_csv(f, header=None)
            string = str(list(data.values.flat)).replace(' ','')[1:-1]
            #string looks like 2,3,5,6,7,8. Space is removed. '[' and ']' are also removed.
            predictions = call_one_exe(string)
            
            output_path = os.path.join('/opt/ml/processing/output', str(i)+'_out.csv')
            print('Saving training features to {}'.format(output_path))
            pd.DataFrame({'results':predictions}).to_csv(output_path, header=False, index=False)
        except Exception as e:
            print(str(e))
            


  


    
    