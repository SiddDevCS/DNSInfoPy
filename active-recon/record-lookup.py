import dns.resolver

dns_domain = input("Enter domain name: ")

def query_record(name, rdtype="A"):
    try:
        answers = dns.resolver.resolve(name, rdtype, lifetime=5)
        return [rdata.to_text() for rdata in answers]
    except Exception as e:
        return ["ERROR: " + str(e)]

records = {
    "A": query_record(dns_domain, "A"),
    "AAAA": query_record(dns_domain, "AAAA"),
    "CNAME": query_record(dns_domain, "CNAME"),
    "MX": query_record(dns_domain, "MX"),
    "NS": query_record(dns_domain, "NS"),
    "TXT": query_record(dns_domain, "TXT"),
    "SOA": query_record(dns_domain, "SOA"),
}

for record_type, result in records.items():
    print(f"{record_type} Records: {', '.join(result)}")