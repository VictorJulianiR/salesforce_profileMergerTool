# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main_window.ui',
# licensing of '.\main_window.ui' applies.
#
# Created: Wed Apr 24 11:59:27 2019
#      by: pyside2-uic  running on PySide2 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(667, 449)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.cmb_api = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_api.setMinimumSize(QtCore.QSize(44, 0))
        self.cmb_api.setObjectName("cmb_api")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.cmb_api.addItem("")
        self.horizontalLayout_3.addWidget(self.cmb_api)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.profileSource_selector_2 = QtWidgets.QWidget(self.centralwidget)
        self.profileSource_selector_2.setObjectName("profileSource_selector_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.profileSource_selector_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_source = QtWidgets.QLabel(self.profileSource_selector_2)
        self.lbl_source.setObjectName("lbl_source")
        self.horizontalLayout.addWidget(self.lbl_source)
        self.btn_source = QtWidgets.QToolButton(self.profileSource_selector_2)
        self.btn_source.setObjectName("btn_source")
        self.horizontalLayout.addWidget(self.btn_source)
        self.verticalLayout_2.addWidget(self.profileSource_selector_2)
        self.profileTarget_selector = QtWidgets.QHBoxLayout()
        self.profileTarget_selector.setObjectName("profileTarget_selector")
        self.lbl_target = QtWidgets.QLabel(self.centralwidget)
        self.lbl_target.setObjectName("lbl_target")
        self.profileTarget_selector.addWidget(self.lbl_target)
        self.btn_target = QtWidgets.QToolButton(self.centralwidget)
        self.btn_target.setObjectName("btn_target")
        self.profileTarget_selector.addWidget(self.btn_target)
        self.verticalLayout_2.addLayout(self.profileTarget_selector)
        spacerItem1 = QtWidgets.QSpacerItem(0, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.fields_selector = QtWidgets.QGridLayout()
        self.fields_selector.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.fields_selector.setContentsMargins(-1, -1, -1, 0)
        self.fields_selector.setObjectName("fields_selector")
        self.btn_addOne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addOne.setObjectName("btn_addOne")
        self.fields_selector.addWidget(self.btn_addOne, 4, 1, 1, 1)
        self.lbl_included = QtWidgets.QLabel(self.centralwidget)
        self.lbl_included.setObjectName("lbl_included")
        self.fields_selector.addWidget(self.lbl_included, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.fields_selector.addItem(spacerItem2, 1, 1, 1, 1)
        self.bar_loading = QtWidgets.QProgressBar(self.centralwidget)
        self.bar_loading.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bar_loading.sizePolicy().hasHeightForWidth())
        self.bar_loading.setSizePolicy(sizePolicy)
        self.bar_loading.setMinimumSize(QtCore.QSize(200, 0))
        self.bar_loading.setProperty("value", 69)
        self.bar_loading.setTextVisible(True)
        self.bar_loading.setInvertedAppearance(False)
        self.bar_loading.setObjectName("bar_loading")
        self.fields_selector.addWidget(self.bar_loading, 9, 0, 1, 3)
        self.lbl_allProfiles = QtWidgets.QLabel(self.centralwidget)
        self.lbl_allProfiles.setObjectName("lbl_allProfiles")
        self.fields_selector.addWidget(self.lbl_allProfiles, 0, 0, 1, 1)
        self.list_included = QtWidgets.QListWidget(self.centralwidget)
        self.list_included.setObjectName("list_included")
        QtWidgets.QListWidgetItem(self.list_included)
        self.fields_selector.addWidget(self.list_included, 1, 2, 8, 1)
        self.list_allProfiles = QtWidgets.QListWidget(self.centralwidget)
        self.list_allProfiles.setObjectName("list_allProfiles")
        QtWidgets.QListWidgetItem(self.list_allProfiles)
        QtWidgets.QListWidgetItem(self.list_allProfiles)
        QtWidgets.QListWidgetItem(self.list_allProfiles)
        self.fields_selector.addWidget(self.list_allProfiles, 1, 0, 8, 1)
        self.btn_rmvOne = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rmvOne.setObjectName("btn_rmvOne")
        self.fields_selector.addWidget(self.btn_rmvOne, 5, 1, 1, 1)
        self.btn_addAll = QtWidgets.QPushButton(self.centralwidget)
        self.btn_addAll.setObjectName("btn_addAll")
        self.fields_selector.addWidget(self.btn_addAll, 3, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.fields_selector.addItem(spacerItem3, 8, 1, 1, 1)
        self.btn_rmvAll = QtWidgets.QPushButton(self.centralwidget)
        self.btn_rmvAll.setObjectName("btn_rmvAll")
        self.fields_selector.addWidget(self.btn_rmvAll, 6, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.fields_selector)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.cmb_api.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cmb_api, self.btn_source)
        MainWindow.setTabOrder(self.btn_source, self.btn_target)
        MainWindow.setTabOrder(self.btn_target, self.list_allProfiles)
        MainWindow.setTabOrder(self.list_allProfiles, self.btn_addAll)
        MainWindow.setTabOrder(self.btn_addAll, self.btn_addOne)
        MainWindow.setTabOrder(self.btn_addOne, self.btn_rmvOne)
        MainWindow.setTabOrder(self.btn_rmvOne, self.btn_rmvAll)
        MainWindow.setTabOrder(self.btn_rmvAll, self.list_included)
        MainWindow.setTabOrder(self.list_included, self.btn_start)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SF Profile Migrator by @f1r3f0x", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Base Api Version:", None, -1))
        self.cmb_api.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "45", None, -1))
        self.cmb_api.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "44", None, -1))
        self.cmb_api.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "43", None, -1))
        self.cmb_api.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "42", None, -1))
        self.cmb_api.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "41", None, -1))
        self.cmb_api.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "40", None, -1))
        self.cmb_api.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "39", None, -1))
        self.cmb_api.setItemText(7, QtWidgets.QApplication.translate("MainWindow", "38", None, -1))
        self.cmb_api.setItemText(8, QtWidgets.QApplication.translate("MainWindow", "37", None, -1))
        self.cmb_api.setItemText(9, QtWidgets.QApplication.translate("MainWindow", "36", None, -1))
        self.cmb_api.setItemText(10, QtWidgets.QApplication.translate("MainWindow", "35", None, -1))
        self.cmb_api.setItemText(11, QtWidgets.QApplication.translate("MainWindow", "34", None, -1))
        self.cmb_api.setItemText(12, QtWidgets.QApplication.translate("MainWindow", "33", None, -1))
        self.cmb_api.setItemText(13, QtWidgets.QApplication.translate("MainWindow", "32", None, -1))
        self.cmb_api.setItemText(14, QtWidgets.QApplication.translate("MainWindow", "30", None, -1))
        self.lbl_source.setText(QtWidgets.QApplication.translate("MainWindow", "Profile Source:", None, -1))
        self.btn_source.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.lbl_target.setText(QtWidgets.QApplication.translate("MainWindow", "Profile Target:", None, -1))
        self.btn_target.setText(QtWidgets.QApplication.translate("MainWindow", "...", None, -1))
        self.btn_addOne.setText(QtWidgets.QApplication.translate("MainWindow", ">", None, -1))
        self.lbl_included.setText(QtWidgets.QApplication.translate("MainWindow", "Included Fields:", None, -1))
        self.lbl_allProfiles.setText(QtWidgets.QApplication.translate("MainWindow", "All Profile Fields:", None, -1))
        __sortingEnabled = self.list_included.isSortingEnabled()
        self.list_included.setSortingEnabled(False)
        self.list_included.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "Opportunity", None, -1))
        self.list_included.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.list_allProfiles.isSortingEnabled()
        self.list_allProfiles.setSortingEnabled(False)
        self.list_allProfiles.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "Account", None, -1))
        self.list_allProfiles.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "Contact", None, -1))
        self.list_allProfiles.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "Custom__c", None, -1))
        self.list_allProfiles.setSortingEnabled(__sortingEnabled)
        self.btn_rmvOne.setText(QtWidgets.QApplication.translate("MainWindow", "<", None, -1))
        self.btn_addAll.setText(QtWidgets.QApplication.translate("MainWindow", ">>", None, -1))
        self.btn_rmvAll.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.btn_start.setText(QtWidgets.QApplication.translate("MainWindow", "Start", None, -1))
