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
- Event Viewer (built-in)
- Snipping Tool or Print Screen
- Notepad / Excel (optional)

---

## Method
1. Open Event Viewer → Windows Logs → Security.
2. Filter for Event IDs:
   - 4625 → Failed logins
   - 4624 → Successful logins
   - 4740 → Account lockouts (optional)
3. Review events and note patterns.
4. Capture screenshots of key events.
5. Record observations and insights.

---

## Observations
- **Number of failed logins:** [Insert number]  
- **Username(s) involved:** [Insert usernames]  
- **Notable patterns:** [E.g., multiple failed attempts in a short period]  
- **Account lockouts observed:** [Yes/No]  
- **Other insights:** [Any additional observations]

---

## Key Takeaways
- Windows Event Viewer provides critical log information for IT support and SOC investigations.
- Event ID 4625 is useful for detecting failed authentication attempts.
- Event ID 4740 helps track account security issues and potential attacks.
- Manual analysis can highlight patterns before automating detection.

---

## Screenshots
- `screenshots/security_log_overview.png` → Security log overview
- `screenshots/failed_login_4625.png` → Failed login details
- `screenshots/successful_login_4624.png` → Successful login details
- `screenshots/account_lockout_4740.png` → Account lockout details (if available)
