document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("preferenceForm");

    form.addEventListener("submit", function (event) {

        event.preventDefault();

        // Get selected genres
        const selectedGenres = Array.from(
            document.querySelectorAll(
                'input[name="genre"]:checked'
            )
        ).map(item => item.value);

        // Get language and budget
        const language = document.getElementById("language").value;
        const budget = document.getElementById("budget").value;

        // Validate preferences
        if (selectedGenres.length === 0) {
            alert("Please select at least one genre!");
            return;
        }

        if (!language || Number(budget) <= 0) {
            alert("Please enter valid preferences!");
            return;
        }

        // Display selected preferences
        let result = document.getElementById("result");

        if (!result) {
            result = document.createElement("div");
            result.id = "result";
            form.appendChild(result);
        }

        result.innerHTML = "";

        const heading = document.createElement("h2");
        heading.textContent = "Your Preferences";

        const details = document.createElement("p");
        details.textContent =
            "Genres: " + selectedGenres.join(", ") +
            " | Language: " + language +
            " | Budget: ₹" + budget;

        const message = document.createElement("p");
        message.textContent =
            "Your preferences are ready for OTT recommendations.";

        result.append(heading, details, message);

        console.log({
            genres: selectedGenres,
            language: language,
            budget: Number(budget)
        });

    });

});