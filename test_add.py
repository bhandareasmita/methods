import add

# Test for the addition function
def test_addition():
    # Test case 1: Positive integers
    result = add.addition(3, 5)
    assert result == 8, "Expected 8, but got {}".format(result)

    # Test case 2: Negative integers
    result = add.addition(-3, -5)
    assert result == -8, "Expected -8, but got {}".format(result)

    # Test case 3: Mixed positive and negative
    result = add.addition(10, -5)
    assert result == 5, "Expected 5, but got {}".format(result)

    # Test case 4: Zero
    result = add.addition(0, 0)
    assert result == 0, "Expected 0, but got {}".format(result)

    print("All tests passed!")

# Run the test
test_addition()
