"""
Create a bank account with deposit and withdraw function
"""
class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "%s's account. Balance: $%.2f" % (self.name, self.balance)
  
  def show_balance(self):
    print "Balance: $%.2f" % self.balance
    
  def deposit(self, amount):
    if amount <= 0:
      print "Error deposit!"
      return
    else:
      print "$%.2f is depositing!" % amount
      self.balance += amount
      self.show_balance()
      
  def withdraw(self, amount):
    if amount > self.balance:
      print "Error withdraw!"
      return
    else:
      print "withdrawing: $%.2f" % amount
      self.balance -= amount
      self.show_balance()
      
      
my_account = BankAccount("roger")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account

      
