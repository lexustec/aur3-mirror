# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './src/mainw.ui'
#
# Created: Sun Dec 26 11:27:38 2010
#      by: PyQt4 UI code generator 4.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainW(object):
    def setupUi(self, MainW):
        MainW.setObjectName(_fromUtf8("MainW"))
        MainW.resize(516, 400)
        MainW.setWindowTitle(_fromUtf8("FeSTige"))
        self.centralwidget = QtGui.QWidget(MainW)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.listVST = QtGui.QTableWidget(self.groupBox)
        self.listVST.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listVST.setProperty(_fromUtf8("showDropIndicator"), False)
        self.listVST.setDragDropOverwriteMode(False)
        self.listVST.setAlternatingRowColors(True)
        self.listVST.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.listVST.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.listVST.setObjectName(_fromUtf8("listVST"))
        self.listVST.setColumnCount(2)
        self.listVST.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.listVST.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.listVST.setHorizontalHeaderItem(1, item)
        self.listVST.horizontalHeader().setStretchLastSection(True)
        self.listVST.verticalHeader().setVisible(False)
        self.listVST.verticalHeader().setDefaultSectionSize(22)
        self.listVST.verticalHeader().setMinimumSectionSize(8)
        self.verticalLayout.addWidget(self.listVST)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.line_cmd = QtGui.QLineEdit(self.groupBox)
        self.line_cmd.setAcceptDrops(False)
        self.line_cmd.setObjectName(_fromUtf8("line_cmd"))
        self.horizontalLayout_2.addWidget(self.line_cmd)
        self.b_copy = QtGui.QPushButton(self.groupBox)
        self.b_copy.setMaximumSize(QtCore.QSize(22, 22))
        self.b_copy.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/edit-copy.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_copy.setIcon(icon)
        self.b_copy.setObjectName(_fromUtf8("b_copy"))
        self.horizontalLayout_2.addWidget(self.b_copy)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.b_launch = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/arrow-right.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_launch.setIcon(icon1)
        self.b_launch.setDefault(True)
        self.b_launch.setObjectName(_fromUtf8("b_launch"))
        self.horizontalLayout.addWidget(self.b_launch)
        self.b_ladish = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/list-add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_ladish.setIcon(icon2)
        self.b_ladish.setObjectName(_fromUtf8("b_ladish"))
        self.horizontalLayout.addWidget(self.b_ladish)
        self.b_info = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/dialog-information.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_info.setIcon(icon3)
        self.b_info.setObjectName(_fromUtf8("b_info"))
        self.horizontalLayout.addWidget(self.b_info)
        self.b_delete = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_delete.setIcon(icon4)
        self.b_delete.setObjectName(_fromUtf8("b_delete"))
        self.horizontalLayout.addWidget(self.b_delete)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.b_refresh = QtGui.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/view-refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.b_refresh.setIcon(icon5)
        self.b_refresh.setObjectName(_fromUtf8("b_refresh"))
        self.horizontalLayout.addWidget(self.b_refresh)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainW.setCentralWidget(self.centralwidget)
        self.menuBar = QtGui.QMenuBar(MainW)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 516, 20))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menu_Edit = QtGui.QMenu(self.menuBar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        self.menu_Help = QtGui.QMenu(self.menuBar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_File = QtGui.QMenu(self.menuBar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        MainW.setMenuBar(self.menuBar)
        self.statusBar = QtGui.QStatusBar(MainW)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainW.setStatusBar(self.statusBar)
        self.act_about = QtGui.QAction(MainW)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_about.setIcon(icon6)
        self.act_about.setObjectName(_fromUtf8("act_about"))
        self.act_launch = QtGui.QAction(MainW)
        self.act_launch.setIcon(icon1)
        self.act_launch.setObjectName(_fromUtf8("act_launch"))
        self.act_delete = QtGui.QAction(MainW)
        self.act_delete.setIcon(icon4)
        self.act_delete.setObjectName(_fromUtf8("act_delete"))
        self.act_refresh = QtGui.QAction(MainW)
        self.act_refresh.setIcon(icon5)
        self.act_refresh.setObjectName(_fromUtf8("act_refresh"))
        self.act_pref = QtGui.QAction(MainW)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/configure.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_pref.setIcon(icon7)
        self.act_pref.setObjectName(_fromUtf8("act_pref"))
        self.act_open = QtGui.QAction(MainW)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/document-open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_open.setIcon(icon8)
        self.act_open.setObjectName(_fromUtf8("act_open"))
        self.act_quit = QtGui.QAction(MainW)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.act_quit.setIcon(icon9)
        self.act_quit.setObjectName(_fromUtf8("act_quit"))
        self.act_ladish = QtGui.QAction(MainW)
        self.act_ladish.setIcon(icon2)
        self.act_ladish.setObjectName(_fromUtf8("act_ladish"))
        self.act_info = QtGui.QAction(MainW)
        self.act_info.setIcon(icon3)
        self.act_info.setObjectName(_fromUtf8("act_info"))
        self.menu_Edit.addAction(self.act_launch)
        self.menu_Edit.addAction(self.act_ladish)
        self.menu_Edit.addAction(self.act_info)
        self.menu_Edit.addAction(self.act_delete)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.act_refresh)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.act_pref)
        self.menu_Help.addAction(self.act_about)
        self.menu_File.addAction(self.act_open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.act_quit)
        self.menuBar.addAction(self.menu_File.menuAction())
        self.menuBar.addAction(self.menu_Edit.menuAction())
        self.menuBar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainW)
        QtCore.QObject.connect(self.act_quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainW.close)
        QtCore.QMetaObject.connectSlotsByName(MainW)

    def retranslateUi(self, MainW):
        self.groupBox.setStatusTip(QtGui.QApplication.translate("MainW", "List of plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainW", "List of Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.listVST.setSortingEnabled(True)
        self.listVST.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainW", "Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.listVST.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainW", "Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStatusTip(QtGui.QApplication.translate("MainW", "Final command executed in order to launch the plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainW", "Final command:", None, QtGui.QApplication.UnicodeUTF8))
        self.line_cmd.setStatusTip(QtGui.QApplication.translate("MainW", "Final command executed in order to launch the plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.b_copy.setToolTip(QtGui.QApplication.translate("MainW", "Copy the command to the buffer", None, QtGui.QApplication.UnicodeUTF8))
        self.b_copy.setStatusTip(QtGui.QApplication.translate("MainW", "Copy the command to the buffer", None, QtGui.QApplication.UnicodeUTF8))
        self.b_launch.setStatusTip(QtGui.QApplication.translate("MainW", "Launch the selected plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.b_launch.setText(QtGui.QApplication.translate("MainW", "&Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.b_ladish.setStatusTip(QtGui.QApplication.translate("MainW", "Add this plugin to the current ladish studio", None, QtGui.QApplication.UnicodeUTF8))
        self.b_ladish.setText(QtGui.QApplication.translate("MainW", "&Add to Ladish", None, QtGui.QApplication.UnicodeUTF8))
        self.b_info.setStatusTip(QtGui.QApplication.translate("MainW", "Show information about this plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.b_info.setText(QtGui.QApplication.translate("MainW", "&Info", None, QtGui.QApplication.UnicodeUTF8))
        self.b_delete.setStatusTip(QtGui.QApplication.translate("MainW", "Delete the selected plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.b_delete.setText(QtGui.QApplication.translate("MainW", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.b_refresh.setStatusTip(QtGui.QApplication.translate("MainW", "Refresh the list of plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.b_refresh.setText(QtGui.QApplication.translate("MainW", "&Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainW", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainW", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainW", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about.setText(QtGui.QApplication.translate("MainW", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.act_about.setStatusTip(QtGui.QApplication.translate("MainW", "About FeSTige", None, QtGui.QApplication.UnicodeUTF8))
        self.act_launch.setText(QtGui.QApplication.translate("MainW", "&Launch", None, QtGui.QApplication.UnicodeUTF8))
        self.act_launch.setStatusTip(QtGui.QApplication.translate("MainW", "Launch the selected plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.act_launch.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+L", None, QtGui.QApplication.UnicodeUTF8))
        self.act_delete.setText(QtGui.QApplication.translate("MainW", "&Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.act_delete.setStatusTip(QtGui.QApplication.translate("MainW", "Delete the selected plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.act_refresh.setText(QtGui.QApplication.translate("MainW", "&Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.act_refresh.setStatusTip(QtGui.QApplication.translate("MainW", "Refresh the list of plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.act_refresh.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.act_pref.setText(QtGui.QApplication.translate("MainW", "&Preferences", None, QtGui.QApplication.UnicodeUTF8))
        self.act_pref.setStatusTip(QtGui.QApplication.translate("MainW", "Configure FeSTige", None, QtGui.QApplication.UnicodeUTF8))
        self.act_pref.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.act_open.setText(QtGui.QApplication.translate("MainW", "Open...", None, QtGui.QApplication.UnicodeUTF8))
        self.act_open.setStatusTip(QtGui.QApplication.translate("MainW", "Open a specific plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.act_open.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.act_quit.setText(QtGui.QApplication.translate("MainW", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.act_quit.setStatusTip(QtGui.QApplication.translate("MainW", "Quit FeSTige", None, QtGui.QApplication.UnicodeUTF8))
        self.act_quit.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.act_ladish.setText(QtGui.QApplication.translate("MainW", "&Add to Ladish", None, QtGui.QApplication.UnicodeUTF8))
        self.act_ladish.setStatusTip(QtGui.QApplication.translate("MainW", "Add this plugin to the current ladish studio", None, QtGui.QApplication.UnicodeUTF8))
        self.act_ladish.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+A", None, QtGui.QApplication.UnicodeUTF8))
        self.act_info.setText(QtGui.QApplication.translate("MainW", "&Info", None, QtGui.QApplication.UnicodeUTF8))
        self.act_info.setStatusTip(QtGui.QApplication.translate("MainW", "Show information about this plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.act_info.setShortcut(QtGui.QApplication.translate("MainW", "Ctrl+I", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc
