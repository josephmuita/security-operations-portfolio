# Wireshark DNS Traffic Analysis Lab

## Objective
Analyze network DNS traffic using Wireshark to detect normal vs suspicious activity.

This lab demonstrates:
- Capturing and filtering DNS packets
- Inspecting source and destination IPs
- Identifying queries and responses
- Understanding basic network traffic analysis for SOC investigations
  
- ## Understanding DNS Traffic

DNS (Domain Name System) translates domain names into IP addresses.

For example:
google.com → 142.250.x.x

When visiting a website, the following happens:

1. My computer sends a **DNS query** asking:
   "What is the IP address of this domain?"

2. The DNS server sends a **DNS response** containing the IP address.

In Wireshark:
- A **DNS query** is an outgoing request from my device.
- A **DNS response** is an incoming reply from the DNS server.

Monitoring DNS traffic helps identify:
- Normal browsing behavior
- Suspicious domains
- Potential malware communication
- Unusual high-frequency requests

This lab demonstrates how to capture and analyze DNS query and response packets using Wireshark.


  

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

  ## Security Insight

Abnormal DNS activity may indicate:
- Malware beaconing
- Communication with command-and-control servers
- DNS tunneling attempts
- Data exfiltration

In this capture, only normal browsing domains were observed.

---

## Screenshots
- `screenshots/dns_overview.png`
- `screenshots/dns_query.png`
- `screenshots/dns_response.png`
