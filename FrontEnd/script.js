async function generateTree() {
  const n = document.getElementById("nodes").value;
  const res = await fetch(`http://127.0.0.1:8000/tree?n=${n}`);
  const data = await res.json();
  const imgTag = document.getElementById("treeImage");
  imgTag.src = `data:image/png;base64,${data.image}`;
}
