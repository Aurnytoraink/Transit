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

class LinesRow(Gtk.ListBoxRow):

    def __init__(self, item):
        Gtk.ListBoxRow.__init__(self)
        self.box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL,5)
        self.code = Gtk.Label.new()
        self.code.set_markup(f"<span size='x-large' font_weight='ultrabold'>{item.code}</span>")
        self.code.show()
        self.name = Gtk.Label.new()
        self.name.set_markup(f"<span font_weight='bold'>{item.name}</span>")
        self.name.show()
        self.box.add(self.code)
        self.box.add(self.name)
        self.box.set_border_width(5)
        self.box.show()
        self.add(self.box)
        self.show()
        self.get_style_context().add_class(f"B_{item.code}")

        self.shortname = f"{item.code} {item.name}"

class LinesListBox(Gtk.ListBox):

    def __init__(self):
        Gtk.ListBox.__init__(self)
        self.connect("row-activated",self._on_child_clicked)
        self.show()

    def _on_child_clicked(self,arg,row):
        # row = self.get_activate_on_single_click()
        print(row.shortname)