#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2020-01-10 19:26:12
# @Author  : Awrrays
# @Link    : http://cnblogs.com/Awrrays
# @Version : 1.0

import getopt
import sys
from colorama import Fore, Back, Style, init
import random
import information as info


if __name__ == '__main__':

	usage = r"""
   _                                    
  /_\__      ___ __ _ __ __ _ _   _ ___ 
 //_\\ \ /\ / / '__| '__/ _` | | | / __|
/  _  \ V  V /| |  | | | (_| | |_| \__ \
\_/ \_/\_/\_/ |_|  |_|  \__,_|\__, |___/
                              |___/     

		"""

	init()
	colors = list(vars(Fore).values())
	colored_chars = [random.choice(colors) + char for char in usage]	

	shortargs = 'ht:'
	longargs = ['help', 'target=']

	if len(sys.argv) == 1:
		print(''.join(colored_chars))
		sys.exit()

	opts, args = getopt.getopt(sys.argv[1:], shortargs, longargs)
	for key, value in opts:

		if key in ('-h', '--help'):
			print(Fore.RED + "[!] example: main.py -t xxx.com")
			sys.exit()
		if key in ('-t', '--target'):
			target = value
			i = info.information(target)
			i.start()
			i.handle()
			print(Fore.CYAN + "[+] Generate html file...")
			i.result_to_html()
			print(Fore.CYAN + "[+] Over...")
