# Apache-Log-Functions
Useful scripts for parsing Apache Log Files. 

This script can be used to parse Log files from its inital format to a csv format through the use of the [Regular Expression Library] (https://docs.python.org/3/library/re.html). 

This library has the functionality to:
* Returns length of the log file
* Returns the logs as a python list object
* Returns a pandas dataframe from the log file
* Splits the request line to separate the Request Type (Eg. POST) from the request line.
* Converts the time from the log file to a python datetime format
* Performs reverse IP Lookup based on the ipinfodb.com api

Basic examples of a few of the functions: 
### Returns list of logs from logfile
```python
listOfLogs = logToList(logfile):
```

### Returns a Pandas dataframe from log file
```python 
dataframe = dataframeLog(access_logs, access)
```
