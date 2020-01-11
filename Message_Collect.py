#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-03 19:03:28
# @Author  : Awrrays 
# @Link    : http://cnblogs.com/Awrrays
# @Version : 1.0

import requests
import nmap
import json
import re

def geting_ip(target):

	Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	ip_list = []


	get_token = 'http://site.ip138.com/' + target
	get_token_data = requests.get(get_token, headers=Headers)
	get_token_pat = "var _TOKEN = '(.*?)';"
	token = re.findall(get_token_pat, get_token_data.text)[0]
	# print(token)
	write_token = 'http://site.ip138.com/domain/write.do?input={0}&token={1}'.format(target, token)
	write_token_data = requests.get(write_token, headers=Headers)

	url = 'http://site.ip138.com/domain/read.do?domain=' + target

	response = requests.get(url, headers=Headers)
	data = json.loads(response.text, encoding='utf-8')

	if 'data' in data:
		for ip in data['data']:
			ip_list.append(ip['ip'])

	return ip_list


def geting_openport(ip_list):
	basic = {}
	for i in ip_list:
		openport_list = []
		nm = nmap.PortScanner()
		nm.scan(hosts=i, arguments='-F')
		if nm[i].state() == 'up' and nm[i].all_tcp():
			for key in nm[i]['tcp']:
				openport_list.append(str(key))
		basic[i] = openport_list
	return basic


def geting_subdomain(target):
	Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	url = 'https://www.dnsscan.cn/dns.html'
	i = 1
	all_subdomain = []
	
	while True:
		page = i
		data = {
			'ecmsfrom':'40.73.68.156',
			'show':'UNITED+STATES',
			'num':'',
			'classid':'0',
			'keywords':target,
			'page':page,
		}


		response = requests.post(url, headers=Headers, data=data)
		# print(len(response.text))

		get_subdomain_pat = '<td><a href="(.*?)"'
		subdomain_list = re.findall(get_subdomain_pat, response.text)
		if len(subdomain_list) < 20:
			for j in range(len(subdomain_list)):
				all_subdomain.append(subdomain_list[j])
			break
		else:
			for j in range(20):
				all_subdomain.append(subdomain_list[j])
		i += 1

	set(all_subdomain)

	return all_subdomain


def geting_sidehost(target):
	Headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}
	side_host = {}

	url = 'http://api.webscan.cc/?action=query&ip=' + target
	response = requests.get(url, headers=Headers)
	data = json.loads(response.text, encoding='utf-8')
	# print(data)
	for i in range(len(data)):
		side_host[data[i]['domain']] = data[i]['title']
	
	return side_host