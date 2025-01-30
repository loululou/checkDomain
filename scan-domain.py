#!/usr/bin/env python3

import re
import socket

def is_syntactically_valid(domain: str) -> bool:
    if not domain:
        return False
    
    if len(domain) > 253:
        return False
    
    # Split the domain into labels
    labels = domain.split('.')
    
    # Regex for valid label
    label_regex = re.compile(r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$')
    
    for label in labels:
        if not label_regex.match(label):
            return False
    
    return True

def is_resolvable(domain: str) -> bool:
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def check_domains_from_file(file_path: str):
    with open(file_path, 'r') as f:
        for line in f:
            domain = line.strip()
            if not domain:
                continue  # skip empty lines

            if is_syntactically_valid(domain):
                if is_resolvable(domain):
                    print(f"{domain} -> Valid & Resolvable")
                else:
                    print(f"{domain} -> Valid but NOT Resolvable")
            else:
                print(f"{domain} -> NOT Valid")

if __name__ == "__main__":
    # Change 'domains.txt' to your domain file path
    check_domains_from_file('domains.txt')
