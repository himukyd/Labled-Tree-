// Calculates Cayley's formula (n^(n-2))
function calculateTrees(n) {
  return Math.pow(n, n - 2);
}

function showInfo() {
  const n = parseInt(document.getElementById("nodes").value);
  const count = calculateTrees(n);
  document.getElementById("treeCount").textContent = count.toLocaleString();
  document.getElementById("pruferCount").textContent = count.toLocaleString();
  document.getElementById("count").textContent = "";
  document.getElementById("treeGrid").innerHTML = "";
}

async function generateAllTrees() {
  const n = parseInt(document.getElementById("nodes").value);
  const url = `http://127.0.0.1:8000/all_trees?n=${n}`;
  const res = await fetch(url);
  const data = await res.json();

  if (data.error) {
    alert(data.error);
    return;
  }

  document.getElementById("treeCount").textContent = data.count;
  document.getElementById("pruferCount").textContent = data.count;
  document.getElementById("count").textContent = `Showing ${data.count} labeled trees for n = ${n}`;

  const grid = document.getElementById("treeGrid");
  grid.innerHTML = "";

  data.trees.forEach((imgB64, idx) => {
    const div = document.createElement("div");
    div.className = "tree-box";
    div.innerHTML = `<p><strong>Tree ${idx + 1}</strong></p>
                     <img src="data:image/png;base64,${imgB64}">`;
    grid.appendChild(div);
  });
}
