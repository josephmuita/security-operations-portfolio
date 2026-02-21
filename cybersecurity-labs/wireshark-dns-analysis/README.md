# Wireshark DNS Traffic Analysis Lab

## Objective
Analyze network DNS traffic using Wireshark to detect normal vs suspicious activity.

This lab demonstrates:
- Capturing and filtering DNS packets
- Inspecting source and destination IPs
- Identifying queries and responses
- Understanding basic network traffic analysis for SOC investigations

---

## Tools Used
- Wireshark (latest version)
- Windows 10 / 11
- Internet connection
- Browser to generate traffic

---

## Method
1. Open Wireshark and select active network adapter.
2. Start capturing packets.
3. Open websites to generate DNS traffic.
4. Stop capture after 30–60 seconds.
5. Apply filter: `dns`
6. Review DNS query and response packets.
7. Capture screenshots for overview, query, and response.
8. Record observations.

---

## Observations
- Number of DNS queries captured: [Insert number]
- Top queried domains: [Insert domains]
- Source IPs: [Insert IPs]
- Destination IPs: [Insert DNS server IPs]
- Patterns: normal web browsing queries; no suspicious domains detected

---

## Screenshots
- `screenshots/dns_overview.png`
- `screenshots/dns_query.png`
- `screenshots/dns_response.png`
