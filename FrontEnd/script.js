async function generateTree() {
  const n = document.getElementById("nodes").value;

  // backend endpoint (localhost for now)
  const url = `http://127.0.0.1:8000/tree?n=${n}`;

  const res = await fetch(url);
  const data = await res.json();

  document.getElementById("tree-title").textContent =
    `Random labeled tree with ${n} vertices`;

  document.getElementById("treeImage").src =
    `data:image/png;base64,${data.image}`;
}
