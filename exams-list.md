---
layout: page
title:  Exams
permalink: /exams-list/
---

{% for hw in site.exams %}
  <p>
    <a target="_parent" href="..{{ hw.url }}">
      {{ hw.title }}
    </a>
  </p>
{% endfor %}

