# lines_row.py
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

from gi.repository import Gtk

class LinesRow(Gtk.Box):

    def __init__(self, item):
        Gtk.Box.__init__(self)
        self.code = Gtk.Label.new()
        self.code.set_markup(item.code)
        self.code.show()
        self.name = Gtk.Label.new()
        self.name.set_markup(item.name)
        self.name.show()
        self.add(self.code)
        self.add(self.name)
        self.show()
        self.get_style_context().add_class(f"B_{item.code}")