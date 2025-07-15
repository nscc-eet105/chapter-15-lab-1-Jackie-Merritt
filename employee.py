#Jackie-Merritt_Chp15-Lb1_7/15/2025
from dataclasses import dataclass


class Employee:

    def __init__(self, name = "", hours = 0, pay = 0):
        self.__name = str(name)

        self.__hours = hours

        self.__pay = pay

        self.__total_pay = 0

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def hours(self):
        return self.__hours
    @hours.setter
    def hours(self, hours):
        self.__hours = hours

    @property
    def pay(self):
        return float(self.__pay)
    @pay.setter
    def pay(self, pay):
        self.__pay = pay

    def calc_pay(self):
        self.__total_pay = self.__hours * self.__pay
        return self.__total_pay

    def __str__(self):
        return f"Employee(_Employee__name='{self.__name}', _Employee__hours_worked={self.__hours}, _Employee__hourly_rate={self.__pay:.2f})"
    def display_total_pay(self):
        print(f'Total pay for {self.__name} is {self.__total_pay:.2f}$')
class Salesperson(Employee):
    def __init__(self, name = "", hours = 0, pay = 0, weekly = 0, com_percent = 0):
        super().__init__(name = "", hours = 0, pay = 0)
        self.__weekly = weekly
        self.__com_percent = com_percent
    @property
    def weekly(self):
        return self.__weekly
    @weekly.setter
    def weekly(self, weekly):
        self.__weekly = weekly
    @property
    def com_percent(self):
        return self.__com_percent
    @com_percent.setter
    def com_percent(self, com_percent):
        self.__com_percent = com_percent
    def __str__(self):
        return f"Employee(_Employee__name='{Employee.name}', _Employee__hours_worked={Employee.hours}, _Employee__hourly_rate={Employee.pay:.2f}, _Salesperson__weekly_sales={self.__weekly}, _Salesperson__commision_rate={self.__com_percent})"
    
        
        
employee1 = Salesperson()
employee1.name = 'James'
employee1.hours = 40
employee1.pay = 15.50
print(employee1)
employee1.calc_pay()
employee1.display_total_pay()
