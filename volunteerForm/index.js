document.addEventListener("DOMContentLoaded", function () {
  const form = document.querySelector("form");

  form.addEventListener("submit", function (e) {
    e.preventDefault();

    const formData = new FormData(form);

    fetch("http://127.0.0.1:8100/api/submit", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (response.ok) {
          form.reset();
          displayThankYou();
        } else {
          console.error("Error:", response.statusText);
        }
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });

  function displayThankYou() {
    const joinUsSection = document.getElementById("join-us");
    joinUsSection.innerHTML = `
      <div class="join-us-div">
        <h2>Thank You!</h2>
        <p>Your application has been submitted successfully.</p>
      </div>
    `;
  }
});
