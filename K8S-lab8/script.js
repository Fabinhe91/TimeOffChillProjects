const API_URL = "http://127.0.0.1:5001/wines";

document.addEventListener("DOMContentLoaded", () => {
  fetchWines();

  const addWineForm = document.getElementById("addWineForm");
  addWineForm.addEventListener("submit", (event) => {
    event.preventDefault();
    addWine();
  });
});

// Fetch and display wines
function fetchWines() {
    fetch(API_URL)
      .then(response => response.json())
      .then(wines => {
        const wineList = document.getElementById("wines");
        wineList.innerHTML = ""; // Limpa a lista antes de renderizar
        wines.forEach(wine => {
          const listItem = document.createElement("li");
          listItem.textContent = `${wine.name} - ${wine.type} (${wine.region}, ${wine.year}) - $${wine.price}`;
          wineList.appendChild(listItem);
        });
      })
      .catch(error => console.error("Error fetching wines:", error));
  }
  
  

// Add a new wine
function addWine() {
  const name = document.getElementById("name").value;
  const type = document.getElementById("type").value;
  const region = document.getElementById("region").value;
  const year = document.getElementById("year").value;
  const price = document.getElementById("price").value;

  const newWine = { name, type, region, year, price };

  fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(newWine)
  })
    .then(response => {
      if (response.ok) {
        fetchWines(); // Refresh the list
        document.getElementById("addWineForm").reset(); // Clear the form
      } else {
        console.error("Error adding wine:", response.statusText);
      }
    })
    .catch(error => console.error("Error adding wine:", error));
}
