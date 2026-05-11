# -*- coding: utf-8 -*-
"""
QGIS 3.x(PyQt5) / QGIS 4.x(PyQt6) 겸용: 열거형·폰트 메트릭·QAction 위치 차이를 한곳에서 처리.
(https://github.com/qgis/QGIS/wiki/Plugin-migration-to-be-compatible-with-Qt5-and-Qt6)
"""
from qgis.core import Qgis, QgsFeatureRequest, QgsTask, QgsWkbTypes

try:
    from qgis.PyQt.QtGui import QAction
except ImportError:
    from qgis.PyQt.QtWidgets import QAction

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QAbstractItemView, QComboBox, QCompleter


def font_metrics_horizontal_advance(font_metrics, text):
    """Qt6: horizontalAdvance만 제공. getattr(..., fm.width)는 기본값 평가 시 Qt6에서 깨짐."""
    if hasattr(font_metrics, "horizontalAdvance"):
        return font_metrics.horizontalAdvance(text)
    return font_metrics.width(text)


# --- QtCore.Qt ---
_ItemDataRole = getattr(Qt, "ItemDataRole", None)
Qt_UserRole = _ItemDataRole.UserRole if _ItemDataRole else Qt.UserRole
Qt_UserRole1 = Qt_UserRole + 1
Qt_DisplayRole = _ItemDataRole.DisplayRole if _ItemDataRole else Qt.DisplayRole
_CursorShape = getattr(Qt, "CursorShape", None)
Qt_WaitCursor = _CursorShape.WaitCursor if _CursorShape else Qt.WaitCursor
_CaseSensitivity = getattr(Qt, "CaseSensitivity", None)
Qt_CaseInsensitive = _CaseSensitivity.CaseInsensitive if _CaseSensitivity else Qt.CaseInsensitive
_MatchFlag = getattr(Qt, "MatchFlag", None)
Qt_MatchContains = _MatchFlag.MatchContains if _MatchFlag else Qt.MatchContains
_DockWidgetArea = getattr(Qt, "DockWidgetArea", None)
Qt_LeftDockWidgetArea = _DockWidgetArea.LeftDockWidgetArea if _DockWidgetArea else Qt.LeftDockWidgetArea

# --- QGIS API ---
_qgis_ml = getattr(Qgis, "MessageLevel", None)
Qgis_Info = _qgis_ml.Info if _qgis_ml else Qgis.Info
Qgis_Warning = _qgis_ml.Warning if _qgis_ml else Qgis.Warning
Qgis_Critical = _qgis_ml.Critical if _qgis_ml else Qgis.Critical
_qgst_ts = getattr(QgsTask, "TaskStatus", None)
QgsTask_Running = _qgst_ts.Running if _qgst_ts else QgsTask.Running
_qgswkb_gt = getattr(QgsWkbTypes, "GeometryType", None)
QgsWkb_PointGeometry = _qgswkb_gt.PointGeometry if _qgswkb_gt else QgsWkbTypes.PointGeometry
_fr_flag = getattr(QgsFeatureRequest, "Flag", None)
QgsFeatureRequest_NoGeometry = _fr_flag.NoGeometry if _fr_flag else QgsFeatureRequest.NoGeometry

# --- QtWidgets ---
_ip = getattr(QComboBox, "InsertPolicy", None)
QComboBox_NoInsert = _ip.NoInsert if _ip else QComboBox.NoInsert
_ssm = getattr(QAbstractItemView, "SelectionMode", None)
QAbstractItemView_SingleSelection = _ssm.SingleSelection if _ssm else QAbstractItemView.SingleSelection
_qc_cm = getattr(QCompleter, "CompletionMode", None)
QCompleter_PopupCompletion = _qc_cm.PopupCompletion if _qc_cm else QCompleter.PopupCompletion
