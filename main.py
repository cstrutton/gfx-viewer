from flask_bootstrap import Bootstrap
from flask import Flask, render_template
from pylogix import PLC

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def overview():
    return render_template('overview.html', name='overview')

@app.route('/rabbits')
def rabbits():
    return render_template('rabbits.html', name='rabbits')

@app.route('/production')
def production():

    with PLC() as comm:
        comm.IPAddress = '10.4.42.135'
        comm.ProcessorSlot = 3

        tag_prefix = 'Program:Production.ProductionData.HourlyParts.Total.'
        today_hourly = []
        today_totals = []
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

            today_hourly.append(shift_counts)

            tag_name = tag_prefix + 'Shift_' + str(shift+1) + '_Total' 
            ret = comm.Read(tag_name)
            # print(ret.TagName, ret.Value, ret.Status)
            if ret.Status == 'Success':
                today_totals.append(ret.Value)
            else:
                today_totals.append('Error')

    template_data = {
        'name': 'production',
        'totals': today_totals,
        'hourly': today_hourly
        }
            
    return render_template('production.html', **template_data)

@app.route('/bypass')
def bypass():
    return render_template('bypass.html', name='bypass')