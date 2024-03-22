from src.calculator import add, multiply


def lambda_handler(event: dict, context: dict) -> dict:
    operation = event.get("operation", "add")

    number_1 = event.get("number_1", "5")
    number_2 = event.get("number_2", "10")

    result = None
    if operation == "add":
        result = add(int(number_1), int(number_2))
    elif operation == "multiply":
        result = multiply(int(number_1), int(number_2))

    return {"status": "success", "operation": operation, "result": result}


if __name__ == "__main__":
    lambda_handler({"number_1": "10", "number_2": "10"}, {})
