# test_admissions.py
import pytest
from admissions import Admissions
from labeled_matrix import LabeledMatrix

# Common setup
student_data = {"gpa": 3.8, "sat": 1450.0, "extracurric": 4.5}
admissions = Admissions()


def test_admit_v1():
    expected = (3.8 * 0.6) + (1450.0 * 0.1) + (4.5 * 0.15)
    result = admissions.admit_v1(3.8, 1450.0, 4.5)
    assert result == pytest.approx(expected)


def test_admit_v2():
    expected = (3.8 * 0.6) + (1450.0 * 0.1) + (4.5 * 0.15)
    # result = admissions.admit_v2(student_data)
    # assert result == pytest.approx(expected)


def test_admit_v3():
    expected_succeed = (3.8 * 0.75) + (1450.0 * 0.25)
    expected_contribute = (3.8 * 0.3) + (4.5 * 0.7)
    # result = admissions.admit_v3(student_data)
    # assert result[0] == pytest.approx(expected_succeed)
    # assert result[1] == pytest.approx(expected_contribute)


def test_admit_v4():
    weights = [
        lambda n: n["gpa"] * 0.6,
        lambda n: n["sat"] * 0.1,
        lambda n: n["extracurric"] * 0.15
    ]
    expected_gpa = 3.8 * 0.6
    expected_sat = 1450.0 * 0.1
    expected_extracurric = 4.5 * 0.15
    # result = admissions.admit_v4(student_data, weights)
    # assert result[0] == pytest.approx(expected_gpa)
    # assert result[1] == pytest.approx(expected_sat)
    # assert result[2] == pytest.approx(expected_extracurric)


def test_matrix_practice1():
    student_names1 = ["Walter", "Jesse", "Gus"]
    weight_functions1 = ["fn1", "fn2"]

    expected_matrix = LabeledMatrix(student_names1, weight_functions1,
                                    292, 437.35, 272.14, 406.86, 252.20, 378.30)
    assert expected_matrix == Admissions.matrix_practice1()


def test_matrix_practice2():
    student_names2 = ["Kratos", "Loki", "Odin", "Thor", "Heimdall"]
    weight_functions2 = ["fn1", "fn2", "fn3"]

    expected_matrix = LabeledMatrix(student_names2, weight_functions2,
                                    1, 1, 1, 0, 0, 0, 0.5, 0.7, 0.1, 0.5, 0.3, 0.9, 0.5, 0.3, 0.9)
    assert expected_matrix == Admissions.matrix_practice2()
