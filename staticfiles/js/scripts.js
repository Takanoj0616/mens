// JavaScriptで星をランダム生成
const starContainer = document.createElement("div");
starContainer.id = "starry_sky";
document.body.appendChild(starContainer);

const numberOfStars = 100;
for (let i = 0; i < numberOfStars; i++) {
    const star = document.createElement("div");
    star.className = "star";

    const size = Math.random() * 3 + 2;
    star.style.width = `${size}px`;
    star.style.height = `${size}px`;
    star.style.top = `${Math.random() * 100}%`;
    star.style.left = `${Math.random() * 100}%`;
    star.style.animationDelay = `${Math.random() * 2}s`;

    starContainer.appendChild(star);
}