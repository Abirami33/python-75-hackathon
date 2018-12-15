import logging

#logging these activities in a log file called toe.log
logging.basicConfig(filename="toe.log",format='%(asctime)s-%(message)s')

#to record the admin log in with date and time
logging.basicConfig(format='%(asctime)s-%(message)s',level=logging.INFO)
logging.info('Root login occurs')

#day month year hour minute second with log out message
logging.basicConfig(format='%(asctime)s-%(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.warning('root logged out')

#there are many logging options
#logging takes place only above info level

logging.debug("Debug message")  
#debug doesnt gets printed since of less severity
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")
logging.critical("Critical message")
  
#Making to log debug messages also
logging.getLogger().setLevel(logging.DEBUG)
logging.debug("Debug message")

file=open("toe.log","r")
print(file.read())
file.close()

'''OUTPUT:
stud@HP-246-Notebook-PC:~$ python abi_logging.py
2018-12-15 14:02:49,172-root logged out
2018-12-15 14:02:49,172-Warning message
2018-12-15 14:02:49,172-Error message
2018-12-15 14:02:49,172-Critical message
2018-12-15 14:02:49,172-Debug message
2018-12-15 14:05:11,704-root logged out
2018-12-15 14:05:11,704-Warning message
2018-12-15 14:05:11,704-Error message
2018-12-15 14:05:11,704-Critical message
2018-12-15 14:05:11,704-Debug message

'''

