lookatme.contrib.grapheasy
==========================

This [lookatme](https://github.com/d0c-s4vage/lookatme) extension adds graph support to code blocks.

Setup
-----

__Prerequisites__

  - graphviz
  - graph-easy

__Installation__
  ```bash
  pip3 install lookatme.contrib.grapheasy
  ```
Usage
-----

Add grapheasy into the extensions header in your file:
```yaml
---
title: Making of The Pan Galactic Gargle Blaster
author: Zaphod Beeblebrox
date: 2022-01-25
extensions:
  - grapheasy
---
```
Then define some code blocks:

~~~markdown
# Graph::Easy

http://bloodgate.com/perl/graph/manual/

```grapheasy
[ Ol' Janx Spirit ] - to -> [ Santraginus V Water ]
```

---

# Graphviz

http://www.graphviz.org/

```dot
digraph {
    subgraph cluster_0 {
        a0 -> a1 -> a2 -> a3;
        label = "process \#1";
    }

    subgraph cluster_1 {
        b0 -> b1 -> b2 -> b3;
        label = "process \#2";
    }

    start -> a0;
    start -> b0;
    a1 -> b3;
    b2 -> a3;
    a3 -> a0;
    a3 -> end;
    b3 -> end;
}
```

---

# VCG & GDL

Not tested but sopposedly supported by easy-graph:

- https://www.rw.cdl.uni-saarland.de/people/sander/private/html/gsvcg1.html
- https://www.absint.com/aisee/
~~~
