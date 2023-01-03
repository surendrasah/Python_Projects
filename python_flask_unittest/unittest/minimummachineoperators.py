"""
Program to find the minimum number of MOs which are required to help the SO so that every machine at
each site of the company is maintained.
"""

import math

#function to check the data type
def typecheck(checkvalue):
    if type(checkvalue) != int:
        raise TypeError

#function for minimum machine operators
def machineoperators(machines,so_c,mo_p):

    #type check
    typecheck(so_c)
    typecheck(mo_p)

    #minimum no of machine operator
    min_mo_count = 0

    try:
        #machine type and range check
        if not machines:
            return("The machines list is empty")

        for i in machines:
            typecheck(i)
            if i >100 or i<1:
                raise ValueError

        #so_c range check
        if so_c >999 or so_c<1:
            raise ValueError

        #mo_p range check
        if mo_p>1000 or mo_p<1:
            raise ValueError

    except TypeError:
        return ("Not an integer values, please give integer values")

    except ValueError:
        return ("Does not satisfy the constraint, please provide proper range value")

    else:
        for machinevalue in machines:
            val = machinevalue

            if (val >= so_c):
                min_mo_count = min_mo_count + 1
                val = val - so_c
                if (val > mo_p):
                    mini_mo=math.ceil(val/mo_p) #operators can not be float and uppermost value
                    min_mo_count = min_mo_count + mini_mo
                    val = mini_mo-so_c

            if (val < so_c and val > 0):
                min_mo_count = min_mo_count + 1


            #print("minimum inside loop count",min_mo_count)
        #print("minimum count",min_mo_count)
    return min_mo_count






