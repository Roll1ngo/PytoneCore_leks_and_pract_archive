import datetime

payment = ()

houre = int(datetime.datetime.today().strftime("%H"))
rate = 1.68
rate_night = rate / 2
last_meter_reading = 5262


meter_readings = int(input("enter the meter readings:"))
different = meter_readings - last_meter_reading


def calc():
    if 8 < houre <= 23:
        payment = different * rate

    elif 23 < houre <= 8:
        payment = different * rate_night
    return payment


last_meter_reading = meter_readings
print(last_meter_reading)


print(calc(), "grn")
