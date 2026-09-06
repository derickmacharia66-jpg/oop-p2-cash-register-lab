#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")

    def add_item(self, item, price, quantity):
        self.total += price * quantity
        self.items.append(item)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        self.total -= self.total * (self.discount / 100)

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("There is no transaction to void.")
            return

        last_tx = self.previous_transactions.pop()
        
        # Deduct price based on quantity of the last item
        self.total -= last_tx["price"] * last_tx["quantity"]
        
        # Remove item from items list
        if last_tx["item"] in self.items:
            self.items.remove(last_tx["item"])