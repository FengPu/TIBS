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

import sys
class PosData:

    def __init__(self, name, did, desc, acc):
        self.acc = acc
        self.desc = desc
        self.name = name
        self.id = did
        self.__set_accountability()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

	def get_accountability(self):
        acc = {}
        acc['name'] = self.acc['name']
        acc['description'] = self.acc['description']
        return acc

    def __set_accountability(self):
        sys.path.append(self.acc["path"])

	def get_content(self):
		content = {}

        if (self.__check_accountiability()):
		    content['status'] = True
		    content['data'] = 'temporary access path or serialized content'
        else:
            content['status'] = False
            content['data'] = ''
        return content 

	def __check_accountiability(self):
        #if sucess return True, else return False
        #example_path
        #  = test_root_dir / publisher_1 / topicA / acc_fun / email_certification.py
        package = self.acc['path'].split('/')[-1].split('.')[0]
        acc_pkg = __import__(package)
        acc = acc_pkg.Accountiabilty() #convention: class name = Accountiability
        result = acc.run_accountiability()
		self.__log_accountiability(result)
		if result['success'] = True: 
            return True
		else:
            return False

	def __log_accountiability(self):
		pass
		