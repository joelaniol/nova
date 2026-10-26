# `nova.inspect_component`

Reads the framework component that rendered an element - React props, state, hooks and context, Vue props and state, Angular inputs in development builds - plus the store the component reads from.

---

## 1. Overview

When a page shows a stale value or behaves oddly, the answer is often in the component's memory rather than in the DOM. `nova.inspect_component` goes from an element (CSS selector) to the component that rendered it and returns that component's data, so an agent no longer walks framework internals by hand with `nova.eval`.

* **React:** props, state (class state or the values of `useState`/`useReducer`/`useSyncExternalStore`), every hook with its kind, the contexts the component reads, the context providers above it, and a Redux-style store (`getState()`).
* **Vue 3 and Vue 2:** props and state (setup state and data, refs unwrapped), and the Pinia or Vuex state. Production Vue 3 builds are supported.
* **Angular:** inputs and fields, through Angular's debug API - available in development builds only.
* **Svelte, production Angular:** these keep no component reference on the page; the element is reported as `state_not_reachable` instead of an empty result.
* **Read-only:** values are read as stored; a getter defined by the page is reported as `{ "$type": "getter" }` and not run. The only page functions called are the read functions frameworks provide for this: a store's `getState()` (only when `store` is requested), Vue 2's reactive getters and Angular's debug API.
* **Pick what you need:** `paths` reads only chosen values; `componentName` or `level` selects a component further up; `owners` lists the component names above.
* **Secrets:** component state is page memory and can hold tokens. `redact` (default `true`) masks values under key names such as `token`, `password`, `secret`, `credential`, `api_key`, `cookie` or `authorization`. A secret under a neutral key name is not recognised.

Only the top document is read, not iframes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. Reads the top document. |
| `selector` | `string` | Yes | — | 1–10000 characters | Required CSS selector of the element whose React/Vue/Angular component to read. Supports ' >>> ' for open Shadow DOM. |
| `componentName` | `string` | No | — | ≤ 200 characters | Read the first component above the element with exactly this name (displayName/name, e.g. 'TodoList') instead of the nearest one. |
| `level` | `integer` | No | `0` | 0–199 | Which component above the element: 0 = nearest, 1 = its parent component, and so on. Ignored when componentName is given. |
| `include` | `array` of `string` | No | — | — | Parts returned whole (depth-limited): props, state (class state or useState/useReducer values; Vue setup state and data), hooks (every React hook with its kind), contexts (consumed context values), providers (context providers above), store (the first store found, see storeKind; available.store names it, available.otherStores the rest). Default props, state, hooks; empty when paths is given. |
| `storeKind` | `string` | No | — | `redux`, `store`, `apollo`, `tanstack-query`, `relay`, `urql`, `pinia`, `vuex` | Which store include/paths 'store' reads when the component reaches several: redux or store (getState), apollo (cache.extract(true), the optimistic view queries render), tanstack-query ({queries by queryHash, mutations}), relay (record source), urql (named, not readable: its cache lives in closures), pinia, vuex. Default: the first found, nearest context first. |
| `paths` | `array` of `string` | No | — | ≤ 32 items | Dotted paths of the values to read, starting with props, state, hooks, contexts, providers or store. The second segment of hooks/contexts/providers is an index or a context name. Missing steps answer {$type:'missing', at}. |
| `depth` | `integer` | No | `3` | 0–8 | Object levels expanded below each returned value; deeper objects are summarized with their class and key count. |
| `maxEntries` | `integer` | No | `50` | 1–500 | Maximum keys or items per object, array, Map or Set; $more counts the rest. |
| `offset` | `integer` | No | `0` | 0–100000 | Skip this many matching elements; pass the previous nextOffset to read the next page. |
| `maxItems` | `integer` | No | `5` | 1–100 | Maximum matching elements inspected in document order. |
| `maxChars` | `integer` | No | `20000` | 1000–200000 | Maximum total characters of returned strings and keys; truncation is reported. |
| `redact` | `boolean` | No | `true` | — | true masks values under secret-looking key names. false returns the values as the page holds them. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Example Calls

### What does the component behind a button hold?
```json
{
  "selector": "button.add-to-cart"
}
```

### Read only chosen values of every card in a list
```json
{
  "selector": "li.product-card",
  "paths": ["props.product.id", "props.product.price", "state.0"],
  "maxItems": 20
}
```

### Read the store a view is connected to
```json
{
  "selector": "#cart-summary",
  "componentName": "CartSummary",
  "paths": ["store.cart.total", "contexts.ReactReduxContext.store"]
}
```

---

## 4. Return Value Structure

```json
{
  "targetId": "tab-101",
  "selector": "button.add-to-cart",
  "ok": true,
  "status": "ok",
  "matchedCount": 1,
  "returnedCount": 1,
  "offset": 0,
  "nextOffset": null,
  "hasMore": false,
  "truncated": false,
  "redacted": true,
  "include": ["props", "state", "hooks"],
  "hint": null,
  "matches": [
    {
      "index": 0,
      "element": "button.add-to-cart",
      "framework": "react",
      "status": "ok",
      "component": { "name": "AddToCart", "kind": "function", "key": null, "level": 0 },
      "owners": ["ProductCard", "ProductList", "App"],
      "available": { "contexts": ["ReactReduxContext"], "providers": ["ReactReduxContext"], "store": "redux (context:ReactReduxContext)" },
      "props": { "productId": 42, "onAdd": { "$type": "function", "name": "handleAdd" } },
      "state": [false],
      "hooks": [
        { "index": 0, "kind": "state", "value": false },
        { "index": 1, "kind": "effect", "value": { "deps": [42] } }
      ]
    }
  ]
}
```

With `paths`, each match carries `values` keyed by path instead of whole parts. A path that leads nowhere answers `{ "$type": "missing", "at": "<path up to the missing step>" }`.

Special values are objects with `$type`: `function`, `getter`, `circular`, `node` (a DOM node), `reactElement`, `date`, `map`, `set`, `undefined`, and `object`/`array` summaries below `depth`. Long strings end with `…[+N chars]`; cut lists and objects carry `$more`.

---

## 5. Match Status

| `status` | Meaning | What to do |
| :--- | :--- | :--- |
| `ok` | The component was read. | — |
| `no_framework` | No React, Vue or Angular component was found on the element or its ancestors. | Pick an element the framework renders; page globals can still be read with `nova.eval(worldMode='main')`. |
| `state_not_reachable` | The framework was recognised but keeps no component reference (Svelte, production Angular). `reason` says why. | Read the DOM, network or page globals instead. |
| `component_not_found` | No component above the element has that `componentName`. `owners` lists the names that exist. | Use one of the listed names. |
| `level_out_of_range` | `level` is higher than the number of components above the element. `owners` lists them. | Lower `level`. |

---

## 6. Common Errors

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `Invalid params: path '...' must start with one of props, state, hooks, contexts, providers, store.` | A path does not name a part of the component. | Start the path with one of the listed parts. |
| `Invalid params: selector is not valid CSS.` | The selector could not be parsed. | Fix the selector syntax. |
| `No DOM element matched selector '...'.` | Nothing in the top document matched. | Check the selector; elements inside iframes are not read. |

---

## 7. Related Tools & Documentation

* [`nova.dom_extract`](nova-dom-extract.md) — Fixed DOM properties of many elements, no page memory.
* [`nova.eval`](nova-eval.md) — Run your own expression, including page globals with `worldMode='main'`.
* [`nova.network_read`](nova-network-read.md) — The requests behind a state change.
