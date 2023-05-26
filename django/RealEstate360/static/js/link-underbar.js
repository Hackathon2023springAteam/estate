const href = location.href;
console.log(href);

let links = document.querySelectorAll("#nav-list > li > a")

for (let i = 0; i < links.length; i++) {
  if (links[i].href == href) {
    console.log(links[i]);
    links[i].classList.add("current");
  }
}
