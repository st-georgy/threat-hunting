def main():
	with open('dns', 'r') as dns, open('hosts', 'r') as hosts:
		dns_lines = dns.readlines()
		dns_lines = [line.strip() for line in dns_lines if line.strip() and line.strip() != "-"]
		hosts_lines = hosts.readlines()
		hosts_lines = [line.strip() for line in hosts_lines if line.strip() and line.strip() != "-" and line.strip() != "#"]
		dns_set = set(dns_lines)
		hosts_set = set(hosts_lines)
		common_lines = dns_set.intersection(hosts_set)

	dns_count = len(dns_lines)
	common_count = len(common_lines)
	percent = round(common_count / dns_count * 100, 2)
	print(f"Процент нежелательного трафика: {percent}%")

if __name__ == '__main__':
	main()