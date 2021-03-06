# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Tue Aug 30 23:13:27 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName(_fromUtf8("main"))
        main.resize(793, 588)
        self.verticalLayout = QtGui.QVBoxLayout(main)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(main)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_6 = QtGui.QWidget(self.splitter)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.artistFilter = QtGui.QLineEdit(self.widget_6)
        self.artistFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair> is <column_name>:<searching_phrase> or (not) (a or d or r). Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.artistFilter.setObjectName(_fromUtf8("artistFilter"))
        self.verticalLayout_3.addWidget(self.artistFilter)
        self.artists = QtGui.QTreeWidget(self.widget_6)
        self.artists.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.artists.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.artists.setIndentation(0)
        self.artists.setItemsExpandable(False)
        self.artists.setColumnCount(1)
        self.artists.setObjectName(_fromUtf8("artists"))
        self.artists.headerItem().setText(0, _fromUtf8("1"))
        self.verticalLayout_3.addWidget(self.artists)
        self.widget_7 = QtGui.QWidget(self.splitter)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.albumFilter = QtGui.QLineEdit(self.widget_7)
        self.albumFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair> is <column_name>:<searching_phrase> or (not) (a or d or r). Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.albumFilter.setObjectName(_fromUtf8("albumFilter"))
        self.verticalLayout_4.addWidget(self.albumFilter)
        self.widget_8 = QtGui.QWidget(self.splitter)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.trackFilter = QtGui.QLineEdit(self.widget_8)
        self.trackFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair> is <column_name>:<searching_phrase> or (not) (a or d or r). Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.trackFilter.setObjectName(_fromUtf8("trackFilter"))
        self.verticalLayout_5.addWidget(self.trackFilter)
        self.tracks = QtGui.QTreeWidget(self.widget_8)
        self.tracks.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tracks.setAlternatingRowColors(True)
        self.tracks.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.tracks.setIndentation(0)
        self.tracks.setItemsExpandable(False)
        self.tracks.setColumnCount(2)
        self.tracks.setObjectName(_fromUtf8("tracks"))
        self.tracks.headerItem().setText(0, _fromUtf8("1"))
        self.tracks.headerItem().setText(1, _fromUtf8("2"))
        self.verticalLayout_5.addWidget(self.tracks)
        self.horizontalLayout.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtGui.QWidget(main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 237))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.artistsStats = QtGui.QGroupBox(self.widget_3)
        self.artistsStats.setTitle(QtGui.QApplication.translate("main", "Artists", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsStats.setObjectName(_fromUtf8("artistsStats"))
        self.formLayout = QtGui.QFormLayout(self.artistsStats)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.artistsGreen = QtGui.QLabel(self.artistsStats)
        self.artistsGreen.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsGreen.setObjectName(_fromUtf8("artistsGreen"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.artistsGreen)
        self.artistsYellow = QtGui.QLabel(self.artistsStats)
        self.artistsYellow.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsYellow.setObjectName(_fromUtf8("artistsYellow"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.artistsYellow)
        self.artistsRed = QtGui.QLabel(self.artistsStats)
        self.artistsRed.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsRed.setObjectName(_fromUtf8("artistsRed"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.artistsRed)
        self.label = QtGui.QLabel(self.artistsStats)
        self.label.setMinimumSize(QtCore.QSize(30, 30))
        self.label.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setFrameShadow(QtGui.QFrame.Sunken)
        self.label.setText(QtGui.QApplication.translate("main", "a", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_3 = QtGui.QLabel(self.artistsStats)
        self.label_3.setMinimumSize(QtCore.QSize(30, 30))
        self.label_3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setText(QtGui.QApplication.translate("main", "d", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtGui.QLabel(self.artistsStats)
        self.label_4.setMinimumSize(QtCore.QSize(30, 30))
        self.label_4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setFrameShape(QtGui.QFrame.Box)
        self.label_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_4.setText(QtGui.QApplication.translate("main", "r", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3.addWidget(self.artistsStats)
        self.albumsStats = QtGui.QGroupBox(self.widget_3)
        self.albumsStats.setTitle(QtGui.QApplication.translate("main", "Albums", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsStats.setObjectName(_fromUtf8("albumsStats"))
        self.formLayout_2 = QtGui.QFormLayout(self.albumsStats)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.albumsStats)
        self.label_2.setMinimumSize(QtCore.QSize(30, 30))
        self.label_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtGui.QFrame.Box)
        self.label_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_2.setText(QtGui.QApplication.translate("main", "a", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.albumsGreen = QtGui.QLabel(self.albumsStats)
        self.albumsGreen.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsGreen.setObjectName(_fromUtf8("albumsGreen"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.albumsGreen)
        self.albumsYellow = QtGui.QLabel(self.albumsStats)
        self.albumsYellow.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsYellow.setObjectName(_fromUtf8("albumsYellow"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.albumsYellow)
        self.albumsRed = QtGui.QLabel(self.albumsStats)
        self.albumsRed.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsRed.setObjectName(_fromUtf8("albumsRed"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.albumsRed)
        self.label_5 = QtGui.QLabel(self.albumsStats)
        self.label_5.setMinimumSize(QtCore.QSize(30, 30))
        self.label_5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_5.setFont(font)
        self.label_5.setFrameShape(QtGui.QFrame.Box)
        self.label_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_5.setText(QtGui.QApplication.translate("main", "d", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtGui.QLabel(self.albumsStats)
        self.label_6.setMinimumSize(QtCore.QSize(30, 30))
        self.label_6.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.Box)
        self.label_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_6.setText(QtGui.QApplication.translate("main", "r", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_3.addWidget(self.albumsStats)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.local = QtGui.QPushButton(self.widget_3)
        self.local.setStatusTip(QtGui.QApplication.translate("main", "Refresh local filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.local.setText(QtGui.QApplication.translate("main", "&Local", None, QtGui.QApplication.UnicodeUTF8))
        self.local.setObjectName(_fromUtf8("local"))
        self.verticalLayout_6.addWidget(self.local)
        self.remote = QtGui.QPushButton(self.widget_3)
        self.remote.setStatusTip(QtGui.QApplication.translate("main", "Refresh internet databases", None, QtGui.QApplication.UnicodeUTF8))
        self.remote.setText(QtGui.QApplication.translate("main", "&Remote", None, QtGui.QApplication.UnicodeUTF8))
        self.remote.setObjectName(_fromUtf8("remote"))
        self.verticalLayout_6.addWidget(self.remote)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.settings = QtGui.QPushButton(self.widget_3)
        self.settings.setStatusTip(QtGui.QApplication.translate("main", "Change settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setText(QtGui.QApplication.translate("main", "S&ettings", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setObjectName(_fromUtf8("settings"))
        self.verticalLayout_7.addWidget(self.settings)
        self.save = QtGui.QPushButton(self.widget_3)
        self.save.setStatusTip(QtGui.QApplication.translate("main", "Save current database to disk.", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("main", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setObjectName(_fromUtf8("save"))
        self.verticalLayout_7.addWidget(self.save)
        self.close = QtGui.QPushButton(self.widget_3)
        self.close.setStatusTip(QtGui.QApplication.translate("main", "Close the application", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("main", "&Close", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setObjectName(_fromUtf8("close"))
        self.verticalLayout_7.addWidget(self.close)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        self.artists.setSortingEnabled(True)
        self.tracks.setSortingEnabled(True)

