from models.income_model import Income
from extensions import db

#Create
def add_income(description, amount):
    new_income = Income(description=description, amount=amount)
    db.session.add(new_income)
    db.session.commit()
    return new_income.to_dict()

#Read

def get_all_income():
    incomes = Income.query.all()
    return [income.to_dict() for income in incomes]

def get_income_by_id(income_id):

    income = Income.query.get(income_id)
    return income

#Update
def update_income(income_id, description=None, amount=None):
    income = get_income_by_id(income_id)

    if description:
        income.description = description
    if amount:
        income.amount = amount
    db.session.commit()
    return income

#Delete
def delete_income(income_id):
    income = get_income_by_id(income_id)
    db.session.delete(income)
    db.session.commit()
    return income
    





