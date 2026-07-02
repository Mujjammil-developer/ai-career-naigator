// Animate progress bars on page load
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".progress-fill").forEach(el => {
    const w = el.style.width;
    el.style.width = "0%";
    setTimeout(() => { el.style.width = w; }, 100);
  });
});
