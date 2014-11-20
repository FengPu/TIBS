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
#    pos_webapi.py
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

from flask import Flask, jsonify
from pos import Pos
from publisher import Publisher
from time import gmtime, strftime

import socket

app = Flask(__name__)

test_pos = Pos('./test_root_dir2/')

@app.errorhandler(404)
def not_found(error):
    return "404 NOT FOUND"

@app.route('/')
def home():
    return 'Hello TIBS'

@app.route('/publishers/', methods=['GET', 'HEAD'])
def get_publishers():
	publisher_list = []

	publishers = test_pos.get_publishers()
	
	for publisher in publishers:
		publisher_list.append({
			"publisher_id": publisher.get_id(),
			"publisher_name": publisher.get_name()
		})

	return jsonify(results=publisher_list)

@app.route('/topics/<publisher_id>/', methods=['GET'])
def get_topics(publisher_id):
	topic_list = []

	publishers = test_pos.get_publishers()
	
	for publisher in publishers:
		if publisher.get_id() == publisher_id:
			topics = publisher.get_topics()
			for topic in topics:
				data_list = topic.get_data()
				for data in data_list:
					topic_list.append({
						"topic_id": topic.get_id(),
						"topic_name": topic.get_name(),
						"topic_desc": data.get_description(),
						"accountibility_name": data.get_accountability()['name']
					})

	return jsonify(results=topic_list)

@app.route('/data_verify/<publisher_id>/<topic_id>', methods=['GET'])
def data_verify(publisher_id, topic_id):
	result = {}
	result["status"] = False
	'''for publisher in publishers:
		if publisher.get_id() == publisher_id:
			topics = publisher.get_topics()
			for topic in topics:
				if topic.get_id() == topic_id:'''

	return strftime("%a, %d %b %Y %X +0000", gmtime())

@app.route('/data_request/<data_key>/', methods=['GET'])
def data_request():
    pass

if __name__ == '__main__':

	
	
    # Start app
	app.run(host= socket.gethostbyname(socket.gethostname()), port=int("80"), debug=True)
