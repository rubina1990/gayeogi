# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../ui/main.ui'
#
# Created: Wed Dec 15 07:32:49 2010
#      by: PyQt4 UI code generator 4.8.1
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
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.splitter = QtGui.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget_6 = QtGui.QWidget(self.splitter)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_6)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.artistFilter = QtGui.QLineEdit(self.widget_6)
        self.artistFilter.setObjectName(_fromUtf8("artistFilter"))
        self.verticalLayout_3.addWidget(self.artistFilter)
        self.artists = QtGui.QTreeWidget(self.widget_6)
        self.artists.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.artists.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.artists.setIndentation(0)
        self.artists.setItemsExpandable(False)
        self.artists.setColumnCount(3)
        self.artists.setObjectName(_fromUtf8("artists"))
        self.artists.headerItem().setText(0, _fromUtf8("1"))
        self.artists.headerItem().setText(1, _fromUtf8("2"))
        self.artists.headerItem().setText(2, _fromUtf8("3"))
        self.verticalLayout_3.addWidget(self.artists)
        self.widget_7 = QtGui.QWidget(self.splitter)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_7)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.albumFilter = QtGui.QLineEdit(self.widget_7)
        self.albumFilter.setObjectName(_fromUtf8("albumFilter"))
        self.verticalLayout_4.addWidget(self.albumFilter)
        self.albums = QtGui.QTreeWidget(self.widget_7)
        self.albums.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.albums.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.albums.setIndentation(0)
        self.albums.setItemsExpandable(False)
        self.albums.setColumnCount(4)
        self.albums.setObjectName(_fromUtf8("albums"))
        self.albums.headerItem().setText(0, _fromUtf8("1"))
        self.albums.headerItem().setText(1, _fromUtf8("2"))
        self.albums.headerItem().setText(2, _fromUtf8("3"))
        self.albums.headerItem().setText(3, _fromUtf8("4"))
        self.verticalLayout_4.addWidget(self.albums)
        self.widget_8 = QtGui.QWidget(self.splitter)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.trackFilter = QtGui.QLineEdit(self.widget_8)
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
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget_4 = QtGui.QWidget(self.widget_3)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.logs = QtGui.QTreeWidget(self.widget_4)
        self.logs.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.logs.setAlternatingRowColors(True)
        self.logs.setIndentation(0)
        self.logs.setItemsExpandable(False)
        self.logs.setColumnCount(4)
        self.logs.setObjectName(_fromUtf8("logs"))
        self.logs.headerItem().setText(0, _fromUtf8("1"))
        self.logs.headerItem().setText(1, _fromUtf8("2"))
        self.logs.headerItem().setText(2, _fromUtf8("3"))
        self.logs.headerItem().setText(3, _fromUtf8("4"))
        self.verticalLayout_2.addWidget(self.logs)
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.clearLogs = QtGui.QPushButton(self.widget_5)
        self.clearLogs.setObjectName(_fromUtf8("clearLogs"))
        self.horizontalLayout_3.addWidget(self.clearLogs)
        self.saveLogs = QtGui.QPushButton(self.widget_5)
        self.saveLogs.setObjectName(_fromUtf8("saveLogs"))
        self.horizontalLayout_3.addWidget(self.saveLogs)
        spacerItem = QtGui.QSpacerItem(162, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.horizontalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtGui.QWidget(self.widget_3)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.formLayout_3 = QtGui.QFormLayout(self.widget_2)
        self.formLayout_3.setMargin(0)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.artistsStats = QtGui.QGroupBox(self.widget_2)
        self.artistsStats.setObjectName(_fromUtf8("artistsStats"))
        self.formLayout = QtGui.QFormLayout(self.artistsStats)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.artistsGreen = QtGui.QLabel(self.artistsStats)
        self.artistsGreen.setObjectName(_fromUtf8("artistsGreen"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.artistsGreen)
        self.frame_2 = QtGui.QFrame(self.artistsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_2.setStyleSheet(_fromUtf8("background-color: yellow;"))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.frame_2)
        self.artistsYellow = QtGui.QLabel(self.artistsStats)
        self.artistsYellow.setObjectName(_fromUtf8("artistsYellow"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.artistsYellow)
        self.frame_3 = QtGui.QFrame(self.artistsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_3.setStyleSheet(_fromUtf8("background-color: red;"))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.frame_3)
        self.artistsRed = QtGui.QLabel(self.artistsStats)
        self.artistsRed.setObjectName(_fromUtf8("artistsRed"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.artistsRed)
        self.frame = QtGui.QFrame(self.artistsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(30, 30))
        self.frame.setStyleSheet(_fromUtf8("background-color: green;"))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame)
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.artistsStats)
        self.albumsStats = QtGui.QGroupBox(self.widget_2)
        self.albumsStats.setObjectName(_fromUtf8("albumsStats"))
        self.formLayout_2 = QtGui.QFormLayout(self.albumsStats)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.frame_6 = QtGui.QFrame(self.albumsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_6.setStyleSheet(_fromUtf8("background-color: green;"))
        self.frame_6.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_6.setObjectName(_fromUtf8("frame_6"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.frame_6)
        self.albumsGreen = QtGui.QLabel(self.albumsStats)
        self.albumsGreen.setObjectName(_fromUtf8("albumsGreen"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.albumsGreen)
        self.frame_5 = QtGui.QFrame(self.albumsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_5.setStyleSheet(_fromUtf8("background-color: yellow;"))
        self.frame_5.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_5.setObjectName(_fromUtf8("frame_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.frame_5)
        self.albumsYellow = QtGui.QLabel(self.albumsStats)
        self.albumsYellow.setObjectName(_fromUtf8("albumsYellow"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.albumsYellow)
        self.frame_4 = QtGui.QFrame(self.albumsStats)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(30, 30))
        self.frame_4.setStyleSheet(_fromUtf8("background-color: red;"))
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName(_fromUtf8("frame_4"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.frame_4)
        self.albumsRed = QtGui.QLabel(self.albumsStats)
        self.albumsRed.setObjectName(_fromUtf8("albumsRed"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.albumsRed)
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.albumsStats)
        self.local = QtGui.QPushButton(self.widget_2)
        self.local.setObjectName(_fromUtf8("local"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.local)
        self.settings = QtGui.QPushButton(self.widget_2)
        self.settings.setObjectName(_fromUtf8("settings"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.settings)
        self.remote = QtGui.QPushButton(self.widget_2)
        self.remote.setObjectName(_fromUtf8("remote"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.remote)
        self.save = QtGui.QPushButton(self.widget_2)
        self.save.setObjectName(_fromUtf8("save"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.save)
        self.close = QtGui.QPushButton(self.widget_2)
        self.close.setObjectName(_fromUtf8("close"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.close)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.widget_3)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        self.artistFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair>=<column_name>:<searching_phrase>. Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.artists.setSortingEnabled(True)
        self.albumFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair>=<column_name>:<searching_phrase>. Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.albums.setSortingEnabled(True)
        self.trackFilter.setStatusTip(QtGui.QApplication.translate("main", "Pattern: <pair>|<pair>, where <pair>=<column_name>:<searching_phrase>. Case insensitive, regexp allowed.", None, QtGui.QApplication.UnicodeUTF8))
        self.tracks.setSortingEnabled(True)
        self.logs.setSortingEnabled(True)
        self.clearLogs.setStatusTip(QtGui.QApplication.translate("main", "Clear logs table", None, QtGui.QApplication.UnicodeUTF8))
        self.clearLogs.setText(QtGui.QApplication.translate("main", "Cle&ar", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLogs.setStatusTip(QtGui.QApplication.translate("main", "Save logs to file", None, QtGui.QApplication.UnicodeUTF8))
        self.saveLogs.setText(QtGui.QApplication.translate("main", "Sa&ve", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsStats.setTitle(QtGui.QApplication.translate("main", "Artists", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsGreen.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsYellow.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.artistsRed.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsStats.setTitle(QtGui.QApplication.translate("main", "Albums", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsGreen.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsYellow.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.albumsRed.setText(QtGui.QApplication.translate("main", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.local.setStatusTip(QtGui.QApplication.translate("main", "Refresh local filesystem", None, QtGui.QApplication.UnicodeUTF8))
        self.local.setText(QtGui.QApplication.translate("main", "&Local", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setStatusTip(QtGui.QApplication.translate("main", "Change settings", None, QtGui.QApplication.UnicodeUTF8))
        self.settings.setText(QtGui.QApplication.translate("main", "S&ettings", None, QtGui.QApplication.UnicodeUTF8))
        self.remote.setStatusTip(QtGui.QApplication.translate("main", "Refresh internet databases", None, QtGui.QApplication.UnicodeUTF8))
        self.remote.setText(QtGui.QApplication.translate("main", "&Remote", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setStatusTip(QtGui.QApplication.translate("main", "Save current database to disk.", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("main", "&Save", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setStatusTip(QtGui.QApplication.translate("main", "Close the application", None, QtGui.QApplication.UnicodeUTF8))
        self.close.setText(QtGui.QApplication.translate("main", "&Close", None, QtGui.QApplication.UnicodeUTF8))

