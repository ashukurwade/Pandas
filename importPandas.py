import pandas as pd 

mydata = {
    'cars' : ["tata","mahindra","maruti"],
    'passing' : [3,6,9]
}
myvar = pd.DataFrame(mydata)

print(myvar)

