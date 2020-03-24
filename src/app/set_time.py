'''
the following import is only necessary because eip.py is not in this directory
'''
import sys
sys.path.append('..')

'''
Get the PLC time
returns datetime.datetime type
'''
from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '10.4.42.135'
    comm.ProcessorSlot = 3
    ret = comm.GetPLCTime()
    print(ret.Value)
    ret = comm.SetPLCTime()
    ret = comm.GetPLCTime()
    print(ret.Value)
