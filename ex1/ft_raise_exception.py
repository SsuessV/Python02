def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    try:
        temp = input_temperature("25")
        print(f"Input data is '{temp}'")
        print(f"Temperature is now {temp}°C")
        print()

        print("Input data is 'abc'")
        input_temperature("abc")

    except ValueError as invalid:
        print(f"Caught input_temperature error: {invalid} ")
        print()

    try:
        print(f"Input data is '{100}'")
        input_temperature("100")

    except ValueError as invalid:
        print(f"Caught input_temperature error: {invalid} ")
        print()

    try:
        print(f"Input data is '{-50}'")
        input_temperature("-50")

    except ValueError as invalid:
        print(f"Caught input_temperature error: {invalid} ")
    print()
    print("All tests completed - program didn't crash!")


print("=== Garden Temperature Checker ===")
print()
test_temperature()
