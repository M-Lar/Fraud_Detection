import math
import random

T = MinTree([1,4,2,5,3])
T.dump()
T.popMin()
T.dump()
T.popMin()
T.dump()
T.changeVal(4, 3)
T.dump()
T.popMin()
T.dump()
T.popMin()
T.dump()
T.changeVal(4, 10)
T.dump()
T.popMin()
T.dump()

T = SamplingTree([10,40,12,50,30], 1)
T.dump()
T.sample()
T.dump()
T.sample()
T.dump()
T.changeVal(3, 3)
T.dump()
T.sample()
T.dump()
T.sample()
T.dump()
T.changeVal(4, 10)
T.dump()
T.sample()
T.dump()