# Authors: Huzi Cheng <hzcheng15@icloud.com>
from hnn_core.gui.gui import run_hnn_gui


def test_run_gui():
    """Test if main gui function gives proper ipywidget"""
    gui = run_hnn_gui()
    assert gui is not None
