import random
from datetime import datetime
import operator
import numpy as np
#switch to max only
#same for min

def explicit(l):
    max_val = max(l)
    max_idx = l.index(max_val)
    return max_idx, max_val

def implicit(l):
    max_idx, max_val = max(enumerate(l), key=operator.itemgetter(1))
    return max_idx, max_val

def npmax(l):
    max_idx = np.argmax(l)
    max_val = l[max_idx]
    return (max_idx, max_val)

if __name__ == "__main__":
    from timeit import Timer

t = Timer("npmax(l)", "from __main__ import explicit, implicit, npmax; "
      "import random; import operator; import numpy as np;"
      "l = np.array([random.random() for _ in xrange(10000000)])")
print "Npmax: %.2f msec/pass" % (1000  * t.timeit(number=10)/10 )

t = Timer("explicit(l)", "from __main__ import explicit, implicit; "
      "import random; import operator;"
      "l = [random.random() for _ in xrange(10000000)]")
print "Explicit: %.2f msec/pass" % (1000  * t.timeit(number=10)/10 )

t = Timer("implicit(l)", "from __main__ import explicit, implicit; "
      "import random; import operator;"
      "l = [random.random() for _ in xrange(10000000)]")
print "Implicit: %.2f msec/pass" % (1000  * t.timeit(number=10)/10 )