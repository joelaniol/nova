# `nova.net_dns`

Looks up DNS records like `dig` or `nslookup`, compares several resolvers, and says what the answers mean.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_dns` answers questions such as **"are the DNS records of my domain right?"**, **"did my DNS change propagate?"**, **"why does this name not resolve?"** and **"which name does this IP have?"**. It needs no extra software and no administrator rights.

* **Asked directly.** Nova asks each resolver over UDP port 53 and switches to TCP when an answer is too long for UDP. The query goes from this PC (`route: "direct"`), not through the browser's proxy.
* **DNS over HTTPS with `transport: "doh"`.** `cloudflare`, `google` and `quad9` are then asked at their DoH addresses (`cloudflare-dns.com`, `dns.google`, `dns.quad9.net`), or a DoH server you name by its https URL in `resolvers` (a URL alone switches to DoH). The question is encrypted on the way and takes the same route as the browser: through the proxy set in Nova or Windows, never around it; `route` and `resolvers[].route` say which. Without a proxy Nova connects to the providers' known addresses, so DoH also works on networks that block port 53. HTTP problems get statuses of their own: `http_error` (with `httpStatus`), `http_redirect` (often a hotel or guest Wi-Fi login page), `invalid_content_type`, `http_rate_limited`, `tls_error`, `proxy_failed`, `response_too_large`. `system` cannot be asked over DoH.
* **A status per answer.** `answered` (records found), `nodata` (the name exists, this type not), `nxdomain` (the name does not exist), `dangling_cname` (a CNAME points to a name that does not exist), `dnssec_failure` (the server fails, but answers with DNSSEC checking turned off), `server_failure`, `refused`, `error`. `timeout`, `unreachable` and `malformed` mean there was no usable answer; they say nothing about the record.
* **Several resolvers compared.** `resolvers=['system','cloudflare','google']` asks each of them. Records all of them agree on are listed once; a resolver that answers differently is listed with its own records. Different A/AAAA addresses are only a note, because CDNs and GeoDNS give different addresses by design; different NS, MX, TXT, SOA, CAA or DS records, or a different status, are reported as findings.
* **More than the records.** The result also names the zone and whether it is DNSSEC-signed (DS record) and validated, checks for a wildcard record, compares the `system` resolver with what Windows itself resolves (hosts file, DNS cache, VPN name rules), and for an IP address checks whether its PTR name resolves back to it.
* **Mail setup with `checks: ["mail"]`.** For questions like **"why does our mail land in spam?"** or **"is my domain protected against spoofing?"** the result gets a `mail` block:
  * **MX:** the MX hosts with their addresses, a null MX (the domain takes no mail), a domain without MX (mail goes to its own address), hosts without an address, MX names that are CNAMEs, DANE (TLSA) records.
  * **SPF:** evaluated the way a receiving server does, including the 10-lookup limit, loops, includes without SPF and `+all`.
  * **DMARC:** follows RFC 9989, including the policy a subdomain inherits, test mode and report addresses another domain has not authorized.
  * **DKIM:** the keys under the selectors you name in `dkimSelectors` (or common ones), with key length and revoked keys.
  * **MTA-STS, TLS-RPT and BIMI** records.

  This is DNS only: no mail server is contacted, so `mail.limitations` lists what the check cannot show. A part that got no answer is marked `incomplete`, not "missing".
* **Name servers with `checks: ["delegation"]`.** For questions like **"are my name servers set up right?"**, **"what is a lame delegation?"** or **"I am moving my domain to another DNS provider"** the result gets a `delegation` block. Nova follows the name from the DNS root servers down to its zone without using a resolver's cache, and asks:
  * **the parent zone** (for example the `.com` servers) which name servers it hands out, and with which addresses (glue);
  * **each name server of the zone** directly, over UDP and TCP: does it answer for the zone, which SOA serial and NS records does it have, and what does it answer for the record types you asked.

  Findings name a lame delegation (a server that does not serve the zone), parent and zone listing different name servers, missing glue, servers that only answer over UDP, different serials and records between the servers, and a single name server. Before you switch providers, pass the new servers in `candidateNameservers`: they are asked the same way and compared with the current ones. Every finding has a `confidence`; `low` means only that a server did not answer from here, which can also be this network. `delegation.coverage` lists every question that was not asked (question budget, no IPv6 on this PC), and `delegation.limitations` what a check from one PC cannot show. Addresses from DNS that are not public are never contacted.
* **Names of your network stay inside.** Single-label names, names under `.local`, `.internal`, `.lan`, `.corp`, `.home.arpa` and similar, and private IP addresses are never sent to a public resolver; those resolvers are listed under `skipped`.
* **Untrusted text.** TXT records and other texts come from DNS servers and are marked `remoteTextTrust: "untrusted_remote"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | ≤ 253 characters | Domain name to look up (e.g. 'example.com', '_dmarc.example.com', 'www.example.com'; international names are converted), or an IPv4/IPv6 address to look up its PTR (reverse) name. No scheme, path or port. |
| `types` | `array` of `string` | No | — | 1–11 items | Record types to ask for. Default for a name: A, AAAA, MX, NS, TXT (a CNAME chain is reported with every type, so CNAME is only needed alone). For an IP address only PTR. SRV needs the full service name (e.g. '_sip._tcp.example.com'). |
| `resolvers` | `array` of `string` | No | — | 1–4 items | Who to ask, up to 4: 'system' (the DNS servers of this PC's active network adapters, VPN first; the default), 'cloudflare' (1.1.1.1), 'google' (8.8.8.8), 'quad9' (9.9.9.9), or the IP address of a DNS server (port 53), or the https URL of a DoH server (e.g. 'https://dns.example.net/dns-query'; implies transport='doh'). Several resolvers = a propagation comparison. Public resolvers see the names asked. |
| `transport` | `string` | No | — | `udp`, `doh` | 'udp' (default): port 53, TCP when the answer is truncated, always direct. 'doh': DNS over HTTPS through the browser's proxy route; needs cloudflare, google, quad9 or a DoH URL in resolvers. Default 'doh' when resolvers holds an https URL. |
| `timeoutMs` | `integer` | No | `2000` | 500–10000 | How long to wait for each answer before trying once more (then the next server of the resolver). Default 2000. |
| `checks` | `array` of `string` | No | — | 1–2 items | Extra checks. 'mail': can the domain receive mail and how well is mail from it protected against forgery - MX, SPF, DMARC, DKIM, MTA-STS, TLS-RPT, BIMI, DANE TLSA, all asked at the first resolver that answered (up to 90 more questions, at most 40 s). Needs a domain name, not an IP; for the reverse DNS of a sending IP call nova.net_dns with that IP instead. 'delegation': walk from the root to the zone and ask its own name servers directly (UDP and TCP, no recursion; up to 160 more questions, at most 40 s). |
| `dkimSelectors` | `array` of `string` | No | — | 1–10 items | Only with checks=['mail']: DKIM selectors to look up (the s= value in the DKIM-Signature header of a mail from the domain, e.g. 'selector1', 'google'). Without them common selectors of large mail providers are tried; not finding a key there does not mean DKIM is missing. |
| `candidateNameservers` | `array` of `object` | No | — | 1–4 items | Only with checks=['delegation']: name servers that should serve the zone but are not (yet) delegated, e.g. the new provider's servers before the switch. Each is asked like a delegated one; findings say whether it answers authoritatively and with the same serial and records. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `connector_ops` (load it with `nova.tools_bundle(bundle='connector_ops')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.net_dns",
  "arguments": {
    "name": "example.com",
    "types": ["A", "MX", "TXT"],
    "resolvers": ["system", "cloudflare", "google"]
  }
}
```

### Response (shortened)
```json
{
  "structuredContent": {
    "ok": true,
    "name": "example.com",
    "queryName": "example.com",
    "route": "direct",
    "answers": [
      {
        "type": "MX",
        "status": "answered",
        "agreed": false,
        "records": [ { "name": "example.com", "ttl": 3600, "data": "10 mail.example.com" } ],
        "byResolver": [
          { "resolver": "system", "status": "answered", "matchesConsensus": true },
          { "resolver": "cloudflare", "status": "answered", "matchesConsensus": true },
          { "resolver": "google", "status": "answered", "matchesConsensus": false,
            "records": [ { "name": "example.com", "ttl": 120, "data": "10 old-mail.example.com" } ] }
        ]
      }
    ],
    "dnssec": { "zone": "example.com", "signed": true, "dsStatus": "answered" },
    "findings": [
      { "severity": "medium", "code": "resolvers_disagree", "text": "MX: google answers differently." }
    ],
    "remoteTextTrust": "untrusted_remote"
  }
}
```

### Is the mail setup of a domain right?
```json
{
  "name": "nova.net_dns",
  "arguments": { "name": "example.com", "checks": ["mail"], "dkimSelectors": ["selector1"] }
}
```

Shortened `mail` block of the answer:
```json
{
  "mail": {
    "status": "checked",
    "incomplete": false,
    "spf": { "status": "valid", "dnsLookups": 4, "maxDnsLookups": 10, "all": "-" },
    "dmarc": { "status": "found", "foundAt": "example.com", "effectivePolicy": "none", "aggregateReports": ["dmarc@example.com"] },
    "dkim": { "selectorSource": "given", "keys": [ { "selector": "selector1", "keyType": "rsa", "bits": 2048, "revoked": false } ] },
    "limitations": ["DNS only: no mail server was contacted, ..."]
  },
  "findings": [
    { "severity": "low", "code": "dmarc_policy_none", "text": "DMARC for example.com is p=none: monitoring only, forged mail is still delivered. ..." }
  ]
}
```

### Are the name servers of a domain right?
```json
{
  "name": "nova.net_dns",
  "arguments": { "name": "example.com", "types": ["A", "MX"], "checks": ["delegation"] }
}
```

Shortened `delegation` block and a finding:
```json
{
  "delegation": {
    "status": "checked",
    "zone": "example.com",
    "parentZone": "com",
    "nameservers": [
      { "name": "ns1.example.net", "bailiwick": "out_of_bailiwick", "inParent": true, "inChild": true, "resolved": ["198.51.100.53"] },
      { "name": "ns2.example.org", "bailiwick": "out_of_bailiwick", "inParent": true, "inChild": true, "resolved": ["203.0.113.53"] }
    ],
    "authorities": [
      { "nameserver": "ns2.example.org", "address": "203.0.113.53", "udp": { "status": "ok", "aa": false, "authoritativeSoa": false }, "authoritative": false }
    ],
    "coverage": { "questions": 41, "budget": 160, "complete": true, "gaps": [] }
  },
  "findings": [
    { "severity": "high", "code": "lame_delegation", "confidence": "high", "text": "ns2.example.org (203.0.113.53) answers, but not with authority for example.com ..." }
  ]
}
```

### Which name does an IP have?
```json
{
  "name": "nova.net_dns",
  "arguments": { "name": "203.0.113.7" }
}
```

---

## 4. Operational Best Practices

* **Propagation after a change.** Ask `system` together with one or two public resolvers. A resolver that still shows the old record only has it cached; its TTL says how long that can last.
* **Mail setup.** Pass `checks: ["mail"]`. If you have a mail from the domain, take the `s=` value of its `DKIM-Signature` header and pass it in `dkimSelectors`: without it only common selectors are tried, and finding no key there does not mean DKIM is missing. For the reverse name of the server that **sends** the mail, call `nova.net_dns` with that IP address.
* **Changing DNS provider.** Set up the zone at the new provider first, then call `checks: ["delegation"]` with the new servers in `candidateNameservers`. Switch the name servers at the registrar only when no `candidate_*` finding is left; afterwards run the check again to see that parent and zone list the same servers.
* **`dangling_cname` needs action.** A CNAME that points to a name that no longer exists can let someone else take over that subdomain at the provider it points to. Remove the record or create the target again.
* **`dnssec_failure` is not an outage of the server.** The zone's signatures do not validate; resolvers that check DNSSEC refuse the name, others still answer.
* **`os_resolution_differs`** means Windows resolves the name differently from the DNS server: look at the hosts file, the DNS cache or VPN name rules.

---

## 5. Related Tools

* [`nova.net_probe`](nova-net-probe.md) — Checks whether the ports of the host are reachable
* [`nova.tls_inspect`](nova-tls-inspect.md) — Inspects the certificate of the host
* [`nova.net_scan`](nova-net-scan.md) — Finds the devices of a network and what they are
