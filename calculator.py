def lambda_handler(event, context):
    number_1 = event.get("number_1", "5")
    number_2 = event.get("number_2", "10")

    print(
        f"Sum of {number_1} and {number_2} is {int(number_1) + int(number_2)}"
    )

    return {"status": "success", "result": int(number_1) + int(number_2)}


if __name__ == "__main__":
    lambda_handler({"number_1": "5", "number_2": "10"}, None)
