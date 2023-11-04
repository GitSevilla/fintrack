from models.expense_model import Expense
from extensions import db

#Create
def add_expense(description, amount):
    new_expense = Expense(description=description, amount=amount)
    db.session.add(new_expense)
    db.session.commit()
    return new_expense.to_dict()

#Read

def get_all_expense():
    expenses = Expense.query.all()
    return [expense.to_dict() for expense in expenses]

def get_expense_by_id(expense_id):

    expense = Expense.query.get(expense_id)
    return expense

#Update
def update_expense(expense_id, description=None, amount=None):
    expense = get_expense_by_id(expense_id)

    if description:
        expense.description = description
    if amount:
        expense.amount = amount
    db.session.commit()
    return expense

#Delete
def delete_expense(expense_id):
    expense = get_expense_by_id(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return expense