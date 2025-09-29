
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

