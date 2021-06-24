import sys
sys.path.append("./engine")
from engine import Engine
pool =  "dicesets/starter.yaml"
engine = Engine("LIBRARY.yaml", pool, pool)
