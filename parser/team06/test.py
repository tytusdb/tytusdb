# JSON Mode Test File
# Released under MIT License
# Copyright (c) 2020 TytusDb Team

from storageManager import jsonMode as j
import pandas as pd
from datetime import *

# drop all databases if exists


data={'iditemtesttbcalifica':['1','2','3','4','5','6'],
        'nombretesttbcalifica':['Jossie','Juanpi','Jossie','Hayrton','Jossie','AlguienX'],
    'apellidotesttbcalifica':['Castrillo','Garcia','Juarez','Ixpata','ApellidoA','ApellidoB'],
    'puntostesttbcalifica':['3.0','6.0','3.0','6.0','5.0','3.0'],
}
df=pd.DataFrame(data,columns=['iditemtesttbcalifica','nombretesttbcalifica','apellidotesttbcalifica','puntostesttbcalifica'])
print(df)
gg=df.groupby('puntostesttbcalifica')
print("El resultado de gg sera: \n",gg.first() )
#print(df.filter(like='nombre'))