import random
import string

class get_random(object):
     def rand_string(self):
          up_low_alpha = string.ascii_letters
          rando_letters = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(20)])
	  print rando_letters
	  return str(rando_letters)


