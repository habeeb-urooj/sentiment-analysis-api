async function predictSentiment() {
    const review = document.getElementById("review").value;
    const button = document.getElementById("predictBtn");

    if (review.trim() === "") {
    document.getElementById("result").innerHTML =
        "⚠️ Please enter a review.";
    return;
    }

    // Show spinner
    document.getElementById("loading").style.display = "block";
    document.getElementById("result").innerHTML = "";
    button.disabled = true;
    button.innerHTML = "Analyzing...";

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            review: review
        })
    });

    const data = await response.json();

    // Hide spinner
    document.getElementById("loading").style.display = "none";
    button.disabled = false;
    button.innerHTML = "Analyze Sentiment";

   const result = document.getElementById("result");

if (data.prediction.toLowerCase() === "positive") {

    result.className = "positive";

    result.innerHTML = `
        <h3>🟢 Positive 😊</h3>
        <p>Your review expresses a positive sentiment.</p>
    `;

} else {

    result.className = "negative";

    result.innerHTML = `
        <h3>🔴 Negative 😞</h3>
        <p>Your review expresses a negative sentiment.</p>
    `;

}
}

document.getElementById("review").addEventListener("keydown", function(e) {
    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        predictSentiment();
    }
});