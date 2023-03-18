'''
Created on 12/7/2022
@author:   Maria Ebrahim
Pledge:    I pledge my honor that I have abided by the Stevens honor system.

CS115 - Hw 12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    def __repr__(self):
        '''This method also returns a string representation for the object.'''
        return self.__str__()

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self): 
            '''Returns a new object with the same month, day, year 
               as the calling object (self).''' 
            dnew = Date(self.month, self.day, self.year) 
            return dnew
    def equals(self, d2): 
        '''Decides if self and d2 represent the same calendar date, 
            whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and self.day == d2.day
    def tomorrow(self):
        '''Changes the calling object so that it repersents one calendar day after the date it orginally repersented.'''
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        x=self.month
        if self.isLeapYear():
            DIM[2]+=1
        if self.day==DIM[x]:
            if self.month==12 and self.day==DIM[12]:
                self.day=1
                self.month=1
                self.year += 1
            else:
                self.day=1
                self.month += 1
        else:
            self.day+=1

    def yesterday(self):
        '''Changes the calling object so that it represents one calendar day before the date it originally represented.'''
        DIM = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if self.isLeapYear():
            DIM[2]+=1
        if self.day==1:
            if self.month==1:
                self.month=12
                self.day=DIM[12]
                self.year=self.year-1
            else:
                self.month=self.month -1
                self.day = DIM[self.month]
        else:
            self.day = self.day-1

    def addNDays(self, N):
        '''Changes the calling object so that it represents N calendar days after the date it originally represented.''' 
        if N>=0:
            for day in range(N):
                print(self)
                self.tomorrow()
        print(self)
    def subNDays(self, N):
        '''Changes the calling object so that it represents N calendar days before the date it originally represented.''' 
        if N>=0:
            for day in range(N):
                print(self)
                self.yesterday()
        print(self)
    def isBefore(self, d2):
        '''Return true if the calling object is a calender date before the input and false if not.'''
        if self.year==d2.year and self.month!=d2.month:
            return self.month<d2.month
        if self.month==d2.month and self.year==d2.year:
            return self.day<d2.day
        else:
            return self.year<d2.year

    def isAfter(self, d2):
        '''Return true if the calling object is a calender date after the input and false if not.'''
        if self.equals(d2):
            return False
        if self.isBefore(d2):
            return False
        else:
            return True

    def diff(self, d2):
        '''returns the differnce in the amount of days between the two dates inputed.'''
        self1 = self.copy()
        count = 0
        if self.equals(d2):
            count += 0
        elif self.equals(d2) == False:
            while self1.isBefore(d2):
                count += -1
                self1.tomorrow()
            while self1.isAfter(d2):
                count+=1
                self1.yesterday()
        return count
    def dow(self):
        '''Returns the day of the week in a given date.'''
        week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        dat = Date(12,7,1941)
        if (abs(self.diff(dat)))<8:
            return week[(abs(self.diff(dat)))]
        else:
            days = (abs(self.diff(dat)))%7
            return week[days]
