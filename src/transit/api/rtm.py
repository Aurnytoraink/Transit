# rtm.py
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

from transit.api.help_request import Request
from transit.api.models import *
# from help_request import Request
# from models import *

class RTM:
    def __init__(self,app):
        self.request = Request()
        self.app = app

    def get_alerts(self):
        return self.request.get("getAlertes/FR/All")

    def get_lines(self,type):
        if type != "tram" and type != "metro" and type != "bus":
            return False
        result = self.request.get("getLines/"+type)
        return list(map(lambda x: Lignes(x), list(map(lambda x: result[x],result))))


# session = RTM()
# print(session.get_lines("bus")[4].code, session.get_lines("bus")[4].name)
# print(session.get_lines("metro")[0].code, session.get_lines("metro")[0].name)
# print(session.get_alerts())