document.addEventListener("DOMContentLoaded", function () {
  if (typeof katex !== "object" || typeof renderMathInElement !== "function") return;

  document.querySelectorAll(".kdmath").forEach(function (element) {
    let expression = element.textContent.trim();

    if (expression.startsWith("$$") && expression.endsWith("$$")) {
      expression = expression.slice(2, -2);
    } else if (expression.startsWith("$") && expression.endsWith("$")) {
      expression = expression.slice(1, -1);
    }

    katex.render(expression, element, {
      displayMode: true,
      throwOnError: false,
      strict: false
    });
  });

  renderMathInElement(document.body, {
    delimiters: [
      { left: "$$", right: "$$", display: true },
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
      { left: "$", right: "$", display: false }
    ],
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    ignoredClasses: ["kdmath"],
    throwOnError: false,
    strict: false
  });
});
