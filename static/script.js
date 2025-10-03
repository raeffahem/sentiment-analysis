async function RunSentimentAnalysis() {

    const textToAnalyze = document.getElementById("textToAnalyze").value;

    if (!textToAnalyze) {
        alert("Please enter some text!");
        return;
    }

    try {
        const response = await fetch("/", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `text=${encodeURIComponent(textToAnalyze)}`
        });

        // Parse JSON response from Flask
        const result = await response.json();

        // Update the output input field
        document.getElementById("result").value =
            `${result.label} (${(result.score * 100).toFixed(2)}%)`;

    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred! Check the console for details.");
    }
}
