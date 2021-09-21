class DefinedInputs:
    @staticmethod
    def currency():
        list_of_avv_currency=['PLN','EUR','USD','CHF','RUB','GBP']
        currency=input("Define currency (ex. PLN or EUR): ")
        if currency.upper() in list_of_avv_currency:
            return currency
        else:
            return DefinedInputs.currency()
    @staticmethod
    def funds():
        fund=input("Define starting currency: ")
        try:
            fund=float(fund)
            return fund
        except ValueError:
            print("Currency must be float data type!")
            return DefinedInputs.funds()
    @staticmethod
    def val():
        money=input("Type transaction value(use - for expense): ")
        try:
            money=float(money)
            return money
        except ValueError:
            print("Value must be float data type!")
            return DefinedInputs.val()
