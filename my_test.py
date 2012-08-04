__author__ = 'Dave'

import my_debugger

debugger = my_debugger.debugger()

#debugger.load("C:\\Windows\\system32\\calc.exe")

pid = raw_input("Enter the PID of the process to attach to:")

debugger.attach(int(pid))

debugger.detach()
