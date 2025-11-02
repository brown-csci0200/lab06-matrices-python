import re
from pathlib import Path
from labeled_matrix import LabeledMatrix

class Admissions:
    def __init__(self):
        pass

    # ------------------------------- V1 ---------------------------------------
    def admit_v1(self, gpa: float, sat: float, extracurric: float) -> float:
        return gpa * 0.6 + sat * 0.1 + extracurric * 0.15

    # ------------------------------- V2 ---------------------------------------
    # TODO Task 2: implement admit_v2

    # ------------------------------- V3 ---------------------------------------
    # TODO Task 3 & 4: implement likely_succeed, likely_contribute, admit_v3

    # ------------------------------- V4 ---------------------------------------
    # TODO Task 5: implement admit_v4

    # ------------------------------- V5 ---------------------------------------
    # TODO Task 6: implement helper class and admit_v5

    # -------------------------- Matrix Practice ---------------------------------
    @staticmethod
    def matrix_practice1() -> LabeledMatrix:
        """
        create a matrix that will be a result of multiplying:

                    Practice Matrix 1
                gpa     sat    extracurr  honors  awards
        Walter  3.5   1450.0     4.0        0       2
        Jesse   3.8   1350.0     3.2        1       1
        Gus     3.0   1250.0     5.0        0       5

                    Practice Matrix 2
                    fn1     fn2
        gpa         0.4     0.1
        sat         0.2     0.3
        extracurr   0.1     0.4
        honors      0.2     0.0
        awards      0.1     0.2
        """
        
        # TODO Task 7: create and multiply matrices
        return None

    @staticmethod
    def matrix_practice2() -> LabeledMatrix:
        """
        5 students by 2 params with 2 params by 3 functions

                    Practice Matrix 3
                    fn1     fn2     fn3
        isLeader    0.5     0.7     0.1
        isVarsity   0.5     0.3     0.9

                    Practice Matrix 4
                    isLeader    isVarsity
        Kratos      1           1
        Loki        0           0
        Odin        1           0
        Thor        0           1
        Heimdall    0           1
        """

        # TODO Task 7: create and multiply matrices
        return None

    @staticmethod
    def find_gpa_in_file(file_path: str) -> float:
        try:
            content = Path(file_path).read_text()
            match = re.search(r"GPA\s*:\s*\d+(\.\d+)?", content)
            if match:
                found = match.group()
                print("Match found:", found)
                parts = found.split(":")
                return float(parts[1])
        except Exception as e:
            print("Error reading file:", e)
        return -1.0


if __name__ == "__main__":
    # Example of creating a lambda object (like Java's Function)
    a = lambda n: n * 2
    print(a(5))

    # ------------------------------ Matrix Example -----------------------------
    params = ["gpa", "sat", "extracurric"]
    students = ["Student 1", "Student 2"]
    functions = ["likelySucceed", "likelyWellRounded", "likelyContribute"]

    # Option 1: manual creation
    mat1 = LabeledMatrix(students, params, 3.5, 1450.0, 4.0, 3.8, 1350.0, 3.2)
    mat2 = LabeledMatrix(params, functions, 0.75, 0.5, 0.3, 0.25, 0.35, 0, 0, 0.15, 0.7)

    # Option 2: load from CSV
    mat3 = LabeledMatrix(students, params, "data/StudentMatrix.csv")
    mat4 = LabeledMatrix(params, functions, "data/FunctionMatrix.csv")

    # Option 3: create empty and set rows/columns
    mat5 = LabeledMatrix(students, params)
    mat5.set_row(0, [3.5, 1450, 4.0])
    mat5.set_row(1, [3.8, 1350, 3.2])

    mat6 = LabeledMatrix(params, functions)
    mat6.set_col(0, [0.75, 0.25, 0])
    mat6.set_col(1, [0.5, 0.35, 0.15])
    mat6.set_col(2, [0.3, 0.0, 0.7])

    # Matrix multiplication (order matters)
    res = LabeledMatrix.multiply_matrices(mat1, mat2)
    res2 = LabeledMatrix.multiply_matrices(mat3, mat4)
    res3 = LabeledMatrix.multiply_matrices(mat5, mat6)
    print(res)
    print(res2)
    print(res3)

    # ------------------------------- Task 9 -----------------------------------
    regex_path = ""  # TODO: put correct path
    gpa = Admissions.find_gpa_in_file(regex_path)
    print(gpa)