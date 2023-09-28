import socket
import dns.resolver

def get_records(domain):
    # A Record
    try:
        a_record = socket.gethostbyname(domain)
        print(f'A Record: {a_record}')
    except socket.gaierror as e:
        print(f'Error fetching A Record: {e}')

    # MX Records
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        print('MX Records:')
        for mx_record in mx_records:
            print(f'{mx_record.exchange} (Preference: {mx_record.preference})')
    except dns.resolver.NoAnswer:
        print(f'No MX Records found for {domain}')
    except Exception as e:
        print(f'Error fetching MX Records: {e}')

    # NS Records
    try:
        ns_records = dns.resolver.resolve(domain, 'NS')
        print('NS Records:')
        for ns_record in ns_records:
            print(ns_record)
    except dns.resolver.NoAnswer:
        print(f'No NS Records found for {domain}')
    except Exception as e:
        print(f'Error fetching NS Records: {e}')

    # TXT Records
    try:
        txt_records = dns.resolver.resolve(domain, 'TXT')
        print('TXT Records:')
        for txt_record in txt_records:
            print(txt_record)
    except dns.resolver.NoAnswer:
        print(f'No TXT Records found for {domain}')
    except Exception as e:
        print(f'Error fetching TXT Records: {e}')

if __name__ == "__main__":
    domain = input("Enter a domain: ")
    get_records(domain)
