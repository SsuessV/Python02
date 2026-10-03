def input_temperature(temp_str: str) -> int:
    return int(temp_str)


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
    print("All tests completed - program didn't crash!")


print("=== Garden Temperature ===")
print()
test_temperature()
