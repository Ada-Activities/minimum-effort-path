from activity.main import min_effort_path
import pytest

def test_min_effort_path_example_1():
    # Arrange
    heights = [[1,2,2],[3,8,2],[5,3,5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 2

def test_min_effort_path_example_2():
    # Arrange
    heights = [[1,2,3],[3,8,4],[5,3,5]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 1

def test_min_effort_path_example_3():
    # Arrange
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 0

def test_min_effort_path_empty_graph():
    # Arrange
    heights = None

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 0

def test_min_effort_path_six_by_six():
    # Arrange
    heights = [[1,2,1,1,1,1],[1,2,1,2,1,2],[1,2,1,2,1,3],[1,2,1,2,1,3],[1,1,1,2,1,2]]

    # Act
    answer = min_effort_path(heights)

    # Assert
    assert answer == 1