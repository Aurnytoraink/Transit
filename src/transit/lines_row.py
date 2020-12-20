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
        self.code_label = Gtk.Label.new()
        self.code_label.set_markup(f"<span size='x-large' font_weight='ultrabold'>{item.code}</span>")
        self.code_label.show()
        self.name = Gtk.Label.new()
        self.name.set_markup(f"<span font_weight='bold'>{item.name}</span>")
        self.name.show()
        self.box.add(self.code_label)
        self.box.add(self.name)
        self.box.set_border_width(5)
        self.box.show()
        self.add(self.box)
        self.show()
        self.get_style_context().add_class(f"B_{item.code}")

        self.item = item

class LinesListBox(Gtk.ListBox):

    def __init__(self,app):
        self.app = app
        self.old_class = ""
        Gtk.ListBox.__init__(self)
        self.connect("row-activated",self._on_child_clicked)
        self.show()

    def _on_child_clicked(self,arg,row):
        # row = self.get_activate_on_single_click()
        self.app.headerbar.set_title(f"{row.item.code} {row.item.name}")

        self.app.headerbar.get_style_context().remove_class(self.old_class)
        self.app.reload_btn.get_style_context().remove_class(self.old_class)
        self.app.headerbar.get_style_context().add_class(f"B_{row.item.code}")
        self.app.reload_btn.get_style_context().add_class(f"B_{row.item.code}")
        self.old_class = f"B_{row.item.code}"