
Oracle Alert Log Parser
---------------------------------------------------------------------------------------------------

A simple Python utility to parse Oracle alert logs, group multiline entries by timestamps, and extract/count ORA- errors.  
This project demonstrates how to bring structure and analysis to DBA logs using Python instead of shell scripts.


Features
- Groups raw alert log lines into structured **entries** (based on timestamps).
- Extracts and counts **ORA- errors** per entry.
- Prints results in a **human-friendly format** or as **JSON** (for downstream tools).
- Includes a **sample log file** for testing.



Project Structure
