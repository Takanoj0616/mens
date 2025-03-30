<script>
    const starContainer = document.createElement("div");
    starContainer.id = "starry_sky";
    document.body.appendChild(starContainer);

    const numberOfStars = 150; // 表示する星の数を調整
    for (let i = 0; i < numberOfStars; i++) {
        const star = document.createElement("div");
        star.className = "star";

        // ランダムなサイズ、位置、アニメーション遅延を設定
        const size = Math.random() * 3 + 2;
        star.style.width = `${size}px`;
        star.style.height = `${size}px`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 2}s`;

        starContainer.appendChild(star);
    }
</script>