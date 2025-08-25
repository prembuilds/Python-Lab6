# Define a class Time with attributes hours, minutes, and seconds. Overload
# the == operator to compare two Time objects for equality. Implement the
# __eq__() method and test it by comparing two Time instances.

class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __eq__(self, other):
        if isinstance(other, Time):
            return (self.hours == other.hours and
                    self.minutes == other.minutes and
                    self.seconds == other.seconds)
        return False


t1 = Time(2, 3, 45)
t2 = Time(2, 3, 45)
t3 = Time(3, 12, 43)
print(t1 == t2)
print(t1 == t3)
    