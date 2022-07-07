import http.client as ht
def smss(qw,ticketid):
    conn = ht.HTTPSConnection("api.msg91.com")

    headers = {"apikey":"https://api.msg91.com/api/v5/flow/",
            'authkey' : "357773Akvdmdxjpv6064226eP1",
            'content-type': "application/json"}




    payload = '{"mobiles":"91' + str(qw) + '","flow_id": "625901c4d5b25d6e981f177a","sender": "TECHHP","var": "TKT_' + str(ticketid) + '"}'


    # sending the connection request
    conn.request("POST", "/api/v5/flow", payload, headers)

    res = conn.getresponse()
    data = res.read()