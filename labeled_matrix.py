from typing import List, Optional
import csv


class LabeledMatrix:
    def __init__(self, row_labels: List[str], col_labels: List[str], *vals_or_filename):
        self.row_labels = row_labels
        self.col_labels = col_labels
        self.values = [[0.0 for _ in col_labels] for _ in row_labels]

        # If no extra args, create empty matrix
        if len(vals_or_filename) == 0:
            return

        # If a single string argument, treat it as filename (CSV)
        if len(vals_or_filename) == 1 and isinstance(vals_or_filename[0], str):
            filename = vals_or_filename[0]
            self._init_from_csv(filename)
            return

        # Otherwise expect numeric vals (flat)
        vals = list(vals_or_filename)
        total_size = len(row_labels) * len(col_labels)
        if len(vals) != total_size:
            raise RuntimeError(f"Labeled Matrix expected {total_size} values but {len(vals)} were given.")
        ncols = len(col_labels)
        for i, v in enumerate(vals):
            r = i // ncols
            c = i % ncols
            self.values[r][c] = float(v)

    def _init_from_csv(self, filename: str):
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
        if len(rows) != len(self.row_labels):
            raise RuntimeError(f"Wrong number of rows in CSV file {filename}")
        for i, row in enumerate(rows):
            if len(row) != len(self.col_labels):
                raise RuntimeError(f"Wrong number of columns in row {i+1} in CSV file {filename}")
            self.values[i] = [float(x) for x in row]

    def set_val(self, row: int, col: int, value: float):
        self.values[row][col] = float(value)

    def get_val(self, row: int, col: int) -> float:
        return self.values[row][col]

    def get_rows(self) -> int:
        return len(self.row_labels)

    def get_cols(self) -> int:
        return len(self.col_labels)

    def set_row(self, i: int, vals: List[float]):
        if len(vals) != len(self.values[i]):
            raise RuntimeError("Length of the matrix row and argument row are not the same")
        self.values[i] = [float(x) for x in vals]

    def set_col(self, j: int, vals: List[float]):
        if len(vals) != len(self.values):
            raise RuntimeError("Length of the matrix column and argument column are not the same")
        for i in range(len(self.values)):
            self.values[i][j] = float(vals[i])

    def __str__(self):
        sb = []
        sb.append("RowLabels: " + ", ".join(self.row_labels))
        sb.append("ColLabels: " + ", ".join(self.col_labels))
        for row in self.values:
            sb.append(" ".join(f"{v:.2f}" for v in row))
        return "\n".join(sb)

    def __eq__(self, other):
        if not isinstance(other, LabeledMatrix):
            return False
        if self.get_rows() != other.get_rows() or self.get_cols() != other.get_cols():
            return False
        tol = 1e-9
        for i in range(self.get_rows()):
            for j in range(self.get_cols()):
                if abs(self.values[i][j] - other.values[i][j]) > tol:
                    return False
        return True

    @staticmethod
    def multiply_matrices(a: 'LabeledMatrix', b: 'LabeledMatrix') -> 'LabeledMatrix':
        if a.get_cols() != b.get_rows():
            raise ValueError("Matrix a needs to have as many columns as matrix b has rows.")
        res = LabeledMatrix(a.row_labels, b.col_labels)
        for row_a in range(a.get_rows()):
            for col_b in range(b.get_cols()):
                dot = 0.0
                for k in range(a.get_cols()):
                    dot += a.get_val(row_a, k) * b.get_val(k, col_b)
                res.set_val(row_a, col_b, dot)
        return res