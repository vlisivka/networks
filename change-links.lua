-- Rename .md to .html in links
function Link(el)
  el.target = el.target:gsub("%.md$", ".html")
  return el
end
