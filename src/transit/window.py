# window.py
#
# Copyright 2020 Aurnytoraink
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sys import setdlopenflags
from gi.repository import Gtk, Handy
from threading import Thread
from transit.lines_row import LinesRow
from transit.api.rtm import RTM
from transit.task import TaskHelper

@Gtk.Template(resource_path='/com/github/Aurnytoraink/Transit/ui/window.ui')
class TransitWindow(Handy.ApplicationWindow):
    __gtype_name__ = 'TransitWindow'

    flowbox = Gtk.Template.Child()
    reload_btn = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reload_btn.connect("clicked",self.get_lines)
        
        self.session = RTM(self)
        self.task_helper = TaskHelper()

    def show_lines(self,lines):
        for i in range(len(lines))  :
            box = LinesRow(lines[i])
            self.flowbox.insert(box,i)

    def get_lines(self,*_):
        for child in self.flowbox.get_children():
            child.destroy()
        self.thread = self.task_helper.run(self.session.get_lines,"bus",callback=(self.show_lines,))