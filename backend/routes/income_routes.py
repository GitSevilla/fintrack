from flask import Blueprint, jsonify, request
import services.income_service as i_s

income_bp = Blueprint('income', __name__)


@income_bp.route('/income', methods=["GET"])
def list_income():
    incomes = i_s.get_all_income()
    return jsonify(incomes)


@income_bp.route('/income', methods=['POST'])
def add_income():
    data = request.get_json()
    description = data.get("description")
    amount = data.get("amount")
    result = i_s.add_income(description, amount)
    return jsonify(result), 201


@income_bp.route('/income/<int:income_id>', methods=['PUT'])
def update_income(income_id):
    data = request.get_json()
    description = data.get('description')
    amount = data.get("amount")

    updated_income = i_s.update_income(income_id, description, amount)

    if updated_income:
        return jsonify({
            "message": "Income updated successfully!",
            "Income": {
                "id": updated_income.id,
                "description": updated_income.description,
                "amount": updated_income.amount
            }
        })
    else:
        return jsonify({"message": "Error updating income"}), 400


@income_bp.route("/income/<int:income_id>", methods=["DELETE"])
def delete_income(income_id):
    deleted_income = i_s.delete_income(income_id)
    return jsonify({"message": "Income Deleted",
                    "Income Deleted": {
                        "id": deleted_income.id,
                        "description": deleted_income.description,
                        "amount": deleted_income.amount
                    }}), 201


@income_bp.route('/test', methods=['GET'])
def test_route():
    return "Test"
