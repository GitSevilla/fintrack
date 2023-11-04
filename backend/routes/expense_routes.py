from flask import Blueprint, jsonify, request
import services.expense_service as e_s

expense_bp = Blueprint('expense', __name__)


@expense_bp.route('/expense', methods=["GET"])
def list_expense():
    expenses = e_s.get_all_expense()
    return jsonify(expenses)


@expense_bp.route('/expense', methods=['POST'])
def add_expense():
    data = request.get_json()
    description = data.get("description")
    amount = data.get("amount")
    result = e_s.add_expense(description, amount)
    return jsonify(result), 201


@expense_bp.route('/expense/<int:expense_id>', methods=['PUT'])
def update_expense(expense_id):
    data = request.get_json()
    description = data.get('description')
    amount = data.get("amount")

    updated_expense = e_s.update_expense(expense_id, description, amount)

    if updated_expense:
        return jsonify({
            "message": "Expense updated successfully!",
            "Expense": {
                "id": updated_expense.id,
                "description": updated_expense.description,
                "amount": updated_expense.amount
            }
        })
    else:
        return jsonify({"message": "Error updating expense"}), 400


@expense_bp.route("/expense/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    deleted_expense = e_s.delete_expense(expense_id)
    return jsonify({"message": "expense Deleted",
                    "Expense Deleted": {
                        "id": deleted_expense.id,
                        "description": deleted_expense.description,
                        "amount": deleted_expense.amount
                    }}), 201


@expense_bp.route('/test', methods=['GET'])
def test_route():
    return "Test-Expense"
