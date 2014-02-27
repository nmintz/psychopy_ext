import wx
import analyzer_gui
import analyzer_comps

class Analyzer( analyzer_gui.MyFrame ):
    def __init__( self, parent ):
        analyzer_gui.MyFrame.__init__( self, parent )

        self.window_canvas.frame = self
        self.list_data.window_canvas = self.window_canvas
        self.list_data.list_data_headers = self.list_data_headers
        self.button_addfiles.Bind(wx.EVT_BUTTON, self.OnFileButton)

        self.plot_type.Bind(wx.EVT_RADIOBOX, self.window_canvas.changePlot)
        self.err_type.Bind(wx.EVT_RADIOBOX, self.window_canvas.changePlot)

        self.list_data_headers.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)
        self.list_subplots.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)
        self.list_rows.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)
        self.list_cols.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)
        self.list_values.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)
        self.list_yerr.Bind(wx.EVT_LIST_DELETE_ITEM, self.window_canvas.changePlot)

        self.list_datafiles.Bind(wx.EVT_LIST_INSERT_ITEM, self.list_data.append_data)
        self.list_datafiles.Bind(wx.EVT_LIST_DELETE_ITEM, self.list_data.load_data)

    def OnFileButton(self, evt):
        dlg = wx.FileDialog(
            self, message="Choose data files",
            style=wx.OPEN | wx.MULTIPLE
            )

        if dlg.ShowModal() == wx.ID_OK:
            # This returns a Python list of files that were selected.
            paths = dlg.GetPaths()
            self.list_datafiles.add_items(paths)

        dlg.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = Analyzer(None)
    frame.Center()
    frame.Show()
    #frame.Maximize()
    app.MainLoop()

