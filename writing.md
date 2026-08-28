---
layout: page
title: Writing
permalink: /writing.html
---

{% if site.categories.writing.size > 0 %}
{% include post_list.html category="writing" %}
{% else %}
<p class="empty-note">尚未发布其他写作。</p>
{% endif %}
