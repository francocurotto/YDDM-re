import sys
sys.path.append("./engine")
from engine import Engine
pool =  "dicesets/starter.yaml"
engine = Engine("LIBRARY.yaml", pool, pool)
rocmd = {"command":"ROLL","dice":{0,1,2}}
dicmd = {"command":"DIM","dice":0,"net":"X1","pos":(15,6),
    "trans":[]}
