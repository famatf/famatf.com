---
layout: page
title: Writings
permalink: /writings.html
---

{% if site.categories.writings.size > 0 %}
{% include post_list.html category="writings" %}
{% else %}
<p class="empty-note">尚未发布其他写作。</p>
{% endif %}
