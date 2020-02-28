from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from pylogix import PLC
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def overview():
    return render_template('overview.html', name='overview')

@app.route('/rabbits')
def rabbits():
    last_runs =[
        get_date_time('Stn010_Rabbit_Mode.Last_Ran.'),
        get_date_time('Program:Stn020.Stn020_Rabbit_Mode.Last_Ran.'),
        get_date_time('Program:Stn030.Stn030_Rabbit_Mode.Last_Ran.'),
        get_date_time('Program:Stn040.Stn040_Rabbit_Mode.Last_Ran.'),
    ]
   
    return render_template('rabbits.html', name='rabbits', last_runs=last_runs)

@app.route('/production')
def production():


    tag_prefix = 'Program:Production.ProductionData.HourlyParts.Total.'
    today_hourly, today_totals = get_production(tag_prefix)

    tag_prefix = 'Program:Production.ProductionData.PrevDayHourlyParts[0].Total.'
    prev_hourly, prev_totals = get_production(tag_prefix)

    template_data = {
        'name': 'production',
        'today_totals': today_totals,
        'today_hourly': today_hourly,
        'prev_totals': prev_totals,
        'prev_hourly': prev_hourly
        }
            
    return render_template('production.html', **template_data)

@app.route('/bypass')
def bypass():
    return render_template('bypass.html', name='bypass')

def get_production(tag_prefix):

    with PLC() as comm:
        comm.IPAddress = '10.4.42.135'
        comm.ProcessorSlot = 3

        hourly = []
        totals = []
        for shift in range(3):
            shift_counts = []
            for hour in range(8):
                tag_name = tag_prefix + 'Shift_'+ str(shift+1) + '_Hour_' + str(hour+1) + '_Total'
                # print(tag_name)
                ret = comm.Read(tag_name)
                # print(ret.TagName, ret.Value, ret.Status)
                if ret.Status == 'Success':
                    shift_counts.append(ret.Value)
                else:
                    shift_counts.append('Error')

            hourly.append(shift_counts)

            tag_name = tag_prefix + 'Shift_' + str(shift+1) + '_Total' 
            ret = comm.Read(tag_name)
            # print(ret.TagName, ret.Value, ret.Status)
            if ret.Status == 'Success':
                totals.append(ret.Value)
            else:
                totals.append('Error')
    return (hourly, totals)

def get_date_time(tag_prefix):
    with PLC() as comm:
        comm.IPAddress = '10.4.42.135'
        comm.ProcessorSlot = 3

        tag_list=[
            tag_prefix + 'Year',
            tag_prefix + 'Month',
            tag_prefix + 'Day',
            tag_prefix + 'Hour',
            tag_prefix + 'Min',
            tag_prefix + 'Sec'
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

