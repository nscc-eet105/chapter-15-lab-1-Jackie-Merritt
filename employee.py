#Jackie-Merritt_Chp15-Lb1_7/15/2025
from dataclasses import dataclass

@dataclass
class Employee:
    name:str = ""
    hours:float = 0
    pay:float = 0

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

    def display_total_pay(self):
        self.__total_pay = self.__hours * self.__pay
        print(f'Total pay for {self.__name} is {self.__total_pay:.2f}$')
        print()
@dataclass
class Salesperson(Employee):
    weekly:float = 0
    com_percent:float = 0
    
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

    def display_total_pay(self):
        self.__total_pay = self.pay * self.hours
        self.__sales_pay = (self.__weekly * self.com_percent)
        self.__sales_total_pay = self.__sales_pay + self.__total_pay
        print(f'Total pay for {self.name} is {self.__sales_total_pay:.2f}$')

    #def display(self):
        #print(f"Salesperson(_Employee__name='{self.name}', _Employee__hours_worked={self.hours}, _Employee__hourly_rate={self.pay:.2f}, _Salesperson__weekly_sales={self.weekly}, _Salesperson__commision_rate={self.__com_percent})")

    
        
        
#employee1 = Salesperson('Leroy Jetson', 25, 15.00, 2550.50, .03)
#employee1.name = 'James'
#employee1.hours = 40
#employee1.pay = 15.50
#employee1.com_percent = 3
#employee1.display()
#employee1.calc_pay()
#employee1.display_total_pay()
#print(employee1)

