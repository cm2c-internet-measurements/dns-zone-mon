#!/usr/bin/env python3
#####################################################################
#####################################################################

import dns.resolver

resolver = dns.resolver.Resolver()

master = "200.3.13.10"
zone = "lacnic.net"

def resolve_a_ns(w_hostname):
    res2 = dns.resolver.query(w_hostname, 'A')
    return res2[0].address
## end def

if __name__ == "__main__":

    ## get nsset for zone

    resolver.nameservers = [master]

    zone_ns_ans = resolver.query(zone, 'NS')

    serials_result = { zone: {} }

    for rdata in zone_ns_ans:
        # print(rdata.to_text())
        ns_hostname = rdata.to_text()
        print("new NS hostname {}".format(ns_hostname))
        # print(repr(serials_result))
        serials_result[zone][ns_hostname] = {}
        serials_result[zone][ns_hostname]['serial'] = 0
        serials_result[zone][ns_hostname]['ip'] = resolve_a_ns(ns_hostname)

    ## Query each ns for its reported serial number

    for server in serials_result[zone].keys():
        print("Querying server {} for zone {} SOA".format(server,zone))
        resolver.nameservers = [ serials_result[zone][server]['ip'] ]
        zone_ns_ans1 = resolver.query(zone, 'SOA')
        serial = zone_ns_ans1[0].serial
        serials_result[zone][server]['serial'] = serial
        print("Serial: {} ".format(serial))


    # ans = dns.resolver.query('lacnic.net', 'SOA')

    # for rdata in ans: 
    #     print(rdata.serial)

    print(repr(serials_result))

## END MAIN

#####################################################################