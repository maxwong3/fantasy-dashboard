document.addEventListener("DOMContentLoaded", () => {
    const playersButton = document.getElementById("players-button");

    if (playersButton) {
        playersButton.addEventListener('click', () => {
        window.location.href = '/players';
    });
    }
});