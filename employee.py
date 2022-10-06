from typing import Optional


class Contract:
    def __init__(
        self, salary: int, hours_required: Optional[int] = None
    ) -> None:
        self.salary = salary
        self.hours_required = hours_required

    @property
    def wage(self) -> int:
        return (
            self.hours_required * self.salary
            if self.hours_required
            else self.salary
        )

    def __str__(self) -> str:
        if self.hours_required:
            return f'contract of {self.hours_required} hours at {self.salary}/hour'
        return f'monthly salary of {self.salary}'


class CommissionHandler:
    def __init__(
        self, bonus_rate: int, contracts_landed: Optional[int] = None
    ) -> None:
        self.bonus_rate = bonus_rate
        self.contracts_landed = contracts_landed

    @property
    def commission(self) -> int:
        return (
            self.bonus_rate * self.contracts_landed
            if self.contracts_landed
            else self.bonus_rate
        )

    def __str__(self) -> str:
        if self.contracts_landed is not None:
            return f'commission for {self.contracts_landed} contract(s) at {self.bonus_rate}/contract'
        return f'bonus commission of {self.bonus_rate}'


class Employee:
    def __init__(
        self,
        name: str,
        contract: Contract,
        commission_handler: Optional[CommissionHandler] = None,
    ) -> None:
        self._contract = contract
        self._commission_handler = commission_handler
        self.name = name

    def get_pay(self):
        if self._commission_handler is None:
            return self._contract.wage
        return self._contract.wage + self._commission_handler.commission

    def __str__(self) -> str:
        output_buffer = f'{self.name} works on a {self._contract}'
        if self._commission_handler:
            output_buffer += f' and receives a {self._commission_handler}'
        output_buffer += f'.  Their total pay is {self.get_pay()}.'
        return output_buffer


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_contract = Contract(4000)
billie = Employee('Billie', billie_contract)
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_contract = Contract(25, 100)
charlie = Employee('Charlie', charlie_contract)
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract, renee_commission = Contract(3000), CommissionHandler(200, 4)
renee = Employee('Renee', renee_contract, renee_commission)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract, jan_commission = Contract(25, 150), CommissionHandler(220, 3)
jan = Employee('Jan', jan_contract, jan_commission)
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_contract, robbie_commission = Contract(2000), CommissionHandler(1500)
robbie = Employee('Robbie', robbie_contract, robbie_commission)


# 'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.'

ariel_contract, ariel_commission = Contract(30, 120), CommissionHandler(600)
ariel = Employee('Ariel', ariel_contract, ariel_commission)
