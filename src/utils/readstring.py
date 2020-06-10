from pylogix import PLC
from datetime import datetime
import humanize


def readString(tag):
    with PLC() as comm:
        comm.IPAddress = '10.4.42.135'
        comm.ProcessorSlot = 3
        length = comm.Read('{}.LEN'.format(tag))
        if not (length.Status == 'Success'):
            return length
        if not length.Value:
            return None

        ret = comm.Read(tag + '.DATA', length.Value)
        if ret.Status == 'Success':
            return ''.join(chr(i) for i in ret.Value)
        else:
            return ret


def get_date_time(tag_prefix):
    """ Returns a datetime object from a collection of tags """
    with PLC() as comm:
        comm.IPAddress = '10.4.42.135'
        comm.ProcessorSlot = 3

        tag_list = [
            tag_prefix + '.Year',
            tag_prefix + '.Month',
            tag_prefix + '.Day',
            tag_prefix + '.Hour',
            tag_prefix + '.Min',
            tag_prefix + '.Sec'
        ]

        x = list(map(test_response, comm.Read(tag_list)))
        if -1 not in x:
            return datetime(*x)


def test_response(resp):
    """ Returns the Value of a response object if Status is Success, -1 other wise """
    if resp.Status == 'Success':
        return resp.Value
    else:
        return -1


def getbypasslogentry(station, entry):
    # print('station: {}, entry: {}  - '.format(station, entry), end="")
    text = readString(
        'Stn0{}0_Bypass_Data.Bypass_Logging[{}].Bypass_String'.format(station, entry))
    if not text:
        return (None, None)
    timestamp = get_date_time(
        'Stn0{}0_Bypass_Data.Bypass_Logging[{}].Date_Time.Actual'.format(station, entry))
    return (timestamp, text)


if __name__ == "__main__":

    log = []
    for station in range(1, 5):
        for entry in range(0, 25):
            time, text = getbypasslogentry(station, entry)
            if time and text:
                logentry = '{} - Stn {}0 - {}'.format(
                    time.isoformat(), station, text)
                log.append(logentry)

    log.sort(reverse=True)
    for entry in log:
        print(entry)
