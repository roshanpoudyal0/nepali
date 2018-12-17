import datetime
from nepali.datetime import *

# NepaliDate
npDate = NepaliDate.today()
print(repr(npDate))

npDate = NepaliDate(2075, 8, 20)
print(repr(npDate))

# NepaliTime
npTime = NepaliTime.now()
print(repr(npTime))

# NepaliDateTime

npDateTime = NepaliDateTime.now()
print(repr(npDateTime))

dt = datetime.datetime.now()
npDateTime = NepaliDateTime.from_datetime(dt)
print(repr(npDateTime))

npDateTime = NepaliDateTime(2075, 8, 20)
print(repr(npDateTime))


# NepaliDatetime timedelta operations
ndt1 = NepaliDateTime.now()
ndt2 = NepaliDateTime(2075, 8, 20)
td = datetime.timedelta(hours=5)
dt1 = datetime.datetime.now()

print(ndt1 + td)

print(ndt1 - td)
print(ndt1 - ndt2)
print(ndt2 - dt1)

print(ndt1 < ndt2)
print(ndt1 < dt1)

print(ndt1 <= ndt2)
print(ndt1 <= dt1)

print(ndt1 > ndt2)
print(ndt1 > dt1)

print(ndt1 >= ndt2)
print(ndt1 >= dt1)

print(ndt1 == ndt2)
print(ndt1 == dt1)

print(ndt1 != ndt2)
print(ndt1 != dt1)


# NepaliDateTime strftime()
npDateTime = NepaliDateTime.now()
print(npDateTime.strftime('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))
print(npDateTime.strftime_en('%a %A %w %d %b %B %m %y %Y %H %I %p %M %S'))


# Humanize datetime
humanize = HumanizeDateTime(datetime.datetime.now())
print(humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt)
print(humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt, threshold=0)
print(humanize.to_str())

ndt = NepaliDateTime(2075, 8, 2)
humanize = HumanizeDateTime(ndt, threshold=0, format='%a %A %w %d %b %B %m %y %Y')
print(humanize.to_str())