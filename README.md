
**Oracle Alert Log Parser**
---------------------------------------------------------------------------------------------------
A simple Python utility to parse Oracle alert logs, group multiline entries by timestamps, and extract/count ORA- errors.  
This project demonstrates how to bring structure and analysis to DBA logs using Python instead of shell scripts.

**Features**
---------------------------------------------------------------------------------------------------
```
1. Groups raw alert log lines into structured entries (based on timestamps).
2. Extracts and counts "ORA- errors" per entry.
3. Prints results in a human-friendly format or as JSON (for downstream tools).
4. Includes a sample log file for testing.
```
**Project Structure**
---------------------------------------------------------------------------------------------------
```
oracle-alert-log-parser/
├── alert_log_parser.py → Main Python script (parses logs, extracts ORA- errors)
├── alert_mock.log → Sample Oracle alert log for testing
├── README.md → Project documentation
├── requirements.txt → Dependencies (currently stdlib only)
├── .gitignore → Ignore venv, pycache, etc.
```
**Usage with example output**
---------------------------------------------------------------------------------------------------
```
Total entries found: 3

--- Entry 1 --- (2 ORA- errors)
Tue Sep 24 12:01:23 2024
Errors in file /u01/app/oracle/diag/rdbms/orcl/trace/orcl_ora_12345.trc:
ORA-00604: error occurred at recursive SQL level 1
ORA-01882: timezone region not found

--- Entry 2 --- (0 ORA- errors)
Tue Sep 24 13:15:45 2024
Thread 1 advanced to log sequence 123 (LGWR switch)

--- Entry 3 --- (1 ORA- error)
Tue Sep 24 14:42:10 2024
Errors in file /u01/app/oracle/diag/rdbms/orcl/trace/orcl_ora_54321.trc:
ORA-01555: snapshot too old: rollback segment number 5 with name "_SYSSMU5$" too small

