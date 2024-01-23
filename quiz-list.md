---
layout: page
title:  Quizzes
permalink: /quiz-list/
---

{% for q in site.quizzes %}
  <p>
    <a target="_parent" href="..{{ q.url }}">
      {{ q.title }}
    </a>
  </p>
{% endfor %}

