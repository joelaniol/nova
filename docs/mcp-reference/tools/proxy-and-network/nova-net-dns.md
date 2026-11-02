# `nova.net_dns`

Looks up DNS records like `dig` or `nslookup`, compares several resolvers, and says what the answers mean.

> **Upcoming in 1.0.0-alpha.21:** this tool is not in a published setup yet.

---

## 1. Overview

`nova.net_dns` answers questions such as **"are the DNS records of my domain right?"**, **"did my DNS change propagate?"**, **"why does this name not resolve?"** and **"which name does this IP have?"**. It needs no extra software and no administrator rights.

* **Asked directly.** Nova asks each resolver over UDP port 53 and switches to TCP when an answer is too long for UDP. The query goes from this PC (`route: "direct"`), not through the browser's proxy.
* **A status per answer.** `answered` (records found), `nodata` (the name exists, this type not), `nxdomain` (the name does not exist), `dangling_cname` (a CNAME points to a name that does not exist), `dnssec_failure` (the server fails, but answers with DNSSEC checking turned off), `server_failure`, `refused`, `error`. `timeout`, `unreachable` and `malformed` mean there was no usable answer; they say nothing about the record.
* **Several resolvers compared.** `resolvers=['system','cloudflare','google']` asks each of them. Records all of them agree on are listed once; a resolver that answers differently is listed with its own records. Different A/AAAA addresses are only a note, because CDNs and GeoDNS give different addresses by design; different NS, MX, TXT, SOA, CAA or DS records, or a different status, are reported as findings.
* **More than the records.** The result also names the zone and whether it is DNSSEC-signed (DS record) and validated, checks for a wildcard record, compares the `system` resolver with what Windows itself resolves (hosts file, DNS cache, VPN name rules), and for an IP address checks whether its PTR name resolves back to it.
* **Names of your network stay inside.** Single-label names, names under `.local`, `.internal`, `.lan`, `.corp`, `.home.arpa` and similar, and private IP addresses are never sent to a public resolver; those resolvers are listed under `skipped`.
* **Untrusted text.** TXT records and other texts come from DNS servers and are marked `remoteTextTrust: "untrusted_remote"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | ≤ 253 characters | Domain name to look up (e.g. 'example.com', '_dmarc.example.com', 'www.example.com'; international names are converted), or an IPv4/IPv6 address to look up its PTR (reverse) name. No scheme, path or port. |
| `types` | `array` of `string` | No | — | 1–11 items | Record types to ask for. Default for a name: A, AAAA, MX, NS, TXT (a CNAME chain is reported with every type, so CNAME is only needed alone). For an IP address only PTR. SRV needs the full service name (e.g. '_sip._tcp.example.com'). |
| `resolvers` | `array` of `string` | No | — | 1–4 items | Who to ask, up to 4: 'system' (the DNS servers of this PC's active network adapters, VPN first; the default), 'cloudflare' (1.1.1.1), 'google' (8.8.8.8), 'quad9' (9.9.9.9), or the IP address of a DNS server (port 53). Several resolvers = a propagation comparison. Public resolvers see the names asked. |
| `timeoutMs` | `integer` | No | `2000` | 500–10000 | How long to wait for each answer before trying once more (then the next server of the resolver). Default 2000. |

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
* **Mail setup.** Check `MX` and `TXT` of the domain, plus `TXT` of `_dmarc.<domain>`, to see SPF and DMARC.
* **`dangling_cname` needs action.** A CNAME that points to a name that no longer exists can let someone else take over that subdomain at the provider it points to. Remove the record or create the target again.
* **`dnssec_failure` is not an outage of the server.** The zone's signatures do not validate; resolvers that check DNSSEC refuse the name, others still answer.
* **`os_resolution_differs`** means Windows resolves the name differently from the DNS server: look at the hosts file, the DNS cache or VPN name rules.

---

## 5. Related Tools

* [`nova.net_probe`](nova-net-probe.md) — Checks whether the ports of the host are reachable
* [`nova.tls_inspect`](nova-tls-inspect.md) — Inspects the certificate of the host
* [`nova.net_scan`](nova-net-scan.md) — Finds the devices of a network and what they are
