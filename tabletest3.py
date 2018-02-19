
import tables as tb

print("jd starting")

class Particle(tb.IsDescription):
    name        = tb.StringCol(16, pos=1) # 16-character String
    lati        = tb.IntCol(pos=2)        # integer
    longi       = tb.IntCol(pos=3)        # integer
    pressure    = tb.Float32Col(pos=4)  # float  (single-precision)
    temperature = tb.FloatCol(pos=5)    # double (double-precision)

fileh = tb.open_file('test4.h5', mode='w')
table = fileh.create_table(fileh.root, 'table', Particle,
                           "A table")

# Append several rows in only one call
table.append([("Particle:     10", 10, 0, 10 * 10, 10**2),
              ("Particle:     11", 11, -1, 11 * 11, 11**2),
              ("Particle:     12", 12, -2, 12 * 12, 12**2)])
fileh.close()

print ("jd finished")