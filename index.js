const jumpscareBtnEL = document.querySelector("#jumpscare-btn");

jumpscareBtnEL.addEventListener("click", async () => {
    try {
        const response = await jumpscareRequest();
        if (response.ok) {
            const rowDiv = document.createElement("div");
            rowDiv.classList.add("row");
            const colDiv = document.createElement("div");
            colDiv.classList.add("col-6");
            const newButton = document.createElement("button");
            newButton.classList.add("btn", "btn-primary");
            newButton.textContent = "asdfdasf";
            
            colDiv.appendChild(newButton);
            rowDiv.appendChild(colDiv);

            const existingElement = document.querySelector('#existing-element-id');
            existingElement.appendChild(rowDiv);
        } else {
            console.error("Failed to fetch jumpscare video.");
        }
    } catch (error) {
        console.error("An error occurred while fetching the jumpscare video:", error);
    }
});

async function jumpscareRequest() {
    try {
        const response = await fetch("https://192.168.1.118:5000/",
            {
                method: "POST"
            }
        )
        return response;
    } catch (error) {
        console.error("An error occurred while fetching the jumpscare video:", error);
        throw error; 
    }
}
