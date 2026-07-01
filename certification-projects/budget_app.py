# manages budget categories, tracking transactions and balances.
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    # records transaction and increases the balance.
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount

    # records transaction, if sufficient funds exist, decrease the balance.
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        return False
      
    def get_balance(self):
        return self.balance

    # moves funds from this category to another target category.
    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    # returns True if the category balance covers the requested amount.
    def check_funds(self, amount):
        return False if amount > self.balance else True

    # formats the ledger into a printable receipt layout.
    def __str__(self):
        title = self.name.center(30, '*')
        body = ''
        for entry in self.ledger:
            desc = entry["description"]
            amount = entry["amount"]
            # limit description to 23 chars and format amount to 2 decimal places
            formatted_desc = f"{desc[:23]:<23}"
            formatted_amount = f"{amount:>7.2f}"
            body += f"{formatted_desc}{formatted_amount}\n"
        return f'{title}\n{body}Total: {self.balance}'

# generates a text-based bar chart representing relative spending per category.
def create_spend_chart(categories):
    result = 'Percentage spent by category\n'

    spent_per_category = []
    total_spent = 0
    
    # calculate total and individual spending across all withdrawals
    for category in categories:
        category_spent = 0
        for entry in category.ledger:
            if entry["amount"] < 0:
                category_spent += abs(entry["amount"])
        spent_per_category.append(category_spent)
        total_spent += category_spent
    
    # calculate spending percentages rounded down to the nearest 10
    percentages = []
    for spent in spent_per_category:
        if total_spent > 0:
            percent = (spent / total_spent) * 100
            rounded_percent = (percent // 10) * 10
            percentages.append(int(rounded_percent))
        else:
            percentages.append(0)
    
    # render the chart bars from 100% down to 0%
    for i in range(100, -1, -10):
        result += f"{i:>3}|"
        for pct in percentages:
            if pct >= i:
                result += " o "
            else:
                result += "   "
        result += " \n"
    
    # render the horizontal separator line
    result += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    
    # render the category names vertically beneath the chart
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        result += "    " 
        for category in categories:
            if i < len(category.name):
                result += f" {category.name[i]} "
            else:
                result += "   "
        result += " "
        if i < max_len - 1:
            result += "\n"

    return result
