import sys

with open(sys.argv[1]) as file:
    arrival = int(file.readline())
    schedule = [
        int(entry)
        for entry in file.readline().split(',')
        if entry != 'x'
    ]

def waiting_time(period):
    return period - (arrival % period)

bus = min(schedule, key=waiting_time)

print(bus, waiting_time(bus), bus * waiting_time(bus))
