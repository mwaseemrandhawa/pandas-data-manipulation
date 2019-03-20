import os
import pandas as pd
path = 'F:\projects\ml\preprocessing'
save_path = "results"
if not os.path.exists("results"):
    os.makedirs(save_path)
for filename in os.listdir(path):
        if not filename.endswith('.csv'): continue
        fullname = os.path.join(path, filename)
        print('Proceessing....')
        file = pd.read_csv(fullname)
        file.drop(['VRot', 'VVH', 'HDate', 'HRot', 'VH'], axis=1, inplace=True)
        file.rename(columns={'VOpen OU':'overOpenVal', 'VOdd':'overOpenOdd', 'VClose OU':'overCloseVal', 'VClose Odd':'overCloseOdd',
                    'HOpen OU':'underOpen', 'HOpenOUOdd':'underOpenOdd', 'HCloseOU':'underCloseVal', 'HClose OUOdd':'underCloseOdd'}, 
                 inplace=True)
        file.to_csv(os.path.join(save_path, filename), sep=',', index=False)
        