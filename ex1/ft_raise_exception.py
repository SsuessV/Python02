def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if 0 <= temp <= 40:
        return temp
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    else:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")


def test_temperature() -> None:
    print("Input data is '25'")
    temp = input_temperature("25")
    print(f"Temperature is now {temp}°C")
    print()

    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} ")
    print()

    print(f"Input data is '{100}'")
    try:
        input_temperature("100")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} ")
        print()

    print(f"Input data is '{-50}'")
    try:
        input_temperature("-50")
    except ValueError as e:
        print(f"Caught input_temperature error: {e} ")
    print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()
    test_temperature()
