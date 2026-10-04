def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")
    elif operation_number == 1:
        42 / 0
    elif operation_number == 2:
        open("/non/existent/file")
    elif operation_number == 3:
        "hello" + 1
    else:
        return


def test_error_types() -> None:
    for op_num in (0, 1, 2, 3, 4):
        print(f"Testing operation {op_num}...")

        try:
            garden_operations(op_num)
        except ValueError as invalid:
            print(f"Caught ValueError: {invalid}")
        except ZeroDivisionError as invalid:
            print(f"Caught ZeroDivisionError: {invalid}")
        except FileNotFoundError as invalid:
            print(f"Caught FileNotFoundError: {invalid}")
        except TypeError as invalid:
            print(f"Caught TypeError: {invalid}")


print("All error types tested successfully!")

print("=== Garden Error Types Demo ===")
test_error_types()
print("Operation completed successfully")
print()
print("All error types tested successfully!")
