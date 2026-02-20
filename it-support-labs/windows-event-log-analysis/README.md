# Windows Event Log Analysis Lab

## Objective
Simulate a small IT/SOC investigation to identify suspicious login activity.

This lab demonstrates:
- Detection of failed logins
- Tracking successful logins
- Monitoring privileged activity
- Observing user account modifications
- Pattern recognition for potential security issues

---

## Tools Used
- Windows 11
- Event Viewer (built-in)
- Snipping Tool

---

## Method
1. Open Event Viewer → Windows Logs → Security.
2. Filter for Event IDs:
   - 4625 → Failed logins
   - 4624 → Successful logins
   - 4672 → Authorized elevation
   - 4738 → User account modified
   - 4798 → User enumerated
3. Review events and note patterns.
4. Capture screenshots of key events.
5. Record observations and insights.

---

## Observations
- **Failed logins (4625):** 3 occurrences  
- **Successful logins (4624):** 2 occurrences  
- **Authorized elevation (4672):** 1 occurrence  
- **User account modified (4738):** 1 occurrence  
- **User enumerated (4798):** 11 occurrences  

**Patterns observed:**
- Multiple failed logins followed by a successful login indicate normal login attempts.  
- Authorized elevation shows administrative privilege granted once.  
- User account modification shows one administrative change to an account.  
- User enumeration shows frequent queries of user accounts, which could indicate monitoring or auditing.  

---

## Key Takeaways
- Windows Event Viewer provides critical information for IT support and SOC investigations.  
- Event ID 4625 is useful for detecting failed authentication attempts.  
- Event ID 4624 helps verify successful logins.  
- Event IDs 4672, 4738, and 4798 provide insight into administrative and user management actions.  
- Understanding patterns across multiple events is essential for security monitoring.

---

## Screenshots
- `screenshots/security_log_overview.png`
- `screenshots/failed_login_4625.png`
- `screenshots/successful_login_4624.png`
- `screenshots/authorized_elevation_4672.png`
- `screenshots/user_account_modified_4738.png`
- `screenshots/user_enumerated_4798.png`
