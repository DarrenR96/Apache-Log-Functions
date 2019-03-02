# Apache-Log-Functions
Useful scripts for parsing Apache Log Files. 

This script can be used to parse Log files from its inital format to a csv format through the use of the [Regular Expression Library] (https://docs.python.org/3/library/re.html). 

This library provides the functionality for: 
### Returns list of logs from logfile
```python
`listOfLogs = logToList(logfile):`

### Returns a Pandas dataframe from log file
```python 
`dataframe = dataframeLog(access_logs, access)
