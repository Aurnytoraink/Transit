# models.py
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

# from transit.api.help_request import Request
# from help_request import Request

class Lignes():
    def __init__(self,item):
        self.id = item["id"]
        self.type = item["sqliType"]
        self.name = item["name"]
        self.code = item["PublicCode"]
        self.color = item["color"]
        self.is_night = item["night"]