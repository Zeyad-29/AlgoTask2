
document.getElementById('dnaForm').addEventListener('submit', (event) => {
    event.preventDefault();
  
    const sonFileInput = document.getElementById('sonFile');
    const fatherFileInput = document.getElementById('fatherFile');
    const resultGrid = document.getElementById('resultGrid');
  
    // Check if both files are uploaded
    if (!sonFileInput.files.length || !fatherFileInput.files.length) {
      alert('Please upload both files.');
      return;
    }
  
    const sonFile = sonFileInput.files[0];
    const fatherFile = fatherFileInput.files[0];
  
    const sonReader = new FileReader();
    const fatherReader = new FileReader();
  
    // Read both files and process DNA comparisons
    sonReader.onload = (e) => {
      const sons = e.target.result.split('\n').filter(row => row.trim());
      fatherReader.onload = (e) => {
        const fathers = e.target.result.split('\n').filter(row => row.trim());
  
        // Validate that both files have the same number of rows
        if (sons.length !== fathers.length) {
          alert('Mismatch: The number of sons and fathers must be the same.');
          return;
        }
  
        resultGrid.innerHTML = ''; // Clear previous results
  
        // Process DNA pairs and generate results
        sons.forEach((sonDna, index) => {
          const fatherDna = fathers[index].trim().toUpperCase();
  
          // Mock similarity calculation
          const similarity = Math.floor(Math.random() * (85 - 50 + 1)) + 50; // Random value between 50% and 85%
          const conclusion = similarity >= 50 ? "Likely Parent-Child Relationship" : "Unlikely Parent-Child Relationship";
  
          // Create grid item for each pair
          const resultItem = document.createElement('div');
          resultItem.classList.add('result-item');
          resultItem.innerHTML = `
            <strong>Pair ${index + 1}</strong><br>
            Similarity: ${similarity}%<br>
            Conclusion: ${conclusion}
          `;
          resultGrid.appendChild(resultItem);
        });
  
        // Show the results section
        document.querySelector('.results').style.display = 'block';
      };
  
      // Read fathers' file
      fatherReader.readAsText(fatherFile);
    };
  
    // Read sons' file
    sonReader.readAsText(sonFile);
  });