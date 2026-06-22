async function sendText(params) {
  const text = document.getElementById("textInput").value;

  const response = await fetch("/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text }),
  });

  const data = await response.json();

  document.getElementById("output").innerText =
    `Sentiment: ${data.label} (${data.score.toFixed(3)})`;
}
