#Websites

#Solution_1 - Alex

class Website:
    websites_list = []

    def __init__(self, host, domain, queries=None):
        self.host = host
        self.domain = domain
        if queries:
            self.queries = queries.split(',')
        else:
            self.queries = queries
        self.websites_list += [self]

    def __str__(self):
        if self.queries:
            return f"https://www.{self.host}.{self.domain}/query?=[{']&['.join(self.queries)}]"
        else:
            return f"https://www.{self.host}.{self.domain}"


def main():
    data = input()
    while data != 'end':
        Website(*data.split(' | '))
        data = input()

    for obj in Website.websites_list:
        print(obj)  # Note: the __str__ method is being called


if __name__ == '__main__':
    main()

#Solution_2 - Tundjai

class Website:
    def __init__(self, host, domain, queries=[]):
        self.host = host
        self.domain = domain
        self.queries = queries

    def Print(self):
        seperator = "&"
        if self.queries:
            a = list(map(lambda x: f"[{x}]", self.queries))
            print(f"https://www.{self.host}.{self.domain}/query?={seperator.join(a)}")
        else:
            print(f"https://www.{self.host}.{self.domain}")


websites = []

while True:
    info = input().split(" | ")
    if len(info) == 1:
        break

    host = info[0]
    domain = info[1]

    try:
        queries = info[2].split(",")
        websites.append(Website(host, domain, queries))
    except Exception:
        websites.append(Website(host, domain))

for site in websites:
    site.Print()


#Solution_3

while True:
    info = input().split(" | ")
    if len(info) == 1:
        break

    host = info[0]
    domain = info[1]

    seperator = "&"
    try:
        queries = info[2].split(",")
        queries = map(lambda x: f"[{x}]", queries)
        print(f"https://www.{host}.{domain}/query?={seperator.join(queries)}")
    except Exception:
        print(f"https://www.{host}.{domain}")