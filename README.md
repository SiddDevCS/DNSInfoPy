# DNS Enumeration Tool with Python

> Note: This project is in progress

# Get started

1. Clone the repo
```shell
git clone https://github.com/SiddDevCS/DNSInfoPy.git
```

2. Go to the project folder:
```shell
cd DNSInfoPy/
```

3. Set up venv (virtual environment)
```shell
python3 -m venv venv
source venv/bin/activate
```

4. Install libraries
```shell
pip install -r requirements.txt
```

5. Run the app
```shell
python3 main.py
```


# Example Usage

```bash
(venv) root@root DNSInfoPy % python3 main.py 

Hi there! This is a tool which you can use for active/passive reconnaissance.
You can use it to gather information about a target domain.

Which of the following would you like to do?
1. Run active reconnaissance
2. Run passive reconnaissance
3. Run record lookup
4. Exit

Enter your choice (1-4): 3
Enter domain name: example.com
A Records: 23.215.0.138, 23.220.75.232, 23.220.75.245, 23.192.228.80, 23.192.228.84, 23.215.0.136
AAAA Records: 2600:1408:ec00:36::1736:7f24, 2600:1408:ec00:36::1736:7f31, 2600:1406:5e00:6::17ce:bc12, 2600:1406:5e00:6::17ce:bc1b, 2600:1406:bc00:53::b81e:94c8, 2600:1406:bc00:53::b81e:94ce
CNAME Records: ERROR: The DNS response does not contain an answer to the question: example.com. IN CNAME
MX Records: 0 .
NS Records: b.iana-servers.net., a.iana-servers.net.
TXT Records: "v=spf1 -all", "_k2n1y4vw3qtb4skdx9e7dxt97qrmmq9"
SOA Records: ns.icann.org. noc.dns.icann.org. 2025082232 7200 3600 1209600 3600
```