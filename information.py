#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10 19:26:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


import Message_Collect as g
from colorama import Fore, init


class information():
	def __init__(self, target):
		self.target = target
		self.ip_list = []
		self.subdomain_list = []
		self.sidehost_list = []
		self.openport_list = []
		self.ipport_html = ''
		self.port_html = ''
		self.subdomain_html = ''
		self.sidehost_html = ''
		self.result = ''



	def start(self):
		init()
		print(Fore.CYAN + "[+] Starting Collecting message of the target...")
		print(Fore.CYAN + "[+] Starting Collecting IP...")
		self.ip_list = g.geting_ip(self.target)
		print(Fore.CYAN + "[+] IP acquisition completed...")
		print(Fore.CYAN + "[+] Starting Collecting Port open condition...")
		self.openport_list = g.geting_openport(self.ip_list)
		print(Fore.CYAN + "[+] Port open condition acquisition completed...")
		print(Fore.CYAN + "[+] Starting Collecting subdomain...")
		self.subdomain_list = g.geting_subdomain(self.target)
		print(Fore.CYAN + "[+] Subdomain acquisition completed...")
		print(Fore.CYAN + "[+] Starting Collecting sidehost...")
		self.sidehost_list = g.geting_sidehost(self.ip_list[0])
		print(Fore.CYAN + "[+] Sidehost acquisition completed...")


	def handle(self):
		for key in self.openport_list:
			for i in self.openport_list[key]:
				self.port_html += '{0},'.format(i)
			self.ipport_html += '<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'.format(self.target, key, self.port_html)
		for i in self.subdomain_list:
			self.subdomain_html += '<tr><td>{0}</td></tr>'.format(i)
		for key, value in self.sidehost_list.items():
			self.sidehost_html += '<tr><td>{0}</td><td>{1}</td></tr>'.format(key, self.sidehost_list[key])


	def result_to_html(self):		
		self.result = '''
			<!DOCTYPE html><html><head><meta charset="gbk"><title>The Scan Result</title><meta name="description" content="Get_Info's result."><link rel="stylesheet" type="text/css" href="css/awrrays.css" /></head><body>
			<div id='header'><h1 align="center">The Result of Scan {0}}</h1></div>
			<div id='Basic'><h2>Basic Information</h2><hr size="1px"><table><tr><td>Target</td><td>IP</td><td>OpenPort</td></tr>{1}</table></div>
			<div id='Basic'><h2>Subdomain Display</h2><hr size="1px"><table><tr><td>domain</td></tr>{2}</table></div>
			<div id='Basic'><h2>SideHost Display</h2><hr size="1px"><table><tr><td>domain</td><td>title</td></tr>{3}</table></div></body></html>
			'''.format(self.target, self.ipport_html, self.subdomain_html, self.sidehost_html)

		with open('a.html','w') as fw:
			fw.write(self.result)
			fw.close()

