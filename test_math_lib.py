import pytest
from math_lib import add, sub, compute_list_mean
import math


def test_add():
    """Should pass"""
    assert add(10, -5) == 5


class TestSub:
    @staticmethod
    def test_pass():
        """Should pass"""
        assert sub(10, -5) == 15

    @staticmethod
    def test_fail():
        """Should fail"""
        assert sub(10, 2) == 0


class TestComputeListMean:
    @staticmethod
    def test_empty_list():
        # Act
        result = compute_list_mean([])
        # Assert
        assert result == 0

    @staticmethod
    def test_number_list():
        # Arrange
        in_list = [0.5, 1, 2.5]
        mean = 4 / 3
        # Act
        result = compute_list_mean(in_list)
        # Assert
        assert math.isclose(result, mean)

    @staticmethod
    def test_wrong_type_in_list():
        # Arrange
        in_list = [0, "X"]
        # Act & Assert
        with pytest.raises(TypeError):
            compute_list_mean(in_list)
