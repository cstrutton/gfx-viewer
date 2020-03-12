from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '10.4.42.135'
    comm.ProcessorSlot = 3
    ret = comm.Read('Program:Production.ProductionData.PrevDayHourlyParts[0].Total.DailyTotal')
    print(ret.Status, ret.Value)