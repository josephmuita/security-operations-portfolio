# Windows Event Log Analysis Lab

## Objective
Simulate a small IT/SOC investigation to identify suspicious login activity.  

This lab demonstrates:
- Detection of failed logins
- Account lockouts
- System event analysis
- Pattern recognition for potential security issues

---

## Tools Used
- Windows 10 / 11
- Event Viewer
- Snipping Tool
- Notepad / Excel (optional)

---

## Method
1. Open Event Viewer → Windows Logs → Security  
2. Filter for Event IDs: 4625, 4624, 4740  
3. Capture screenshots of key events  
4. Observe patterns in log entries

---

## Observations
- Number of failed logins: [5]  
- Username(s) involved: [Insert username]  
- Notable patterns: [Insert patterns, e.g., multiple failures from same user]  
- Account lockouts observed: [Yes/No]  

---

## Key Takeaways
- Windows Event Viewer provides critical log information for IT support and SOC investigations  
- Event ID 4625 is useful for detecting failed authentication attempts  
- Event ID 4740 helps track account security issues and potential attacks  
- Manual analysis can highlight patterns before automation  

---

## Screenshots
- `screenshots/failed_login_4625.png`  
- `screenshots/successful_login_4624.png`  
- `screenshots/account_lockout_4740.png` (if available)
