# -*- coding:utf-8 -*-
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from networkapiclient.ApiGenericClient import ApiGenericClient
from networkapiclient.utils import build_uri_with_ids


class ApiInterfaceRequest(ApiGenericClient):
	def __init__(self, networkapi_url, user, password, user_ldap=None, log_level='INFO'):
		"""Class constructor receives parameters to connect to the networkAPI.
		:param networkapi_url: URL to access the network API.
		:param user: User for authentication.
		:param password: Password for authentication.
		"""

		super(ApiInterfaceRequest, self).__init__(
			networkapi_url,
			user,
			password,
			user_ldap,
			log_level
		)

	def deploy_interface_config_sync(self, interface_id):
		"""
		"""

		uri = "api/interface/%s/deploy_config_sync/" % (interface_id)

		data = dict()

		return self.put(uri, data)

	def deploy_channel_config_sync(self, channel_id):
		"""
		"""

		uri = "api/interface/channel/%s/deploy_config_sync/" % (channel_id)

		data = dict()

		return self.put(uri, data)

	def remove_connection(self, interface1, interface2):
		"""Remove a connection between two interfaces"""

		uri = "api/interface/disconnect/%s/%s/" % (interface1, interface2)

		return self.delete(uri)


	def search(self, **kwargs):
		"""
		Method to search interfaces based on extends search.

		:param search: Dict containing QuerySets to find interfaces.
		:param include: Array containing fields to include on response.
		:param exclude: Array containing fields to exclude on response.
		:param fields:  Array containing fields to override default fields.
		:param kind: Determine if result will be detailed ('details') or basic ('basic').
		:return: Dict containing equipments
		"""

		return super(ApiInterfaceRequest, self).get(self.prepare_url('api/v3/interface/', kwargs))


	def get(self, ids, **kwargs):
		"""
		Method to get environments by their ids

		:param ids: List containing identifiers of environments
		:param include: Array containing fields to include on response.
		:param exclude: Array containing fields to exclude on response.
		:param fields: Array containing fields to override default fields.
		:param kind: Determine if result will be detailed ('detail') or basic ('basic').
		:return: Dict containing environments
		"""

		url = build_uri_with_ids('api/v3/interface/%s/', ids)

		return super(ApiInterfaceRequest, self).get(self.prepare_url(url, kwargs))