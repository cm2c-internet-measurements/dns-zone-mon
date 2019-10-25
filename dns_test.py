#!/usr/bin/env python3
#####################################################################
#####################################################################

import dns.resolver
import pprint

resolver = dns.resolver.Resolver()

## resolve A record for a given hostname
def resolve_a_ns(w_hostname):
    '''
    Resolve A record for a given hostname.
    '''
    res2 = dns.resolver.query(w_hostname, 'A')
    return res2[0].address
## end def

## resolve serial numbers from different ns servers for a single zone
def get_serials_for_zone(w_master, w_zone):
    '''
    '''
    ## get nsset for zone

    zone = w_zone
    resolver.nameservers = [w_master]

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

    return serials_result

## end def #####################################################################

## BEGIN MAIN ##################################################################
if __name__ == "__main__":

    serials_result = get_serials_for_zone('200.3.13.11', '179.in-addr.arpa')

    # ans = dns.resolver.query('lacnic.net', 'SOA')
    # for rdata in ans: 
    #     print(rdata.serial)

    pp = pprint.PrettyPrinter()
    pp.pprint(serials_result)

    # print(repr(serials_result))

## END MAIN #####################################################################
