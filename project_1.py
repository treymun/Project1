from PyQt5.QtWidgets import *
from project_view import *

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.NumberOfStudentsInput.setText('')
        self.StudentScoresInput.setText('')
        self.StudentGradesOutput.setText('')
        self.StudentGradesOutput_2.setText('')
        self.StudentGradesOutput_3.setText('')
        self.NumberOfStudentsLabel.adjustSize()
        self.NumberOfStudentsInput.adjustSize()
        self.StudentGradesOutput.adjustSize()
        self.StudentScoresInput.adjustSize()
        self.StudentGradesOutput_2.adjustSize()
        self.StudentGradesOutput_3.adjustSize()
        self.StudentsScoresLabel.adjustSize()
        self.GradingLayout.adjustSize()
        self.GradingLayout_3.adjustSize()
        self.GradingLayout_2.adjustSize()
        self.GradingLayout_4.adjustSize()
        self.GradingSchemeLabel.adjustSize()
        self.SubmitButton.clicked.connect(lambda: self.submit())
        self.ClearButton.clicked.connect(lambda: self.clear())
    def submit(self):
        self.student_num_input = self.NumberOfStudentsInput.text()
        self.student_num = int(self.student_num_input)
        self.StudentsScoresLabel.setText(f'{self.student_num} Students Scores:')
        self.score = self.StudentScoresInput.text()
        self.scores = [int(s) for s in self.score.split()]
        while True:
            if len(self.scores) < self.student_num:
                self.StudentScoresInput.clear()
                self.scores = [int(s) for s in self.score.split()]
            else:
                break
        self.score_total = self.scores[0]
        for i in range(self.student_num):
            if self.scores[i] > self.score_total:
                self.score_total = self.scores[i]
        self.score_total_1 = self.score_total

        self.grade = ''
        self.grade_2 = ''
        self.grade_3 = ''

        if len(self.scores) == 1:
            if self.scores[0] >= self.score_total - 10:
                self.grade = 'A'
            elif self.scores[0] >= self.score_total - 20:
                self.grade = 'B'
            elif self.scores[0] >= self.score_total - 30:
                self.grade = 'C'
            elif self.scores[0] >= self.score_total - 40:
                self.grade = 'D'
            else:
                self.grade = 'F'
        elif len(self.scores) == 2:
            if self.scores[0] >= self.score_total - 10:
                self.grade = 'A'
            elif self.scores[0] >= self.score_total - 20:
                self.grade = 'B'
            elif self.scores[0] >= self.score_total - 30:
                self.grade = 'C'
            elif self.scores[0] >= self.score_total - 40:
                self.grade = 'D'
            else:
                self.grade = 'F'
            if self.scores[1] >= self.score_total - 10:
                self.grade_2 = 'A'
            elif self.scores[1] >= self.score_total - 20:
                self.grade_2 = 'B'
            elif self.scores[1] >= self.score_total - 30:
                self.grade_2 = 'C'
            elif self.scores[1] >= self.score_total - 40:
                self.grade_2 = 'D'
            else:
                self.grade_2 = 'F'
        else:
            if self.scores[0] >= self.score_total - 10:
                self.grade = 'A'
            elif self.scores[0] >= self.score_total - 20:
                self.grade = 'B'
            elif self.scores[0] >= self.score_total - 30:
                self.grade = 'C'
            elif self.scores[0] >= self.score_total - 40:
                self.grade = 'D'
            else:
                self.grade = 'F'
            if self.scores[1] >= self.score_total - 10:
                self.grade_2 = 'A'
            elif self.scores[1] >= self.score_total - 20:
                self.grade_2 = 'B'
            elif self.scores[1] >= self.score_total - 30:
                self.grade_2 = 'C'
            elif self.scores[1] >= self.score_total - 40:
                self.grade_2 = 'D'
            else:
                self.grade_2 = 'F'
            if self.scores[2] >= self.score_total - 10:
                self.grade_3 = 'A'
            elif self.scores[2] >= self.score_total - 20:
                self.grade_3 = 'B'
            elif self.scores[2] >= self.score_total - 30:
                self.grade_3 = 'C'
            elif self.scores[2] >= self.score_total - 40:
                self.grade_3 = 'D'
            else:
                self.grade_3 = 'F'

        for i in range(self.student_num):
            if self.student_num == 1:
                self.score_total_final = self.score_total_1
                self.StudentGradesOutput.setText(f'Student {1} score is {self.scores[0]} and grade is {self.grade}')
            elif self.student_num == 2:
                self.score_total_final = self.score_total_1
                self.StudentGradesOutput.setText(f'Student {1} score is {self.scores[0]} and grade is {self.grade}')
                self.StudentGradesOutput_2.setText(f'Student {2} score is {self.scores[1]} and grade is {self.grade_2}')
            else:
                self.score_total_final = self.score_total_1
                self.StudentGradesOutput.setText(f'Student {1} score is {self.scores[0]} and grade is {self.grade}')
                self.StudentGradesOutput_2.setText(f'Student {2} score is {self.scores[1]} and grade is {self.grade_2}')
                self.StudentGradesOutput_3.setText(f'Student {3} score is {self.scores[2]} and grade is {self.grade_3}')
        self.NumberOfStudentsLabel.adjustSize()
        self.NumberOfStudentsInput.adjustSize()
        self.StudentGradesOutput.adjustSize()
        self.StudentScoresInput.adjustSize()
        self.StudentGradesOutput_2.adjustSize()
        self.StudentGradesOutput_3.adjustSize()
        self.StudentsScoresLabel.adjustSize()
        self.GradingLayout.adjustSize()
        self.GradingLayout_3.adjustSize()
        self.GradingLayout_2.adjustSize()
        self.GradingLayout_4.adjustSize()
        self.GradingSchemeLabel.adjustSize()

    def clear(self):
        self.NumberOfStudentsInput.clear()
        self.StudentScoresInput.clear()
        self.StudentsScoresLabel.setText("Student Scores:")
        self.StudentGradesOutput.clear()
        self.StudentGradesOutput_2.clear()
        self.StudentGradesOutput_3.clear()
