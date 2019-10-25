#!/usr/bin/env python3

import click
import pprint

import monitors.soa-serial-mon as mon

@click.command()
@click.option('--zone', default=None, help='Zone to check.')
@click.option('--master', default=None, help='Master NS server (to get NSSet).')
def checkserial(zone, master):
    print("zone {}, master {}".format(zone,master))
    sr = mon.get_serials_for_zone(master, zone)
    pp = pprint.PrettyPrinter(width=70)
    pp.pprint(sr)

## BEGIN MAIN ##################################################################
if __name__ == "__main__":

    # serials_result = get_serials_for_zone('200.3.13.11', '179.in-addr.arpa')
    checkserial()

    # ans = dns.resolver.query('lacnic.net', 'SOA')
    # for rdata in ans: 
    #     print(rdata.serial)

    # pp = pprint.PrettyPrinter()
    # pp.pprint(serials_result)

    # print(repr(serials_result))

## END MAIN #####################################################################