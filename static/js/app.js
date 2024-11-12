async function generateImage() {
    const prompt = document.getElementById("prompt").value;
    const loader = document.getElementById("loader");
    const imgContainer = document.getElementById("image-container");

    if (!prompt) {
        alert("Please enter a prompt.");
        return;
    }

    // Show the loader before generating the image
    loader.style.visibility = "visible";

    try {
        const response = await fetch("/generate", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ prompt }),
        });

        if (!response.ok) {
            const error = await response.json();
            alert(error.error || "Error generating image");
            return;
        }

        const blob = await response.blob();
        const imgUrl = URL.createObjectURL(blob);

        // Hide the loader once the image is ready
        loader.style.visibility = "hidden";

        imgContainer.innerHTML = `<img src="${imgUrl}" alt="Generated Image">`;
    } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while generating the image.");
        loader.style.visibility = "hidden"; // Hide loader in case of an error
    }
}

