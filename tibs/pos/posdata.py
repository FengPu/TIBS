# -*- coding: utf-8 -*-
#    This file is part of POS with TIBS.
#
#    POS with TIBS is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    POS with TIBS is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with POS with TIBS.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
# Module Name:
#
#    topic.py
#
# Abstract:
#
# Author:
#
#    Project Manager : Feng-Pu Yabg
#    Core Team Member: Bai-Small
#
# Project:
#
#    OpenISDM
#
# -*-

class PosData:

	def __init__(self, data_name, data_id, desc, acc):
		print "name is:" + data_name
		print "id is:" + data_id
		print "desc is:" + desc
		print acc
		
		self.name = data_name
		self.id = data_id
		self.desc = desc
		self.acc = acc


	def get_id(self):
		return self.id

	def get_name(self):
		return self.name

	def get_description(self):
		return self.desc

	def get_accountability(self):
		return self.acc

	def get_content(self):
		content = {}

		if (self.__check_accountiability()):
			content['status'] = True
			content['data'] = 'temporary access path or \
		                       serialized content'
		else:
			content['status'] = False
			content['data'] = ''

		return content

	def __check_accountiability(self):

		self.__log_accountiability()
		#if sucess return True, else return False
		return True

	def __log_accountiability(self):
		pass
