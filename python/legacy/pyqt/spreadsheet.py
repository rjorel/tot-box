#!/usr/bin/env python3

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SpreadSheet(QWidget):
    _LABELS = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z'
    ]

    def __init__(self, rows, columns, clipboard, parent=None):
        super().__init__(parent)

        # Basic attributes.
        self._rows = rows
        self._columns = columns
        self._clipboard = clipboard

        # Table and shortcut configuration.
        self._table = QTableWidget(rows, columns)
        self._table.setHorizontalHeaderLabels(SpreadSheet._LABELS)

        QShortcut(QKeySequence('Ctrl+C'), self).activated.connect(self.copy)
        QShortcut(QKeySequence('Ctrl+V'), self).activated.connect(self.paste)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self._table)

        self.setMinimumSize(640, 480)
        self.setWindowTitle('SpreadSheet')

        self.show()

    def copy(self):
        indices = self._get_sorted_indices()

        if not indices:
            return

        self._put_in_clipboard(
            self._get_values(indices)
        )

    def _get_sorted_indices(self):
        return sorted([
            (index.column(), index.row())
            for index in self._table.selectedIndexes()
        ])

    def _get_values(self, indices: list):
        values = self._generate_values(indices)

        for index in indices:
            try:
                col = index[1] - indices[0][1]
                row = index[0] - indices[0][0]

                values[col][row] = self._table.item(index[1], index[0]).text()

            except AttributeError:
                pass

        return values

    @staticmethod
    def _generate_values(indices: list):
        if not indices:
            return []

        width = (indices[-1][0] - indices[0][0]) + 1
        height = (indices[-1][1] - indices[0][1]) + 1

        return [
            [''] * width for _ in range(0, height)
        ]

    def _put_in_clipboard(self, values: list):
        self._clipboard.setText(
            '\n'.join(['\t'.join(row) for row in values])
        )

    def paste(self):
        indices = self._get_sorted_indices()

        if not indices:
            return

        self._put_in_sheet_at(indices[0])

    def _put_in_sheet_at(self, index):
        for (row_index, row) in enumerate(self._get_rows_from_clipboard()):
            for (col_index, cell_value) in enumerate(self._get_cell_from_row(row)):
                self._table.setItem(
                    index[1] + row_index,
                    index[0] + col_index,
                    QTableWidgetItem(cell_value)
                )

    def _get_rows_from_clipboard(self):
        return self._clipboard.text().split('\n')

    @staticmethod
    def _get_cell_from_row(row):
        return row.split('\t')


if __name__ == '__main__':
    app = QApplication(sys.argv)

    spreadsheet = SpreadSheet(50, 26, app.clipboard())
    sys.exit(app.exec_())
