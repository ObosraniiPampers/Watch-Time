# WatchTime

A Python library for working with time in digital clock format (HH:MM), managing calendar dates, handling built-in timezone features, and displaying automatic live updates.

## Features

- **24-hour Time Encapsulation**: Automatically handles minutes overflow and cycles within 24 hours.
- **Operator Overloading**: Support for dunder methods allowing direct mathematical actions (`+`, `-`) and comparisons (`==`, `<`, `>`, `<=`, `>=`).
- **Timezone Calculations**: Easy shift of current system time by specified hours and minutes.
- **Live Console Player**: Built-in function (`AtThatMoment`) that refreshes the console every second to display live ticking time.
- **Strict Type Checking**: Returns `NotImplemented` on type mismatches to ensure robust standard exception handling.
- **Calendar Management (Date)**: Encapsulate, validate, and compare calendar dates (DD/MM/YYYY) with component-wise arithmetic

## Installation

The project includes an automatic bash installer script. To install the library locally to your user `site-packages`, clone the repository and run:

```bash
chmod +x install.sh
./install.sh
```

## Usage Examples

### Basic Operations & Comparisons

```python
from watchtime import WatchTime

# Initialization automatically fixes overflows
t1 = WatchTime(23, 75)  # Becomes 00:15
t2 = WatchTime(1, 30)

# Addition and Subtraction
print(t1 + t2)  # 01:45
print(t2 - t1)  # 01:15

# Boolean comparisons
print(t1 < t2)  # True
print(t1 == WatchTime(0, 15))  # True
```

### Working with Real Time & Timezones

```python
from watchtime import RealTimeWatchTime, TimeZone, AtThatMoment

# Get current system time shifted by 2 hours
local_time = RealTimeWatchTime(hour=2)
print(f"Local adjusted time: {local_time}")

# Get time in a specific timezone
cet_time = TimeZone(1)
print(f"Central european time: {cet_time}")
```

### Launching Live Clock

To start a live ticking clock inside your terminal that updates every second, pass the function as a callback into `AtThatMoment`:

```python
from watchtime import AtThatMoment, TimeZone

# Creates an infinite loop that catches SIGINT (Ctrl+C) for a clean exit
AtThatMoment(TimeZone, zonehour=2)
```

### Working with Date & TodayDate

```python
from watchtime import Date, TodayDate

# Date arithmetic (component-wise)
# 24-15=09 days, 12-10=02 months, 2027-2026=0001 year
print(Date(24, 12, 2027) - Date(15, 10, 2026))  # 09/02/01

# Dynamic date generation
print(TodayDate())  # 30/09/2026

# Boolean comparisons
d1 = Date(15, 10, 2026)
d2 = Date(24, 12, 2027)

print(d1 < d2)   # True
print(d1 == Date(15, 10, 2026))  # True
print(d2 >= d1)  # True
```

## License

This project is open-source and available under the MIT License.
