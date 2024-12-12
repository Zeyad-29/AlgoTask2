document.getElementById("dnaUploadForm").addEventListener("submit", async (event) => {
    event.preventDefault();

    const sonFile = document.getElementById("sonFile").files[0];
    const fatherFile = document.getElementById("fatherFile").files[0];

    if (!sonFile || !fatherFile) {
        alert("Please upload both files.");
        return;
    }

    try {
        // Read files and send data to the backend
        const sonDNA = await readFileContent(sonFile);
        const fatherDNA = await readFileContent(fatherFile);

        const response = await fetch("/verify_lineage", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ son_dna: sonDNA, father_dna: fatherDNA })
        });

        const result = await response.json();
        displayResults(result);
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while processing the files.");
    }
});

function readFileContent(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result.trim());
        reader.onerror = reject;
        reader.readAsText(file);
    });
}

function displayResults(result) {
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `
        <p>Similarity: ${result.similarity_percentage}</p>
        <p>Conclusion: ${result.conclusion}</p>
    `;
}