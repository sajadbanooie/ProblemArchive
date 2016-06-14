# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

import webbrowser

from PyQt5 import QtCore, QtWidgets

from ProblemArchive.db import *


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(690, 664)
        TabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.problem_tab = QtWidgets.QWidget()
        self.problem_tab.setObjectName("problem_tab")
        self.groupBox = QtWidgets.QGroupBox(self.problem_tab)
        self.groupBox.setGeometry(QtCore.QRect(330, 430, 341, 191))
        self.groupBox.setObjectName("groupBox")
        self.p_search_name = QtWidgets.QLineEdit(self.groupBox)
        self.p_search_name.setGeometry(QtCore.QRect(80, 30, 251, 27))
        self.p_search_name.setObjectName("p_search_name")
        self.p_search_tags = QtWidgets.QPlainTextEdit(self.groupBox)
        self.p_search_tags.setGeometry(QtCore.QRect(80, 70, 251, 78))
        self.p_search_tags.setObjectName("p_search_tags")
        self.p_check_name = QtWidgets.QCheckBox(self.groupBox)
        self.p_check_name.setGeometry(QtCore.QRect(10, 30, 71, 22))
        self.p_check_name.setObjectName("p_check_name")
        self.p_check_diff = QtWidgets.QCheckBox(self.groupBox)
        self.p_check_diff.setGeometry(QtCore.QRect(10, 160, 97, 22))
        self.p_check_diff.setObjectName("p_check_diff")
        self.p_check_tags = QtWidgets.QCheckBox(self.groupBox)
        self.p_check_tags.setGeometry(QtCore.QRect(10, 70, 61, 22))
        self.p_check_tags.setObjectName("p_check_tags")
        self.p_search_diff = QtWidgets.QSpinBox(self.groupBox)
        self.p_search_diff.setGeometry(QtCore.QRect(130, 160, 48, 27))
        self.p_search_diff.setObjectName("p_search_diff")
        self.go = QtWidgets.QPushButton(self.groupBox)
        self.go.setGeometry(QtCore.QRect(210, 160, 99, 27))
        self.go.setObjectName("go")
        self.groupBox_2 = QtWidgets.QGroupBox(self.problem_tab)
        self.groupBox_2.setGeometry(QtCore.QRect(330, 10, 351, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.p_name = QtWidgets.QLineEdit(self.groupBox_2)
        self.p_name.setGeometry(QtCore.QRect(70, 30, 261, 27))
        self.p_name.setObjectName("p_name")
        self.p_url = QtWidgets.QLineEdit(self.groupBox_2)
        self.p_url.setGeometry(QtCore.QRect(70, 70, 261, 27))
        self.p_url.setObjectName("p_url")
        self.p_diff = QtWidgets.QSpinBox(self.groupBox_2)
        self.p_diff.setGeometry(QtCore.QRect(90, 110, 48, 27))
        self.p_diff.setObjectName("p_diff")
        self.p_story = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.p_story.setGeometry(QtCore.QRect(70, 150, 261, 121))
        self.p_story.setObjectName("p_story")
        self.p_tags = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.p_tags.setGeometry(QtCore.QRect(70, 280, 261, 91))
        self.p_tags.setObjectName("p_tags")
        self.p_open = QtWidgets.QPushButton(self.groupBox_2)
        self.p_open.setGeometry(QtCore.QRect(10, 380, 121, 27))
        self.p_open.setObjectName("p_open")
        self.p_delete = QtWidgets.QPushButton(self.groupBox_2)
        self.p_delete.setGeometry(QtCore.QRect(130, 380, 99, 27))
        self.p_delete.setObjectName("p_delet")
        self.p_save = QtWidgets.QPushButton(self.groupBox_2)
        self.p_save.setGeometry(QtCore.QRect(230, 380, 99, 27))
        self.p_save.setObjectName("p_save")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 67, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 67, 17))
        self.label_5.setObjectName("label_5")
        self.p_solved = QtWidgets.QCheckBox(self.groupBox_2)
        self.p_solved.setGeometry(QtCore.QRect(180, 110, 97, 22))
        self.p_solved.setObjectName("p_solved")
        self.p_reload = QtWidgets.QPushButton(self.problem_tab)
        self.p_reload.setGeometry(QtCore.QRect(40, 560, 99, 27))
        self.p_reload.setObjectName("p_reload")
        self.p_sort_diff = QtWidgets.QPushButton(self.problem_tab)
        self.p_sort_diff.setGeometry(QtCore.QRect(160, 560, 141, 27))
        self.p_sort_diff.setObjectName("p_sort_diff")
        self.p_sort_alpha = QtWidgets.QPushButton(self.problem_tab)
        self.p_sort_alpha.setGeometry(QtCore.QRect(160, 600, 141, 27))
        self.p_sort_alpha.setObjectName("p_sort_alpha")
        self.problem_list_view = QtWidgets.QListWidget(self.problem_tab)
        self.problem_list_view.setGeometry(QtCore.QRect(10, 10, 311, 541))
        self.problem_list_view.setObjectName("problem_list_view")
        TabWidget.addTab(self.problem_tab, "")
        self.contest_tab = QtWidgets.QWidget()
        self.contest_tab.setObjectName("contest_tab")
        self.contest_list_view = QtWidgets.QListWidget(self.contest_tab)
        self.contest_list_view.setGeometry(QtCore.QRect(10, 10, 301, 351))
        self.contest_list_view.setObjectName("contest_list_view")
        self.groupBox_3 = QtWidgets.QGroupBox(self.contest_tab)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 10, 341, 611))
        self.groupBox_3.setObjectName("groupBox_3")
        self.c_open = QtWidgets.QPushButton(self.groupBox_3)
        self.c_open.setGeometry(QtCore.QRect(188, 110, 121, 27))
        self.c_open.setObjectName("c_open")
        self.c_diff = QtWidgets.QSpinBox(self.groupBox_3)
        self.c_diff.setGeometry(QtCore.QRect(90, 110, 48, 27))
        self.c_diff.setObjectName("c_diff")
        self.c_name = QtWidgets.QLineEdit(self.groupBox_3)
        self.c_name.setGeometry(QtCore.QRect(70, 30, 261, 27))
        self.c_name.setObjectName("c_name")
        self.c_url = QtWidgets.QLineEdit(self.groupBox_3)
        self.c_url.setGeometry(QtCore.QRect(70, 70, 261, 27))
        self.c_url.setObjectName("c_url")
        self.c_tags = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.c_tags.setGeometry(QtCore.QRect(70, 150, 261, 91))
        self.c_tags.setObjectName("c_tags")
        self.c_problems = QtWidgets.QListWidget(self.groupBox_3)
        self.c_problems.setGeometry(QtCore.QRect(80, 260, 251, 251))
        self.c_problems.setObjectName("c_problems")
        self.problem_combo = QtWidgets.QComboBox(self.groupBox_3)
        self.problem_combo.setGeometry(QtCore.QRect(10, 520, 151, 27))
        self.problem_combo.setObjectName("problem_combo")
        self.c_addp = QtWidgets.QPushButton(self.groupBox_3)
        self.c_addp.setGeometry(QtCore.QRect(170, 520, 71, 27))
        self.c_addp.setObjectName("c_addp")
        self.c_delete_p = QtWidgets.QPushButton(self.groupBox_3)
        self.c_delete_p.setGeometry(QtCore.QRect(238, 520, 91, 27))
        self.c_delete_p.setObjectName("c_delete_p")
        self.c_delete = QtWidgets.QPushButton(self.groupBox_3)
        self.c_delete.setGeometry(QtCore.QRect(20, 560, 99, 27))
        self.c_delete.setObjectName("c_delete")
        self.c_save = QtWidgets.QPushButton(self.groupBox_3)
        self.c_save.setGeometry(QtCore.QRect(130, 560, 99, 27))
        self.c_save.setObjectName("c_save")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 67, 17))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 67, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 67, 17))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 150, 67, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 260, 71, 17))
        self.label_10.setObjectName("label_10")
        self.groupBox_4 = QtWidgets.QGroupBox(self.contest_tab)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 430, 311, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.c_search_name = QtWidgets.QLineEdit(self.groupBox_4)
        self.c_search_name.setGeometry(QtCore.QRect(80, 30, 221, 27))
        self.c_search_name.setObjectName("c_search_name")
        self.c_search_tags = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.c_search_tags.setGeometry(QtCore.QRect(80, 70, 221, 78))
        self.c_search_tags.setObjectName("c_search_tags")
        self.c_check_name = QtWidgets.QCheckBox(self.groupBox_4)
        self.c_check_name.setGeometry(QtCore.QRect(10, 30, 71, 22))
        self.c_check_name.setObjectName("c_check_name")
        self.c_check_diff = QtWidgets.QCheckBox(self.groupBox_4)
        self.c_check_diff.setGeometry(QtCore.QRect(10, 160, 97, 22))
        self.c_check_diff.setObjectName("c_check_diff")
        self.c_check_tags = QtWidgets.QCheckBox(self.groupBox_4)
        self.c_check_tags.setGeometry(QtCore.QRect(10, 70, 61, 22))
        self.c_check_tags.setObjectName("c_check_tags")
        self.c_search_diff = QtWidgets.QSpinBox(self.groupBox_4)
        self.c_search_diff.setGeometry(QtCore.QRect(130, 160, 48, 27))
        self.c_search_diff.setObjectName("c_search_diff")
        self.c_go = QtWidgets.QPushButton(self.groupBox_4)
        self.c_go.setGeometry(QtCore.QRect(200, 160, 99, 27))
        self.c_go.setObjectName("c_go")
        self.c_sort_diff = QtWidgets.QPushButton(self.contest_tab)
        self.c_sort_diff.setGeometry(QtCore.QRect(170, 370, 141, 27))
        self.c_sort_diff.setObjectName("c_sort_diff")
        self.c_sort_alpha = QtWidgets.QPushButton(self.contest_tab)
        self.c_sort_alpha.setGeometry(QtCore.QRect(20, 370, 141, 27))
        self.c_sort_alpha.setObjectName("c_sort_alpha")
        self.c_reload = QtWidgets.QPushButton(self.contest_tab)
        self.c_reload.setGeometry(QtCore.QRect(110, 400, 99, 27))
        self.c_reload.setObjectName("c_reload")
        TabWidget.addTab(self.contest_tab, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        self.p_reload.clicked.connect(self.p_do_reload)
        self.c_reload.clicked.connect(self.c_do_reload)
        self.p_sort_alpha.clicked.connect(self.p_do_reload_a_sorted)
        self.p_sort_diff.clicked.connect(self.p_do_reload_d_sorted)
        self.c_sort_alpha.clicked.connect(self.c_do_reload_a_sorted)
        self.c_sort_diff.clicked.connect(self.c_do_reload_d_sorted)
        self.p_save.clicked.connect(self.on_save)
        self.c_save.clicked.connect(self.on_csave)
        self.p_delete.clicked.connect(self.on_p_delete)
        self.c_delete.clicked.connect(self.on_c_delete)
        self.go.clicked.connect(self.p_search)
        self.c_go.clicked.connect(self.c_search)
        self.c_addp.clicked.connect(self.add_p_to_c)
        self.c_delete_p.clicked.connect(self.delete_p_c)
        self.c_open.clicked.connect(self.c_open_url)
        self.p_open.clicked.connect(self.p_open_url)
        self.problem_list_view.itemClicked.connect(self.on_problem_clicked)
        self.contest_list_view.itemClicked.connect(self.on_contest_clicked)
        self.p_do_reload()
        self.c_do_reload()

    def delete_p_c(self):
        for item in self.c_problems.selectedItems():
            self.c_problems.takeItem(self.c_problems.row(item))

    def p_open_url(self):
        webbrowser.open_new_tab("http://" + self.p_url.text())

    def c_open_url(self):
        webbrowser.open_new_tab("http://" + self.c_url.text())

    def add_p_to_c(self):
        self.c_problems.addItem(self.problem_combo.currentText())
        self.problem_combo.removeItem(0)

    def p_search(self):
        argvs = {'name': None, 'diff': None, 'tags': None}
        if self.p_check_name.isChecked():
            argvs['name'] = self.p_search_name.text()
        if self.p_check_diff.isChecked():
            argvs['diff'] = self.p_search_diff.value()
        if self.p_check_tags.isChecked():
            argvs['tags'] = self.p_search_tags.toPlainText()
        for child in self.groupBox_2.children():
            child.setDisabled(True)
        self.problem_list_view.clear()
        for p in problem_search(**argvs):
            self.problem_list_view.addItem(p.name)
        self.problem_list_view.addItem("add new...")

    def c_search(self):
        argvs = {'name': None, 'diff': None, 'tags': None}
        if self.c_check_name.isChecked():
            argvs['name'] = self.c_search_name.text()
        if self.c_check_diff.isChecked():
            argvs['diff'] = self.c_search_diff.value()
        if self.c_check_tags.isChecked():
            argvs['tags'] = self.c_search_tags.toPlainText()
        for child in self.groupBox_3.children():
            child.setDisabled(True)
        self.contest_list_view.clear()
        for p in contest_search(**argvs):
            self.contest_list_view.addItem(p.name)
        self.contest_list_view.addItem("add new...")

    def on_p_delete(self):
        with db_session:
            delete(p for p in Problem if p.name == self.p_name.text())
        self.p_do_reload()

    def on_c_delete(self):
        with db_session:
            delete(c for c in Problem if c.name == self.c_name.text())
        self.c_do_reload()

    def p_do_reload(self):
        for child in self.groupBox_2.children():
            child.setDisabled(True)
        self.problem_list_view.clear()
        for p in get_problems():
            self.problem_list_view.addItem(p.name)
        self.problem_list_view.addItem("add new...")

    def p_do_reload_a_sorted(self):
        for child in self.groupBox_2.children():
            child.setDisabled(True)
        self.problem_list_view.clear()
        for p in get_problems_a():
            self.problem_list_view.addItem(p.name)
        self.problem_list_view.addItem("add new...")

    def p_do_reload_d_sorted(self):
        for child in self.groupBox_2.children():
            child.setDisabled(True)
        self.problem_list_view.clear()
        for p in get_problems_d():
            self.problem_list_view.addItem(p.name)
        self.problem_list_view.addItem("add new...")

    def c_do_reload(self):
        for child in self.groupBox_3.children():
            child.setDisabled(True)
        self.contest_list_view.clear()
        for c in get_contests():
            self.contest_list_view.addItem(c.name)
        self.contest_list_view.addItem("add new...")

    def c_do_reload_a_sorted(self):
        for child in self.groupBox_3.children():
            child.setDisabled(True)
        self.contest_list_view.clear()
        for p in get_contests_a():
            self.contest_list_view.addItem(p.name)
        self.contest_list_view.addItem("add new...")

    def c_do_reload_d_sorted(self):
        for child in self.groupBox_3.children():
            child.setDisabled(True)
        self.contest_list_view.clear()
        for p in get_contests_d():
            self.contest_list_view.addItem(p.name)
        self.contest_list_view.addItem("add new...")

    def on_problem_clicked(self, item):
        for child in self.groupBox_2.children():
            child.setDisabled(False)
        self.selected = item.text()
        if self.selected != "add new...":
            with db_session:
                self.selected = get_problem(self.selected)
                self.p_save.setText("Save")
                self.p_delete.setDisabled(False)
                self.p_name.setText(self.selected.name)
                self.p_diff.setValue(self.selected.diff)
                self.p_url.setText(self.selected.url)
                self.p_tags.setPlainText(self.selected.tags)
                self.p_story.setPlainText(self.selected.story)
                self.p_solved.setChecked(self.selected.solved)
            return
        self.p_save.setText("Add")
        self.p_delete.setDisabled(True)
        self.p_name.setText("")
        self.p_diff.setValue(0)
        self.p_url.setText("")
        self.p_tags.setPlainText("")
        self.p_story.setPlainText("")

    def on_contest_clicked(self, item):
        for child in self.groupBox_3.children():
            child.setDisabled(False)
        self.selected = item.text()
        if self.selected != "add new...":
            with db_session:
                self.selected = get_contest(self.selected)
                self.c_save.setText("Save")
                self.c_delete.setDisabled(False)
                self.c_name.setText(self.selected.name)
                self.c_diff.setValue(self.selected.diff)
                self.c_url.setText(self.selected.url)
                self.c_tags.setPlainText(self.selected.tags)
                self.c_problems.clear()
                for p in self.selected.problems:
                    self.c_problems.addItem(p.name)
                self.problem_combo.clear()
                for p in get_unassigned_problems():
                    self.problem_combo.addItem(p.name)
            return
        self.c_save.setText("Add")
        self.c_delete.setDisabled(True)
        self.c_name.setText("")
        self.c_diff.setValue(0)
        self.c_url.setText("")
        self.c_tags.setPlainText("")
        self.c_problems.clear()
        self.problem_combo.clear()
        for p in get_unassigned_problems():
            self.problem_combo.addItem(p.name)

    @db_session
    def on_save(self):
        if self.selected == "add new...":
            add_problem(self.p_name.text(), self.p_diff.value(), self.p_url.text(), self.p_tags.toPlainText(),
                        self.p_story.toPlainText(), solved=self.p_solved.isChecked())
            print("he")
            # QtWidgets.QDialogButtonBox("Problem added").show()
        else:
            modify_problem(self.selected.name, self.p_name.text(), self.p_diff.value(), self.p_url.text(),
                           self.p_tags.toPlainText(),
                           self.p_story.toPlainText(), solved=self.p_solved.isChecked())
        self.p_do_reload()

    @db_session
    def on_csave(self):
        if self.selected == "add new...":
            add_contest(self.c_name.text(), self.c_diff.value(), self.c_url.text(), self.c_tags.toPlainText(),
                        [self.c_problems.item(i).text() for i in range(self.c_problems.count())])
            print("he")
            # QtWidgets.QDialogButtonBox("Problem added").show()
        else:
            modify_contest(self.selected.name, self.c_name.text(), self.c_diff.value(), self.c_url.text(), self.c_tags.toPlainText(),
                           [self.c_problems.item(i).text() for i in range(self.c_problems.count())])
        self.c_do_reload()

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "ProblemArchive"))
        self.groupBox.setTitle(_translate("TabWidget", "Search"))
        self.p_check_name.setText(_translate("TabWidget", "Name"))
        self.p_check_diff.setText(_translate("TabWidget", "Difficulty"))
        self.p_check_tags.setText(_translate("TabWidget", "Tags"))
        self.go.setText(_translate("TabWidget", "Go!"))
        self.groupBox_2.setTitle(_translate("TabWidget", "Problem"))
        self.p_tags.setPlaceholderText(_translate("TabWidget", "Seprate Tags with \',\'"))
        self.p_open.setText(_translate("TabWidget", "Open in browser"))
        self.p_delete.setText(_translate("TabWidget", "Delete"))
        self.p_save.setText(_translate("TabWidget", "Save"))
        self.label.setText(_translate("TabWidget", "Name"))
        self.label_2.setText(_translate("TabWidget", "Url"))
        self.label_3.setText(_translate("TabWidget", "Difficulty"))
        self.label_4.setText(_translate("TabWidget", "Story"))
        self.label_5.setText(_translate("TabWidget", "Tags"))
        self.p_solved.setText(_translate("TabWidget", "Solved"))
        self.p_reload.setText(_translate("TabWidget", "Reload all"))
        self.p_sort_diff.setText(_translate("TabWidget", "Sort by Difficulty"))
        self.p_sort_alpha.setText(_translate("TabWidget", "Sort alphabetically"))
        TabWidget.setTabText(TabWidget.indexOf(self.problem_tab), _translate("TabWidget", "Problems"))
        self.groupBox_3.setTitle(_translate("TabWidget", "Contest"))
        self.c_open.setText(_translate("TabWidget", "Open in browser"))
        self.c_tags.setPlaceholderText(_translate("TabWidget", "Seprate Tags with \',\'"))
        self.c_addp.setText(_translate("TabWidget", "Add"))
        self.c_delete_p.setText(_translate("TabWidget", "Delete"))
        self.c_delete.setText(_translate("TabWidget", "Delete"))
        self.c_save.setText(_translate("TabWidget", "Save"))
        self.label_6.setText(_translate("TabWidget", "Name"))
        self.label_7.setText(_translate("TabWidget", "Url"))
        self.label_8.setText(_translate("TabWidget", "Difficulty"))
        self.label_9.setText(_translate("TabWidget", "Tags"))
        self.label_10.setText(_translate("TabWidget", "Problems"))
        self.groupBox_4.setTitle(_translate("TabWidget", "Search"))
        self.c_check_name.setText(_translate("TabWidget", "Name"))
        self.c_check_diff.setText(_translate("TabWidget", "Difficulty"))
        self.c_check_tags.setText(_translate("TabWidget", "Tags"))
        self.c_go.setText(_translate("TabWidget", "Go!"))
        self.c_sort_diff.setText(_translate("TabWidget", "Sort by Difficulty"))
        self.c_sort_alpha.setText(_translate("TabWidget", "Sort alphabetically"))
        self.c_reload.setText(_translate("TabWidget", "Reload all"))
        TabWidget.setTabText(TabWidget.indexOf(self.contest_tab), _translate("TabWidget", "Contests"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = Ui_TabWidget()
    ui.setupUi(TabWidget)
    TabWidget.show()
    sys.exit(app.exec_())
