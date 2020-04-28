import pytest
import src.exercise

def test_exercise():
    input_values = ["5","25","35","10","55","55"]
    input_values_stored = ["5","25","35","10","55","55"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2]] == ["Give the first number:","Give the second number:","Greater number is: " + input_values_stored[1]]
    assert [output[3],output[4],output[5]] == ["Give the first number:","Give the second number:","Greater number is: " + input_values_stored[2]]
    assert [output[6],output[7],output[8]] == ["Give the first number:","Give the second number:","The numbers are equal!"]
