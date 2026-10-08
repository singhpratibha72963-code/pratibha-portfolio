document.getElementById("year").textContent = new Date().getFullYear();

function toggleMenu() {
  document.getElementById("nav").classList.toggle("open");
}
document.querySelectorAll("#nav a").forEach(a => a.addEventListener("click", () => {
  document.getElementById("nav").classList.remove("open");
}));

const form = document.getElementById("contactForm");
const statusBox = document.getElementById("formStatus");
const button = form.querySelector("button");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  statusBox.className = "form-status";
  statusBox.textContent = "Sending...";
  button.disabled = true;

  const data = Object.fromEntries(new FormData(form).entries());

  try {
    const response = await fetch("/api/contact", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(data)
    });
    const result = await response.json();

    if (!response.ok) throw new Error(result.error || "Something went wrong.");
    statusBox.className = "form-status success";
    statusBox.textContent = "Thanks! Your enquiry has been sent.";
    form.reset();
  } catch (error) {
    statusBox.className = "form-status error";
    statusBox.textContent = error.message || "Unable to send. Please email Pratibha directly.";
  } finally {
    button.disabled = false;
  }
});
