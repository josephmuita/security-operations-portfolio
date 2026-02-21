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
Repeated DNS queries at fixed time intervals may indicate automated communication such as beaconing behavior, which should be reviewed for potential security risks

---

## Screenshots
- `screenshots/dns_overview.png`
- `screenshots/dns_query.png`
- `screenshots/dns_response.png`
- 
NOTES;

Wireshark 

________________________________________
🌍 PART 1 — How DNS Actually Works (Step by Step)

DNS = Domain Name System
Its job:
Translate domain names into IP addresses.
Because computers don’t understand:
google.com
They understand:
142.250.x.x

________________________________________
🔄 What Happens When You Type a Website
Let’s say you type:
github.com
Here’s what happens behind the scenes:

1️⃣ Your Computer Checks Cache
•	“Do I already know the IP?”
•	If yes → skip DNS.
•	If no → continue.

________________________________________
2️⃣ Your Computer Sends a DNS Query
Your PC sends a packet to a DNS server:
“What is the IP address for github.com?”
This is a DNS Query.
It contains:
•	Source IP (your PC)
•	Destination IP (DNS server)
•	Query type (A record = IPv4)
•	Domain name requested
________________________________________

3️⃣ DNS Server Responds
The DNS server replies:
“github.com = 140.82.113.3”
This is a DNS Response.
It contains:
•	The IP address
•	TTL (how long to cache it)
•	Record type
________________________________________

4️⃣ Your Computer Connects to That IP
Now your browser:
•	Opens a TCP connection
•	Starts HTTPS session
•	Loads website
DNS is just the first step.
________________________________________

📦 PART 2 — What a DNS Packet Contains

When you expand a DNS packet in Wireshark, you’ll see:
In a Query:
•	Transaction ID
•	Flags (standard query)
•	Questions section
•	Domain name
•	Type (A, AAAA, MX, etc.)
Example:
Standard query A github.com
________________________________________
In a Response:
•	Same Transaction ID
•	Flags (standard response)
•	Answers section
•	IP address
•	TTL
Example:
Standard query response A github.com A 140.82.113.3
________________________________________

🦈 PART 3 — What Wireshark Does

Wireshark is a packet analyzer.
It:
•	Captures packets
•	Shows protocol details
•	Allows filtering
•	Lets you inspect packet structure
Think of it as:
A microscope for network traffic.
________________________________________
What You See in Wireshark Columns
Column	Meaning
No.	Packet number
Time	Timestamp
Source	Who sent it
Destination	Who received it
Protocol	DNS, TCP, HTTP, etc.
Info	What happened
________________________________________

🔍 PART 4 — Filtering DNS

In the filter bar, you type:
dns
Now Wireshark shows only DNS packets.
You’ll see:
•	Queries (request)
•	Responses (answer)
________________________________________

🧠 PART 5 — Why DNS Matters in Cybersecurity

DNS is monitored because:
•	Malware uses DNS
•	Command & control uses DNS
•	DNS tunneling hides data
•	Suspicious domains reveal compromise
DNS traffic is almost always allowed through firewalls.
That makes it attractive to attackers.
________________________________________

🚨 PART 6 — What Suspicious DNS Looks Like

🚩 1. Random Domains
asdkfj2398.xyz
🚩 2. Many Requests Per Minute
High frequency → possible beaconing.
🚩 3. Long Random Subdomains
asd8f7a98df7a.data.exfil.com
Possible DNS tunneling.
🚩 4. Repeated Requests at Regular Intervals
Every 60 seconds exactly → automated behavior.
Humans don’t browse like that.
________________________________________

📊 PART 7 — What Your Lab Proves

When you upload your Wireshark lab, you are proving:
✅ You understand DNS basics
✅ You know query vs response
✅ You can capture packets
✅ You can filter traffic
✅ You understand security implications
That’s solid entry-level SOC knowledge.
________________________________________

🎤 PART 8 — What You Should Be Able to Explain in Interviews

You should confidently explain:
1.	What DNS does
2.	What a DNS query is
3.	What a DNS response is
4.	Why DNS monitoring matters
5.	What suspicious DNS activity looks like
6.	How you captured traffic using Wireshark
If you can explain those clearly, you’re ahead of most beginners.
________________________________________

🧩 PART 9 — Important Extra Knowledge

DNS Record Types:
•	A → IPv4
•	AAAA → IPv6
•	MX → Mail server
•	NS → Name server
•	TXT → Text records (sometimes abused)
Most browsing uses A and AAAA.
________________________________________

🔥 Final Big Picture

DNS is:
The phonebook of the internet.
Wireshark lets you:
Watch every phone call being made.
SOC analysts use DNS to:
Detect suspicious communication early.
________________________________________

In simple words:
What is the difference between:
•	A DNS query
•	A DNS response
•	And what happens after the response?


