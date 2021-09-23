''' This is input_functions.py wich include Definedinputs class
    Class contains different statci methods about inputs like:
     currency - input must be one of element from list of avaible currency
     funds - checks if typed datat is convertable to float
     val - does the same as funds but for transactions functions
     acc_numeber - checks if user type accureta account number'''


class DefinedInputs:
    @staticmethod
    def currency():
        list_of_avv_currency = ['PLN', 'EUR', 'USD', 'CHF', 'RUB', 'GBP']
        currency = input("Define currency (ex. PLN or EUR): ")
        if currency.upper() in list_of_avv_currency:
            return currency
        else:
            return DefinedInputs.currency()

    @staticmethod
    def funds():
        fund = input("Define starting currency: ")
        try:
            fund = float(fund)
            return fund
        except ValueError:
            print("Currency must be float data type!")
            return DefinedInputs.funds()

    @staticmethod
    def val():
        money = input("Type transaction value(use - for expense): ")
        try:
            money = float(money)
            return money
        except ValueError:
            print("Value must be float data type!")
            return DefinedInputs.val()

    @staticmethod
    def acc_number(length):
        number = input('Type account number: ')
        try:
            number = int(number)
            if number > length or number < 0:
                return DefinedInputs.acc_number(length)
            return number
        except ValueError:
            print("Account number must be int data type!")
            return DefinedInputs.acc_number(length)
        pass
