#БЫЛО
#import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

#СТАЛО
import pandas as pd
import random
lst = [1] * 10
lst1 = [0] * 10
random.shuffle(lst)
random.shuffle(lst1)
data = pd.DataFrame({"robot":lst, "human":lst1})
data.head(20)