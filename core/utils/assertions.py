class Assertions:

    @staticmethod
    def assert_equals(actual,expected, message=""):

        assert actual == expected, (
            f"{message}"
            f"\nExpected: {expected}"
            f"\nActual: {actual}"
        )

    @staticmethod
    def assert_contains(actual,expected, message=""):

        assert expected in actual, (
            f"{message}"
            f"\nExpected to contain: {expected}"
            f"\nActual: {actual}"
        )